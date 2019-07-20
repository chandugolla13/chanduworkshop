class immutable:
    def main():
        
        s1 = "hello"
        s2 = "hiii"
        print("s1 id: " ,id(s1))
        print("s2 id: " , id(s2))
        s3 = s1 + "word"
        print("s1 id: " ,s3)
        print("s1 id: " ,id(s3))
        print("s1 id: ",id(s2))
    
immutable.main()
