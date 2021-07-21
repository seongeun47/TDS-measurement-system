import serial
import MySQLdb

port = serial.Serial("/dev/ttyACM0", "9600")

db = MySQLdb.connect("localhost", "lse", "1234", "tds")
curs = db.cursor()

while True :
    try :
        data = port.readline()
        
        print("TDS : ")
        print(data)

        curs.execute("""INSERT INTO water(sensor) VALUES (%s)""", [data])
        db.commit()

    except KeyboardInterrupt :
        break

port.close()
db.close()
