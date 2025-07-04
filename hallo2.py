Frage =False
a=0
List = [] 
NochEine = False
Fehler = False


while Fehler == False:
    while Frage == False:

        a += 1            
        try:
            Zahl1=int(input("Zahl" + str(a) + ": "))
        except:
            print("Fehlerhafte Zahl die Angabe wird als ungültig gewertet.")
            break
        
          
            
        item = Zahl1
        List.append(item)

        while NochEine == False:
            Frage1=str(input("Noch eine?: "))
            if Frage1 =="nein" + "Nein":
                Frage = True
                NochEine = True
                
            elif Frage1 == "ja" + "Ja":
                Frage = False 
                NochEine = True
                
            else:
                print("Gib bitte eine Gültige antwort ein! (Ja, Nein)")
                NochEine = False
              
        NochEine = False
       
        
        

        if len(List) <= 1:
            print("Du benotigst mindestens 2 Zahlen um eine Rechnung durchzuführen!")
            NochEine = False
            Frage = False
            Eingabe = False 
            
        else:
            Fehler = True
            
    

    
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