import time
import paho.mqtt.client as paho
from dotenv import dotenv_values

#Variable de configuracion
broker = "localhost"
port = 1883
topico1_luces = "actuadores/luces/1"
topico2_volar = "actuadores/volar"
topico3_motores1 = "actuadores/motores/1"
topico4_motores2 = "actuadores/motores/2"
topico5_motores3 = "actuadores/motores/3"
topico6_motores4 = "actuadores/motores/4"
topico7_joystick = "actuadores/joystick"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt conectado")
    else:
        print(f"Mqtt connection faild, error code={rc}")

#Crear el cliente MQTT y conectarse la IP y puerto definidos:
client = paho.Client("Drone")
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()
#Enviar informacion (topic,payload.)
client.publish(topico2_volar,1)
client.publish(topico7_joystick,'{"x": 0, "y": 0}')
time.sleep(4)
client.publish(topico7_joystick,'{"x":-1, "y": 0}')
time.sleep(4)
client.publish(topico7_joystick,'{"x": 0, "y": 1}')
time.sleep(4)
client.publish(topico7_joystick,'{"x": 1, "y": 1}')
time.sleep(4)
client.publish(topico7_joystick,'{"x": 0, "y": 0}')
time.sleep(2)
luz =1
for i in range(40):
    client.publish(topico1_luces,luz)
    time.sleep(2)
    if luz ==1:
        luz =0
    else:
        luz = 1

client.publish(topico2_volar,0)
time.sleep(3)
#Finalizar el script con la desconexión del publicador y la finalización del cliente MQTT:
client.disconnect()
client.loop_stop()
