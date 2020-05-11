def resource(klass):
    def wrapper():
        print("Class wrap")
        print(klass)
        print("End class wrap")
    
    return wrapper