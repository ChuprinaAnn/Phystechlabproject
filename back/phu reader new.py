import numpy as np
import matplotlib.pyplot as plt
import struct, time

def ReadPHUFile(file_path, plot=False):
    """
    задается путь к фалу и ставиться флаг строить считыне кривые или нет
    возвращает массив кривых и кол-во кривых файле
    """
    # Tag Types
    tyEmpty8      = struct.unpack(">i", bytes.fromhex("FFFF0008"))[0]
    tyBool8       = struct.unpack(">i", bytes.fromhex("00000008"))[0]
    tyInt8        = struct.unpack(">i", bytes.fromhex("10000008"))[0]
    tyBitSet64    = struct.unpack(">i", bytes.fromhex("11000008"))[0]
    tyColor8      = struct.unpack(">i", bytes.fromhex("12000008"))[0]
    tyFloat8      = struct.unpack(">i", bytes.fromhex("20000008"))[0]
    tyTDateTime   = struct.unpack(">i", bytes.fromhex("21000008"))[0]
    tyFloat8Array = struct.unpack(">i", bytes.fromhex("2001FFFF"))[0]
    tyAnsiString  = struct.unpack(">i", bytes.fromhex("4001FFFF"))[0]
    tyWideString  = struct.unpack(">i", bytes.fromhex("4002FFFF"))[0]
    tyBinaryBlob  = struct.unpack(">i", bytes.fromhex("FFFFFFFF"))[0]


    inputfile = open(file_path, "rb")
    magic = inputfile.read(8).decode("ascii").strip('\0')
    if magic != "PQHISTO":
        print("ERROR: Magic invalid, this is not a PHU file.")
        exit(0)

    version = inputfile.read(8).decode("ascii").strip('\0')
    tagDataList = []    # Contains tuples of (tagName, tagValue)
    while True:
        tagIdent = inputfile.read(32).decode("ascii").strip('\0')
        tagIdx = struct.unpack("<i", inputfile.read(4))[0]
        tagTyp = struct.unpack("<i", inputfile.read(4))[0]
        if tagIdx > -1:
            evalName = tagIdent + '(' + str(tagIdx) + ')'
        else:
            evalName = tagIdent
        if tagTyp == tyEmpty8:
            inputfile.read(8)
            tagDataList.append((evalName, "<empty Tag>"))
        elif tagTyp == tyBool8:
            tagInt = struct.unpack("<q", inputfile.read(8))[0]
            if tagInt == 0:
                tagDataList.append((evalName, "False"))
            else:
                tagDataList.append((evalName, "True"))
        elif tagTyp == tyInt8:
            tagInt = struct.unpack("<q", inputfile.read(8))[0]
            tagDataList.append((evalName, tagInt))
        elif tagTyp == tyBitSet64:
            tagInt = struct.unpack("<q", inputfile.read(8))[0]
            tagDataList.append((evalName, tagInt))
        elif tagTyp == tyColor8:
            tagInt = struct.unpack("<q", inputfile.read(8))[0]
            tagDataList.append((evalName, tagInt))
        elif tagTyp == tyFloat8:
            tagFloat = struct.unpack("<d", inputfile.read(8))[0]
            tagDataList.append((evalName, tagFloat))
        elif tagTyp == tyFloat8Array:
            tagInt = struct.unpack("<q", inputfile.read(8))[0]
            tagDataList.append((evalName, tagInt))
        elif tagTyp == tyTDateTime:
            tagFloat = struct.unpack("<d", inputfile.read(8))[0]
            tagTime = int((tagFloat - 25569) * 86400)
            tagTime = time.gmtime(tagTime)
            tagDataList.append((evalName, tagTime))
        elif tagTyp == tyAnsiString:
            tagInt = struct.unpack("<q", inputfile.read(8))[0]
            tagString = inputfile.read(tagInt).decode("ascii").strip("\0")
            tagDataList.append((evalName, tagString))
        elif tagTyp == tyWideString:
            tagInt = struct.unpack("<q", inputfile.read(8))[0]
            tagString = inputfile.read(tagInt).decode("ascii").strip("\0")
            tagDataList.append((evalName, tagString))
        elif tagTyp == tyBinaryBlob:
            tagInt = struct.unpack("<q", inputfile.read(8))[0]
            tagDataList.append((evalName, tagInt))
        else:
            print("ERROR: Unknown tag type")
            exit(0)
        if tagIdent == "Header_End":
            break

    # Reformat the saved data for easier access
    tagNames = [tagDataList[i][0] for i in range(0, len(tagDataList))]
    tagValues = [tagDataList[i][1] for i in range(0, len(tagDataList))]


    # Write histogram data to file
    curveIndices = [tagValues[i] for i in range(0, len(tagNames))\
                    if tagNames[i][0:-3] == "HistResDscr_CurveIndex"]
    curves=[]
    for i in curveIndices:
        histogramBins = tagValues[tagNames.index("HistResDscr_HistogramBins(%d)" % i)]
        resolution = tagValues[tagNames.index("HistResDscr_MDescResolution(%d)" % i)]
        t = np.linspace(0, round(histogramBins*resolution*1e9),histogramBins, False)
        hist_data = []
        for j in range(0, histogramBins):
            try:
                histogramData = struct.unpack("<i", inputfile.read(4))[0]
            except:
                print("The file ended earlier than expected, at bin %d/%d."\
                      % (j, histogramBins))
            hist_data.append(histogramData)

        curves.append(np.array([t, np.array(hist_data)]).transpose())

    inputfile.close()
    n=0
    if plot:
        for i in curves:
            plt.plot(i[:,0], i[:,1], label = str(n))
            n+=1
        plt.xlabel("time, ns")
        plt.ylabel("Intensity, counts")
        plt.yscale("log")
        plt.grid()
        plt.legend()
        plt.show()

    return curves, n


path = "phu_example.phu"
data, n = ReadPHUFile(path, True)