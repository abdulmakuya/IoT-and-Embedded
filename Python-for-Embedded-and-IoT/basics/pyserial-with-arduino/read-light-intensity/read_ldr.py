from serial import Serial

arduino = Serial('COM12', baudrate=115200, timeout=1)
arduino.flush

while True:
    arduino.write(b'r')
    line = arduino.readline().decode()
    print(line)

