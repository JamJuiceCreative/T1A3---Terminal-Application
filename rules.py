def open_rules():    
    try:
        file = open("rules.txt", "r")
        print(file.read())
    finally:
        file.close
