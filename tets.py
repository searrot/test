import daemon, random, getpass
getpass.getuser()
def main():
    res = random.randint(0, 1000)
    print(1/res)
    return 1/res

with daemon.DaemonContext():
    main()