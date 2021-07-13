word = ""
started = False
while word.lower() != "quit":
 word = input('> ')
 if word.lower()=="start":
     if started:
         print("car is already started")
     else:
         started = True
         print("car started..ready to go")
 elif word.lower() =="stop":
     if not started:
         print("car already stopped")
     else:
          started= False
          print("car stopped")
 elif word.lower() == "help":
  print('''start - to start the car'
     stop - to stop the car'
     quit - to exit''')
 elif word !="quit":
    print("I can't understand")