from serial.tools import list_ports
import serial, time
import numpy as np
import matplotlib.pyplot as plt

# command list for piezo
'''

command content
s -- shows all available commands
setk -- switches the remote control for one channel on or off
cloop -- switches one channel to closed loop or open loop ()
set -- sets the values to one channel
setall -- sets the values to all channels
rk -- measures either the position (only NV40/3CLE, NV120/1CLE) or voltage
(only NV40/3, NV120/1) only for one channel
measure -- gives values of all channels either for position () or voltage
monwpa -- switches the monitor in different modes
fenable -- enables the soft start function for the given channel
fready -- enables the soft start function for all channels
encmode -- encoder: mode (EN)
enctime -- encoder: sample interval (SI)
enclim -- encoder: maximum step
encexp -- encoder: exponent for calculation of acceleration (EM0)
encstol -- encoder: interval for “open loop” (EM1,2)
encstcl -- encoder: interval for “closed loop” (EM1,2) ()
ver -- gives the version number of controller and amplifier software
ERR? -- shows the last occurred error
light -- display brightness (0...255)


'''
piconame = "piezojena NV40/3CL USB"
ports = list(list_ports.comports())

resultPorts = []
descriptions = []
com_port_piezo = ''
for port in ports:
    if port.device:
        resultPorts.append(port.device)
        descriptions.append(str(port.description))
for i in descriptions:
    if i == piconame:
        com_port_piezo = resultPorts[i]


