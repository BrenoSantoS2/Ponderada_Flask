from serial.serialutil import SerialException
from serial.tools import list_ports
from moveJ import Arm

# Encontra automaticamente a porta em que o robô está conectado
# robot = None

def find_port():
    available_ports = list_ports.comports()
    robot_is_connected = False

    for port in available_ports:
        if "Dispositivo Serial USB" in port.description:
            chosen_port = port.device
            print(f"Porta encontrada: {chosen_port}")
            robot_is_connected = True
            print(chosen_port)
            return chosen_port, robot_is_connected
        
    print("Nenhuma porta encontrada para o robô.")
    return None, robot_is_connected

# Função responsável por iniciar a ferramenta conectado ao robo
def initialize_tool():
    robot = None
    if robot == None:
        try:
            robot = Arm(port=find_port()[0], verbose=False)
        except SerialException as e:
            print(f"Erro ao abrir a porta serial: {e}")

    robot.wait(200)
    robot.suck(True)
    robot.close()

    return "Ferramenta inicializada com sucesso!"


# Função responsável por desligar a ferramenta conectado ao robo
def turn_off_tool():
    robot = None
    if robot == None:
        try:
            robot = Arm(port=find_port()[0], verbose=False)
        except SerialException as e:
            print(f"Erro ao abrir a porta serial: {e}")

    robot.wait(200)
    robot.suck(False)
    robot.close()

    return "Ferramenta desligada com sucesso!"

# Função responsável por levar ao robo de volta a posição inicial
def home():
    robot = None
    if robot == None:
        try:
            robot = Arm(port=find_port()[0], verbose=False)
        except SerialException as e:
            print(f"Erro ao abrir a porta serial: {e}")

    robot.wait(300)
    robot.movej_to(230, 1, 159, 0, wait=True)
    robot.close()

    return "Robo levado a posição inicial com sucesso!"

# Função responsável por mover o robo para a distância e eixo escolhido pelo usuário
def move(axle,distance):
    robot = None
    if robot == None:
        try:
            robot = Arm(port=find_port()[0], verbose=False)
        except SerialException as e:
            print(f"Erro ao abrir a porta serial: {e}")
            
    actual_position = robot.pose()
    x,y,z,w = actual_position[:4]
    
    if axle == "x":
        robot.wait(300)
        robot.movej_to(x + float(distance), y, z, w, wait=True)
    
    elif axle == "y":
        robot.wait(300)
        robot.movej_to(x, y + float(distance), z, w, wait=True)
    
    elif axle == "z":
        robot.wait(300)
        robot.movej_to(x, y, z + float(distance), w, wait=True)
    
    robot.close()
    return f"Robo movido {distance} no eixo {axle} com sucesso!"

# Função responsável por mostrar no console a localização atual do robo
def actual_location():
    robot = None
    if robot == None:
        try:
            robot = Arm(port=find_port()[0], verbose=False)
        except SerialException as e:
            print(f"Erro ao abrir a porta serial: {e}")
    x,y,z,r,_,_,_,_ = robot.pose()
    robot.close()
    return f"The actual robot position is: {x}, {y}, {z}, {r}"

# Função responsável fechar o looping e fechar a conexão com robo
def turn_off_robot():
    global running
    running = False
    return "Robo desligado com sucesso!"