from serial.tools import list_ports
from moveJ import Arm

# Encontra automaticamente a porta em que o robô está conectado
def find_port():
    available_ports = list_ports.comports()
    robot_is_connected = False

    for port in available_ports:
        if "Dispositivo Serial USB" in port.description:
            chosen_port = port.device
            print(f"Porta encontrada: {chosen_port}")
            robot_is_connected = True
            return chosen_port, robot_is_connected
        
    print("Nenhuma porta encontrada para o robô.")
    return None, robot_is_connected

#Instancia a biblioteca do robo.
if find_port()[1] == True:
    robot = Arm(port=find_port()[0], verbose=False)

# Função responsável por iniciar a ferramenta conectado ao robo
def initialize_tool():
    robot.wait(200)
    robot.suck(True)

# Função responsável por desligar a ferramenta conectado ao robo
def turn_off_tool():
    robot.wait(200)
    robot.suck(False)

# Função responsável por levar ao robo de volta a posição inicial
def home():
    robot.wait(300)
    robot.movej_to(230, 1, 159, 0, wait=True)

# Função responsável por mover o robo para a distância e eixo escolhido pelo usuário
def move(axle,distance):
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

# Função responsável por mostrar no console a localização atual do robo
def actual_location():
    actual_position = robot.pose()
    print(f"The actual robot position is: {actual_position}")

# Função responsável fechar o looping e fechar a conexão com robo
def turn_off_robot():
    global running
    running = False