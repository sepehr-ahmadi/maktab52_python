class BackupOpen:
    def __init__(self, file):
        self.file = file

    def __str__(self):
        return self.f.read()

    def __enter__(self):
        self.f = open(self.file)

    def __exit__(self, exc, value, traceback):
        if not exc:
            return True
        else:
            self.f.close()
        return True


with BackupOpen("text.txt"):
    pass
