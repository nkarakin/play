# Berechne Summe der Elemente ohne die Bereiche, die mit 6 beginnen und 7 enden. 
# Jeder Bereich, der mit 6 anfängt wird mit einer 7 abgeschlossen.
# Beispiel, wo y fuer "Schreiben" und n fuer "nicht Schreiben" steht:
#  y y y y y|n n n n n n|y y y y|n n|n n n|y
# [0,0,2,4,5,6,6,6,0,4,7,8,7,7,5,6,7,6,8,7,7] 

a = [0,0,2,4,5,6,6,6,0,4,7,8,7,7,5,6,7,6,8,7,7]
flag = "schreiben"
flag_7 = "flag_is_master"
a_s = []
for element in a:
    if element == 6:
        flag = "nicht_schreiben"
    elif element == 7 and flag == "nicht_schreiben":
        flag = "schreiben"
        flag_7 = "7_nicht_schreiben"
    else:
        pass
 
    if element == 7 and flag_7 == "7_nicht_schreiben":
        a_s.append(0)
        flag_7 = "flag_is_master"
    elif element == 7 and flag_7 == "flag_is_master":
        a_s.append(element)
    elif element != 7 and flag == "schreiben":
        a_s.append(element)
    else:
        a_s.append(0)
print(a)        
print(a_s, sum(a_s))

     

