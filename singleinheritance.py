class parent():
    def m1(self):
        print("parent...1")
        
        return
    def m2(self):
        print("parent...2")
        
        return
    def m3(self):
        print("parent...3")
        
        return

class child(parent):
    def m1(self):
        print("child....1")
        return
    def m2(self):
        print("child....2")
        return
    def m3(self):
        print("child....3")
        return

class grandson(child):
    def m1(self):
        print("grandchild....1")
        return
    def m2(self):
        print("grandchild....2")
        return
    def m3(self):
        print("grandchild....3")
        return


class superson(grandson):
    def m1():
        print("superchild....1")
        return
    def m2():
        print("superchild....2")
        return
    def m3():
        print("superchild....3")
        return

    

class SingleInheritance():
    def main():
        c = child()
        c.m1()
        c.m2()
        c.m3()
        p = parent()
        p.m1()
        p.m2()
        p.m3()
        g = grandson()
        g.m1()
        g.m2()
        g.m3()
        superson.m1()
        superson.m2()
        superson.m3()
        
SingleInheritance.main()

