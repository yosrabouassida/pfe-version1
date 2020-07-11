#perception -> Decision ->Navigation
from flask import Flask
import requests
import time

#r = requests.post('https://httpbin.org/post', data = {'key':'value'})
#print(r.text)

r = requests.get('http://0.0.0.0:5002/envoyerMsg')
print("request received from decision module at ")
reqdecision=time.time()
print(reqdecision)
print(r.text)
a=float(r.text)
print(a)

print("temps d'envoi d'une requete from decision to navigation")
reqdecnav=reqdecision-a
print(reqdecnav)

app = Flask(__name__)
print("debut decision")
d=time.time()
print("d")
print(d)
execdecision = requests.get('http://0.0.0.0:5002/envoyerMsg1')
reqperceptiondeci = requests.get('http://0.0.0.0:5002/envoyerMsg2')
execpercep = requests.get('http://0.0.0.0:5002/envoyerMsg3')

@app.route('/')
def hello_world():
    return "hello from navigation module"
print("le module decision s'execute")
f=time.time()
print("f")
print(f)
execnav=f-d
print("temps d'execution du module navigation")
print(execnav)
print("à partir du moment où perception envoie une requête au Decision + exécution de Décision +requête envoyée de Decision vers Navigation + exécution de Navigation")
b=float(execpercep.text)
c=float(reqperceptiondeci.text)
d=float(execdecision.text)
print("exection perception")
print(b)
print("req from perception to decision")
print(c)
print("execution decision")
print(d)
print("req from decision to navigation")
print(reqdecnav)
print("execution navigation")
print(execnav)
print("temps d'execution de chemin total")
print(b+c+d+reqdecnav+execnav)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)