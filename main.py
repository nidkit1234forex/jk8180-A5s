import os
import json

with open("set-mode/mode.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    mode = loads['mode']
    update = loads['update']
    print("MODE     =",mode)

if update == "1":
    os.popen('sh ~/jk8180-multi/move.sh')

if  mode == "1":
 with open("set-miner-on-multi/ccminer.json", "r", encoding='utf8') as file:
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

 with open("set-miner-name-cpu-all/name-cpu-all.json", "r", encoding='utf8') as file:
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
 with open("set-miner-on-multi/hansen33s-dero.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    wallet = loads['wallet']
    print("WALLET   =",wallet)
 WALLET=wallet

 with open("set-miner-name-cpu-all/name-cpu-all.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    name = loads['name']
    cpu = loads['cpu']
    print("NAME     =",name)
    print("CPU      =",cpu)
 NAME=name
 CPU=cpu
 os.system(f"cd miner && ./hansen33s-dero-miner-android-arm64 -wallet-address {WALLET} -worker-name {NAME} -turbo")

if  mode == "3":
 with open("set-miner-on-multi/xmrigcc.json", "r", encoding='utf8') as file:
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

 with open("set-miner-name-cpu-all/name-cpu-all.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    name = loads['name']
    cpu = loads['cpu']
    print("NAME     =",name)
    print("CPU      =",cpu)
 NAME=name
 CPU=cpu
 os.system(f"cd miner && ./xmrigDaemon -o {POOL} -a {ALGO} -u {WALLET}@{NAME} -p {PASSWORD} -k, --rig-id= {NAME} -t {CPU}")

if  mode == "4":
 with open("set-miner-on-multi/hansen33s-dero.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    wallet = loads['wallet']
    print("WALLET   =",wallet)
 WALLET=wallet

 with open("set-miner-name-cpu-all/name-cpu-all.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    name = loads['name']
    cpu = loads['cpu']
    print("NAME     =",name)
    print("CPU      =",cpu)
 NAME=name
 CPU=cpu
 os.system(f"cd miner && proot-distro login ubuntu")
