def chords_converter():
    lines = []
    l=''
    print("A continuacion, pega el texto con los acordes que quieras convertir")
    print("Cuando hayas copiado todo y pulsado ENTER, escribe FIN y pulsa ENTER de nuevo, asi el programa terminara de imprimir los acordes traducidos")
    print("PEGA AQUI LOS ACORDES ")
    while l != 'FIN':
        l=input(" ")
        lines.append(l)

    #lines = [l for l in inpf]
    #inpf.close()
    lines = lines[:-1]
    final_lines=[]
    for l in lines:
        if l.count(" ")>len(l)/5:
            l = l.replace("A", "La")
            l = l.replace("B", "Si")
            l = l.replace("D", "Re")
            l = l.replace("C", "Do")
            l = l.replace("E", "Mi")
            l = l.replace("F", "Fa")
            l = l.replace("G", "Sol")
            final_lines.append(l)
        elif len(l) < 5 and ('A' in l or 'B' in l or 'C' in l or 'D' in l or 'E' in l or 'F' in l or 'G' in l):
            l = l.replace("A", "La")
            l = l.replace("B", "Si")
            l = l.replace("D", "Re")
            l = l.replace("C", "Do")
            l = l.replace("E", "Mi")
            l = l.replace("F", "Fa")
            l = l.replace("G", "Sol")
            final_lines.append(l)
        else:
            final_lines.append(l)

    for i in final_lines:
        print(i)

chords_converter()
