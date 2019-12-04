from inspect import signature

def helper(info = '(No info provided)'):
    def should_help(func):
        def pythia_func(*args, **kwargs):
            if args[0] == "__help__":
                return info
            elif args[0] == "__params__":
                return signature(func).parameters
            else:
                return func(*args, **kwargs)
        return pythia_func
    return should_help