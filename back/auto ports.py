from serial.tools import list_ports


def listPorts():

    ports = list(list_ports.comports() )

    resultPorts = []
    descriptions = []
    for port in ports:
        if port.device:
            resultPorts.append( port.device )
            descriptions.append( str( port.description ) )

    return (resultPorts, descriptions)


print(listPorts())