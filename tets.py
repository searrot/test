import daemon, random

def main():
    
    for i in range(1000):
        res = random.randint(0, 1000)
        print(1/res)
        return 1/res

with daemon.DaemonContext():
    main()