class Indenter:
    counter=0
    def __enter__(self,):
        print("", end="")
        Indenter.counter=Indenter.counter+4
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("",end="")
        Indenter.counter=Indenter.counter-4
        pass

    def print(self, str):
        print((Indenter.counter-4)*" "+str)



with Indenter() as indent:
    indent.print('hi!') 
    with indent:
        indent.print('talk is cheap') 
        with indent:
            indent.print('show me the code ') 
    indent.print('Torvalds')




# output is :

"""
hi!
	talk is cheap
		show me the code 
Torvalds



"""
