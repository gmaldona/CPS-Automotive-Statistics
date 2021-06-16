import csv
import socket
import os
import threading
'''
Parsing the incoming data -> data is separated by ','
'''

'''
    Description: Opens a socket for the java program to communicate with.
                 The socket collects the vehicle data to send to log() and
                 record data.
                 
                 socket is opened on port 7000 unless specified on a different port 
'''
def openSocket(trackLayout: str, trial: int, vehicles: int, port=7000):
    vehicle_data = None
    host = '127.0.0.1'
    for i in range(0, vehicles):
        print("STARTING UP SOCKET", i)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind( (host, port) ) 
            s.listen(5)
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    vehicle_data = data.decode()
            log(vehicle_data.split(','), trackLayout, trial)
            s.close()
            print("CLOSING SOCKET", i)
    
'''
    Data sent by Automotive-CPS:

        ~ Vehicle Message Speed
        ~ Vehicle Model
        ~ Vehicle ID
        ~ Lane
        ~ Battery Level
        ~ Average Velocity
''' 

'''
    description: Logs the data into a csv file from the java program
'''
def log(data: [list], trackLayout: str, trial: int):
    data = [x.strip("\n") for x in data]
    data.insert(0, trackLayout)
    data.insert(0, trial)
    with open('stats.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        file.close()

'''
    description: runs the gradlew build
'''
def run():
    print("running vehicles...")
    os.system("cd ../;./gradlew VelocityDemo")

'''
    description: threads the python socket and gradlew build to communicate with each other
'''
def start(track="figure-8", trials=1, vehicles=1):
    for i in range(1, trials + 1):
        t1 = threading.Thread(target=run) 
        t2 = threading.Thread(target=openSocket, args=(track, i, vehicles))
        t1.start()
        t2.start() 
        t1.join()
        t2.join()
        
start(trials=30, vehicles=2)