class Piezo(si.SerialInstrument):

    def __init__(self, port=com_port_piezo):
        self.termination_character = '\r'
        self.port_settings = {
            'baudrate': 19200,
            'bytesize': serial.EIGHTBITS,
            'stopbits': serial.STOPBITS_ONE,
            'timeout': 0.5,  # wait at most half second for a response
            'xonxoff': True

        }
        si.SerialInstrument.__init__(self, port=com_port_piezo)

    '''def move_rel(self, axe, value, unit="n"):
        if unit == "n":
            multiplier = 0.001
        elif unit == "u":
            multiplier = 1

        if axe != "X" or "Y" or "Z":
            print("Invalid axes, try again")

        if axe == "X":
            if (value * multiplier + self.write('rk,0')) > 80 or (value * multiplier + self.position) < 0.001:
                print("The value is out of range! 0-100 um (0-1E8 nm) (Z)")
            elif (value * multiplier + self.position) < 1E5 and (value * multiplier + self.position) >= 0:
                self.write(f"MOVRX {str(value) + unit}")
                self.position = (value * multiplier + self.position)
        elif axe == "Y":
            if (value * multiplier + self.position) > 1E5 or (value * multiplier + self.position) < 0:
                print("The value is out of range! 0-100 um (0-1E8 nm) (Z)")
            elif (value * multiplier + self.position) < 1E5 and (value * multiplier + self.position) >= 0:
                self.write(f"MOVRY {str(value) + unit}")
                self.position = (value * multiplier + self.position)
        elif axe == "Y":
            if (value * multiplier + self.position) > 1E5 or (value * multiplier + self.position) < 0:
                print("The value is out of range! 0-100 um (0-1E8 nm) (Z)")
            elif (value * multiplier + self.position) < 1E5 and (value * multiplier + self.position) >= 0:
                self.write(f"MOVRZ {str(value) + unit}")
                self.position = (value * multiplier + self.position)'''

    def set_pos(self, axe, value, unit):
        if unit == "n":
            multiplier = 0.001
        elif unit == "u":
            multiplier = 1

        if axe != "X" or "Y" or "Z":
            print("Invalid axes, should be X, Y or Z!")
        if value * multiplier < 0.001 or value * multiplier > 80:
            print("Invalid range, should be between 0.001u and 80.000u!")

        elif value * multiplier < 80 and value * multiplier >= 0:
            if axe == "X":
                self.write('set,0,' + str(value * multiplier) + '\r'.encode())
            elif axe == "Y":
                self.write('set,1,' + str(value * multiplier) + '\r'.encode())
            elif axe == "Z":
                self.write('set,2,' + str(value * multiplier) + '\r'.encode())
        return self.write('measure'.encode())

    def position(self):
        return self.write('measure'.encode())

    '''def line(self, axe, start, end, step, unit="n"):
        if unit == "n":
            multiplier = 0.001
        elif unit == "u":
            multiplier = 1

        if axe != "X" or "Y" or "Z":
            print("Invalid axes, try again")

        if start * multiplier < 0.001 or start * multiplier > 80 or end * multiplier < 0.001 or end * multiplier > 80:
            print("Invalid range, should be between 0.001u and 80.000u!")
        else:
            if axe == "X":
                x_list = np.arange(0, start*multiplier + step*multiplier, step*multiplier)
                for i in x_list:
                    command = 'set,0,' + str(i) + '\r'
                    self.write(command.encode())
                    time.sleep(aq_time)
            elif axe == "Y":
                y_list = np.arange(0, start*multiplier + step*multiplier, step*multiplier)
                for i in y_list:
                    command = 'set,1,' + str(i) + '\r'
                    self.write(command.encode())
                    time.sleep(aq_time)
            elif axe == "Z":
                z_list = np.arange(0, start * multiplier + step * multiplier, step * multiplier)
                for i in z_list:
                    command = 'set,2,' + str(i) + '\r'
                    self.write(command.encode())
                    time.sleep(aq_time)
'''

    def scan_3d_vol(self, axe_conf="XYZ", start=[0, 0, 0], stop=[0, 0, 0], step=[0, 0, 0], unit=['u', 'u', 'u'],
                    aq_time=0.1):
        configs = ["XYZ", "XZY", "YXZ", "YZX", "ZYX", "ZXY", "XY", "XZ", "YZ", "YX", "ZY", "ZX", "X", "Y", "Z"]
        multiplier = [1, 1, 1]
        for i in range(len(unit)):
            if unit[i] == 'u':
                multiplier[i] = 1
            elif unit[i] == 'n':
                multiplier[i] = 0.001
            else:
                print('Invalid units!')
        if axe_conf not in configs:
            print("Invalid axes configuration!")
        else:
            x_list = np.arange(start[0] * multiplier[0], stop[0] * multiplier[0] + step[0] * multiplier[0],
                               step[0] * multiplier[0])
            y_list = np.arange(start[1] * multiplier[1], stop[1] * multiplier[1] + step[1] * multiplier[1],
                               step[1] * multiplier[1])
            z_list = np.arange(start[2] * multiplier[2], stop[2] * multiplier[2] + step[1] * multiplier[2],
                               step[2] * multiplier[2])
            spl = list(axe_conf)
            conf_dic = {"X": x_list, "Y": y_list, "Z": z_list}
            conf_com = {"X": 0, "Y": 1, "Z": 2}
            if len(spl) == 1:
                for i in conf_dic[spl[0]]:
                    command = 'set,' + str(conf_com[spl[0]]) + ',' + str(i) + '\r'
                    self.write(command.encode())
                    time.sleep(aq_time)
            elif len(spl) == 2:
                arr_step = 1
                for i in conf_dic[spl[0]]:
                    command = 'set,' + str(conf_com[spl[0]]) + ',' + str(i) + '\r'
                    self.write(command.encode())
                    for j in conf_dic[spl[1]]:
                        command = 'set,' + str(conf_com[spl[1]]) + ',' + str(i) + '\r'
                        self.write(command.encode())
                        time.sleep(aq_time)
                    arr_step *= -1
            elif len(spl) == 3:
                for k in conf_dic[spl[2]]:
                    command = 'set,' + str(conf_com[spl[2]]) + ',' + str(k) + '\r'
                    self.write(command.encode())
                    arr_step = 1
                    for i in conf_dic[spl[0]]:
                        command = 'set,' + str(conf_com[spl[0]]) + ',' + str(i) + '\r'
                        self.write(command.encode())
                        for j in conf_dic[spl[1]]:
                            command = 'set,' + str(conf_com[spl[1]]) + ',' + str(j) + '\r'
                            self.write(command.encode())
                            time.sleep(aq_time)
                        arr_step *= -1
                    time.sleep(aq_time)
        return self.write('measure'.encode())

    def scan_3d_free(self, data_points, units=['u', 'u', 'u'], aq_time=0.1):
        multiplier = [1, 1, 1]
        for i in range(len(unit)):
            if unit[i] == 'u':
                multiplier[i] = 1
            elif unit[i] == 'n':
                multiplier[i] = 0.001
            else:
                print('Invalid units!')
        for i in len(data_points):
            if data_points < 0 or data_points > multiplier * 80:
                print('Data points are out of range!')
        x_list = [j for j in data_points[0][j]]
        y_list = [j for j in data_points[1][j]]
        z_list = [j for j in data_points[2][j]]
        for i in range(len(data_points)):
            self.write('set,0,' + str(x_list[i] * multiplier[0]) + '\r'.encode())
            self.write('set,1,' + str(y_list[i] * multiplier[1]) + '\r'.encode())
            self.write('set,2,' + str(z_list[i] * multiplier[2]) + '\r'.encode())
            time.sleep(aq_time)
        return self.write('measure'.encode())

    def INFO(self):
        return self.query('ver'.encode(), multiline=True, termination_line="\n \n \n \n", timeout=.1)


'''
# preset
aq_time = 0.1 #s
x_list = np.arange(0,x_max+x_step,x_step)
y_list = np.arange(0,y_max+y_step,y_step)
z_list = np.arange(0,z_max+z_step,z_step)
arr_step = 1
full_list = []
for y in y_list:
    for x in x_list[::arr_step]:
        full_list.append([x,y])
    arr_step*=-1
full_list = np.array(full_list)
plt.figure(dpi=200, figsize=(8,6))
plt.plot(full_list[:,0], full_list[:,1],'-o')
plt.axis('equal')
plt.show()

# Запуск сканирования
k = 0
with serial.Serial(port=com_port, baudrate=19200, xonxoff=True) as ser:
    for i in y_list:
        command = 'set,0,'+str(i)+'\r'
        ser.write(command.encode())
        for j in x_list[::arr_step]:
            command = 'set,1,'+str(j)+'\r'
            ser.write(command.encode())
            time.sleep(aq_time)
        arr_step*=-1
        command_z = 'set,2,'+str(z_list[k])+'\r'
        ser.write(command_z.encode())
        k += 1
arr_step=1
'''
