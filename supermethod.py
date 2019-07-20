class parent():
    def fun(self):
        print("parent fun...")
        return

class child(parent):
    def fun(self):
        print("child fun...")
        return
    
    def access(self):
        self.fun
        super().fun()
        return
    
    def main():
        obj = child()
        obj.access()

child.main()
