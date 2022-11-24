from genGraph import GraphGenerator

if __name__=="__main__":

    source = open("first-quantum.py", "r")
    code = source.read()
    generator= GraphGenerator(code, 'graph', 'png')
    generator.genCFG()
