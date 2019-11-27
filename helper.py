def helper(info = 'No info provided.'):
    def should_help(func):
        def get_info(*args, **kwargs):
            if args[0] == "__help__":
                return info
            else:
                return func(*args, **kwargs)
        return get_info
    return should_help