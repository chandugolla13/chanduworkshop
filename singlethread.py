import threading

class SingleThread():
    def main():
        print("starts @main")
        obj = SingleThread()
        obj.PrintNumbers()

        for y in range(1,101):
             print("y val: ",y)
             print("@ends")
             return




    def PrintNumbers(self):
         for x in range(1,101):
             print("x val: ",x)
             return

SingleThread.main()
