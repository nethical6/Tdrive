class text:
    def getArgs(cmd) -> list:
        args = str(cmd).split(" ")
        # delete the cmd from args
        print(args)
        args.pop(1) 
        return args