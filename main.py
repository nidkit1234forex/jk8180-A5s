import os
import json

with open("set-mode/mode.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    mode = loads['mode']
    print("MODE     =",mode)

if  mode == "1":
 with open("set-miner-on/ccminer.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    pool = loads['pool']
    wallet = loads['wallet']
    password = loads['pass']
    print("POOL     =",pool)
    print("WALLET   =",wallet)
    print("PASSWORD =",password)
 POOL=pool
 WALLET=wallet
 PASSWORD=password

 with open("set-miner-off/offline.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    name = loads['name']
    cpu = loads['cpu']
    print("NAME     =",name)
    print("CPU      =",cpu)
 NAME=name
 CPU=cpu
 os.system(f"cd miner && ./ccminer -a verus -o {POOL} -u {WALLET}.{NAME} -p {PASSWORD} -t {CPU}")

if  mode == "2":
 with open("set-miner-on/xmrigcc.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    algo = loads['algo']
    pool = loads['pool']
    wallet = loads['wallet']
    password = loads['pass']
    print("ALGO     =",algo)
    print("POOL     =",pool)
    print("WALLET   =",wallet)
    print("PASSWORD =",password)
 ALGO=algo
 POOL=pool
 WALLET=wallet
 PASSWORD=password

 with open("set-miner-off/offline.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    name = loads['name']
    cpu = loads['cpu']
    print("NAME     =",name)
    print("CPU      =",cpu)
 NAME=name
 CPU=cpu
 os.system(f"cd miner && ./xmrigDaemon -o {POOL} -a {ALGO} -u {WALLET}@{NAME} -p {PASSWORD} -k, --rig-id= {NAME} -t {CPU}")


