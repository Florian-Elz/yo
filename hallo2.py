Frage =False
a=0
List = [] 

while Frage == False:
    
    a += 1 
    Zahl1=int(input("Zahl" + str(a) + ": "))
    
    
    item = Zahl1
    List.append(item)
    
    Frage1=str(input("noch eine?: "))
    
    if Frage1 =="nein":
        Frage = True
        
    else:
        Frage = False    
     
print(List)
Rechenzeichen=input("Addieren? (+), Subtrahieren? (-), Multiplizieren? (*), Dividieren? (/), : ")
Ergebnis=0
if Rechenzeichen=="+":
  
    for x in List:
        Ergebnis += x 
if Rechenzeichen=="-":
    for x in List:
        Ergebnis -= x 
if Rechenzeichen=="*":
    Ergebnis = 1
    for x in List:
        Ergebnis *= x 
if Rechenzeichen=="/":
    Ergebnis = List[0]
    for x in List[1:]:
        Ergebnis /= x 


    
print("Das Ergebnis ist:", Ergebnis)