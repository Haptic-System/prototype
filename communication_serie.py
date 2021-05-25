import serial as s
import time as t
import itertools as tools



arduino_serie=s.Serial(port="COM3",baudrate=1000000,
timeout=0,write_timeout=0 )
#/dev/ttyACM0

def start():
    if not arduino_serie.isOpen():
        print("Impossible d'ouvrir le port Serie")
        quit()


start()


"""def mesure(nb_val=3):
    k=0
    vec=[]
    while True: #collects mesurements
        k+=1
        arduino_serie.write('r'.encode('ascii'))
        line = arduino_serie.readline()

        new_line =line.decode('utf-8')
        vec.append(new_line)
        print(new_line)
        if k>= nb_val:
            break
    new_vec=[float(e[0:])for e in vec]
    return new_vec
"""
global line
global message
message = []
line = ""
global cpt
cpt=0
global cpt2
cpt2 = 0
def mesure():
    #print("################################################")
    global line
    vec=[]
    while True: #collects mesurements
        tmp = arduino_serie.readline()
        try :
            line = line + tmp.decode('ascii')
            if '\\n'in str(tmp):         # check if full data is received.
                vec.append(line.rstrip())
                line = ""
            else:
                break
        except:
            global cpt2
            cpt2 += 1
            print("error " + str(cpt2))
        #print(new_line)
    #new_vec=[float(e[0:])for e in vec]
    res = []
    global message
    for v in vec:
        if len(message) == 0:
            if v== "#" :
                message.append(v)
        else:
            try:
                val_max = 1024
                e= float(v)/val_max
                if e >= val_max:
                    e = 0.0
                message.append(e)
            except Exception:
                #print("message non valide")
                global cpt
                cpt += 1
                if cpt == 1000:
                    print(v)
                    print("erreur ! " + str(cpt))
                    cpt = 1
                message = []
            if len(message) == 4:
                #print(message)
                res.append( [message[1], message[2],message[3]] )
    return res


def end():
    arduino_serie.close()
    print("closed")

if __name__== "__main__":
    start()
    cpt = 0
    while True:
        for (sample, sampley, samplez) in mesure():
            cpt +=1
            if cpt == 1000:
                cpt = 0
                print( sample, sampley, samplez)
