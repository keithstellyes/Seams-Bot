#etcetra.py

___name___ = "etcetra"

def pythonEvaluator(args):
    ___name___ = "pythonEvaluator"
    if args[0].lower() == "return":
        return eval(args[1])
    if args[0].lower() == "none":
        exec(args[1])
