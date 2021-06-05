class A:
    def do_job(self, *args):
        print(args, "A")
        if len(args) > 1:
            if args[1] == 'f':
                print('I am walking ...')


class Z:
    def do_job(self, *args):
        if str(args[0]).isnumeric():
            print(args[0], "Z")
            print(f'I am counting from 1 to {args[0]}:  {list(range(1, args[0] + 1))}')
        else:
            print(args[1], "Z")
            print(f'I am counting from 1 to {args[1]}:  {list(range(1, args[1] + 1))}')


class B(A):
    def do_job(self, *args):
        print(*args, "B")
        A.do_job(self, *args)
        print(f'I am printing your string : "{args[0]}"')


class C(A, Z):
    def do_job(self, *args):
        print(*args, "C")
        Z.do_job(self, args[0])
        A.do_job(self)

        print('I am jumping ...')


class D(B):
    def do_job(self, *args):
        print(args[0], "D")
        B.do_job(self, *args)
        print('I am speaking ...')


class E(D, C):
    def do_job(self, *args):
        print(args, "E")
        C.do_job(self, args[1])
        D.do_job(self, args[0], "e")

        # super().do_job(args[0], args[1])
        print('I am laughing ...')


class F(Z, B):
    def do_job(self, *args):
        print(args[0], args[1], "F")
        B.do_job(self, args[0], "f")
        Z.do_job(self, args[1])

        print('I am playing ...')


obja = A()
obja.do_job()

print()
objz = Z()
objz.do_job(3)

print()
obje = E()
obje.do_job('Python', 5)

print()
objf = F()
objf.do_job('Python', 6)
