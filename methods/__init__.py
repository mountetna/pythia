def get_modules():
    from os.path import dirname, basename, isfile, join
    import glob
    import importlib
    
    return [importlib.import_module("methods.%s" % basename(f)[:-3])
            for f in glob.glob(join(dirname(__file__), "*.py"))
            if isfile(f) and basename(f) != "__init__.py"]

def get_functions():
    from os.path import dirname, basename, isfile, join
    import glob
    import importlib
  
    return dict([[f, getattr(module, f)] 
            for module in get_modules()
            for f in [obj for obj in dir(module)
                      if getattr(getattr(module, obj), "__name__", None) is "pythia_func"]])
    
#MODULES = get_modules()
FUNCTIONS = get_functions()