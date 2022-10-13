from tkinter import *
from PIL import Image, ImageTk
from main import algoritmo, init, reconstruirCamino
from Librerias import aux_ret

paradas = []
Estaciones = [
    "Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky", "Beresteiska",
    "Shuliavska", "Politekhnichnyl instytut", "Vokzalna", "Universytet",
    "Teatralna", "Khreschchatyk", "Arsenalna", "Dnipro", "Hidropark",
    "Livoberezhna", "Darnytsia", "Chernihivska", "Lisova", "Heroiv Dnipra",
    "Minska", "Obolon", "Petrivka", "Tarasa Shevchenka", "Kontraktova ploshcha",
    "Poshtova ploshcha", "Maidan Nezalezhnosti", "Ploshcha Lva Tolstoho",
    "Olimpiiska", "Palats Ukrania", "Lybidska", "Demiivska", "Holosiivska",
    "Vasylkivska", "Vystavkovyi tsentr", "Ipodrom", "Teremky", "Syrets",
    "Dorohozhychi", "Lukianivska", "Zoloti vorota", "Palats sportu", "Klovska",
    "Pecherska", "Dryzhby narodiv", "Vyduychi", "Slavutych", "Osokorky",
    "Pozniaky", "Kharkivska", "Vyrlytsia", "Boryspilska", "Chervonyi khutir"
]

nombre_paradas = {110: "Akademmistechko", 111: "Zhytomyrska", 112: "Sviatoshyn", 113: "Nyvky", 114: "Beresteiska",
                  115: "Shuliavska", 116: "Politekhnichnyl instytut", 117: "Vokzalna", 118: "Universytet",
                  119: "Teatralna", 120: "Khreschchatyk", 121: "Arsenalna", 122: "Dnipro", 123: "Hidropark",
                  124: "Livoberezhna", 125: "Darnytsia", 126: "Chernihivska", 127: "Lisova", 210: "Heroiv Dnipra",
                  211: "Minska", 212: "Obolon", 213: "Petrivka", 214: "Tarasa Shevchenka", 215: "Kontraktova ploshcha",
                  216: "Poshtova ploshcha", 217: "Maidan Nezalezhnosti", 218: "Ploshcha Lva Tolstoho",
                  219: "Olimpiiska", 220: "Palats Ukrania", 221: "Lybidska", 222: "Demiivska", 223: "Holosiivska",
                  224: "Vasylkivska", 225: "Vystavkovyi tsentr", 226: "Ipodrom", 227: "Teremky", 310: "Syrets",
                  311: "Dorohozhychi", 312: "Lukianivska", 314: "Zoloti vorota", 315: "Palats sportu", 316: "Klovska",
                  317: "Pecherska", 318: "Dryzhby narodiv", 319: "Vyduychi", 321: "Slavutych", 322: "Osokorky",
                  323: "Pozniaky", 324: "Kharkivska", 325: "Vyrlytsia", 326: "Boryspilska", 327: "Chervonyi khutir"}

pos_paradas = {110: (22, 252), 111: (22, 287), 112: (22, 318), 113: (22, 362), 114: (65, 362),
               115: (105, 362), 116: (147, 362), 117: (188, 362), 118: (229, 362),
               119: (265, 327), 120: (327, 312), 121: (376, 312), 122: (434, 312), 123: (482, 298),
               124: (521, 268), 125: (558, 239), 126: (588, 215), 127: (618, 191), 210: (327, 48),
               211: (327, 84), 212: (327, 119), 213: (327, 152), 214: (327, 188), 215: (327, 222),
               216: (327, 256), 217: (327, 288), 218: (327, 376),
               219: (327, 424), 220: (327, 474), 221: (327, 520), 222: (327, 569), 223: (288, 605),
               224: (220, 605), 225: (165, 605), 226: (117, 605), 227: (66, 605), 310: (155, 154),
               311: (187, 203), 312: (215, 249), 314: (252, 305), 315: (353, 375), 316: (376, 389),
               317: (396, 417), 318: (417, 445), 319: (439, 475), 321: (461, 507), 322: (483, 537),
               323: (501, 562), 324: (519, 587), 325: (549, 604), 326: (579, 606), 327: (608, 606)
               }

ventana = Tk()
ventana.title("Metro de Kiev")
ventana.iconbitmap("kiev-metro.ico")
ventana.geometry("1200x900")
ventana.resizable(0, 0)
MARCO = 50
COLOR_FONDO = "#fff8e7"
ventana.config(bd=int(MARCO))
ventana.config(bg=COLOR_FONDO, relief="groove")
inicio = Frame(ventana)
inicio.pack(side=TOP, anchor=NW)
inicio.config(relief="groove", bg=COLOR_FONDO)

varOrigen = StringVar(ventana)
varOrigen.set("Seleccione una parada")

varDestino = StringVar(ventana)
varDestino.set("Seleccione una parada")
aux = aux_ret()

def busqueda():
    if (punto_inicio == "" or punto_final == ""):
        return
    global canvas_foto, paradas
    canvas_foto.delete("trayecto")
    textoInfoItinerario.configure(text="")
    prove = list(nombre_paradas.values())
    init(prove.index(varDestino.get()), paradas)
    algoritmo(prove.index(varOrigen.get()), prove.index(varDestino.get()), paradas)
    # aux = aux_ret()
    paradas = reconstruirCamino(prove.index(varDestino.get()), paradas, aux, -1)
    itinerario()
    paradas = []


punto_inicio = ""

def inic(*args):
    global punto_inicio, paradas
    canvas_foto.delete("trayecto")
    textoInfoItinerario.configure(text="")
    numero = list(nombre_paradas.keys())[list(nombre_paradas.values()).index(varOrigen.get())]
    if punto_inicio != "":
        canvas_foto.delete(punto_inicio)
    punto_inicio = canvas_foto.create_oval(pos_paradas.get(numero)[0] - 10, pos_paradas.get(numero)[1] + 10,
                                           pos_paradas.get(numero)[0] + 10, pos_paradas.get(numero)[1] - 10,
                                           fill="green")

punto_final = ""

def fin(*args):
    global punto_final
    canvas_foto.delete("trayecto")
    textoInfoItinerario.configure(text="")
    numero = list(nombre_paradas.keys())[list(nombre_paradas.values()).index(varDestino.get())]
    if punto_final != "":
        canvas_foto.delete(punto_final)
    punto_final = canvas_foto.create_oval(pos_paradas.get(numero)[0] - 10, pos_paradas.get(numero)[1] + 10,
                                          pos_paradas.get(numero)[0] + 10, pos_paradas.get(numero)[1] - 10, fill="red")

Estaciones.sort()
origen = OptionMenu(inicio, varOrigen, *Estaciones, command=inic)
origen.config(cursor="trek", bg="#eae6ca", width=25, height=1)
origen.grid(row=0, column=1, padx=5, pady=10)
destino = OptionMenu(inicio, varDestino, *Estaciones, command=fin)
destino.config(cursor="trek", bg="#eae6ca", width=25, height=1)
destino.grid(row=1, column=1, padx=5)
origenLabel = Label(inicio, text="Origen:", bg=COLOR_FONDO, font=("Helvetica", 12, "bold"), padx=40)
origenLabel.grid(row=0, column=0, pady=25)
destinoLabel = Label(inicio, text="Destino:", bg=COLOR_FONDO, font=("Helvetica", 12, "bold"), padx=40)
destinoLabel.grid(row=1, column=0)
canvas_foto = Canvas(ventana, width=653, height=673)
canvas_foto.pack(side="right", padx=20, pady=20)
foto = ImageTk.PhotoImage(Image.open("kiev-metro.jpg"))
canvas_foto.create_image(653, 653, image=foto, anchor=SE)

Label(inicio, text="\t\t\t\t\t              ", bg=COLOR_FONDO).grid(row=1, column=2)

boton_buscar = Button(inicio, command=busqueda, text="Buscar", height=2, width=10, bg="#eae6ca", cursor="trek",
                      font=("Helvetica", 13, "bold"), padx=50)
boton_buscar.grid(row=1, column=3, padx=5, pady=3)


frameInfoItinerario = Frame()
frameInfoItinerario.pack(anchor="w", side="bottom", padx=20, pady=20)
frameInfoItinerario.config(bg="#fffacd")
frameInfoItinerario.pack_propagate(0)
textoInfoItinerario = Label(frameInfoItinerario)
textoInfoItinerario.config(text="", bg="#fffacd", relief="groove", height=41, width=50, anchor="nw")
textoInfoItinerario.grid(row=0, column=0, sticky="w")
textoInfoItinerario.grid_propagate(0)

def itinerario():
    linea_parada1 = 0
    linea_parada2 = 0
    transbordos = 0
    global paradas, strListaParadas, aux
    paradas = paradas.split("-")
    strListaParadas = "\n\tRECORRIDO:\n \n"
    parada_1 = int(paradas[0])  # parada actual
    parada_2 = int(paradas[1])  # parada posterior
    linea_parada1 = int(parada_1/100)
    linea_parada2 = int(parada_2/100)
    if linea_parada1 != linea_parada2: transbordos += 1
    if not es_linea_curva(parada_1, parada_2):
        canvas_foto.create_line(pos_paradas.get(parada_1)[0], pos_paradas.get(parada_1)[1],
                                pos_paradas.get(parada_2)[0], pos_paradas.get(parada_2)[1],
                                fill="yellow", width=4, tags="trayecto")
    canvas_foto.create_oval(pos_paradas.get(parada_1)[0] - 10, pos_paradas.get(parada_1)[1] + 10,
                            pos_paradas.get(parada_1)[0] + 10, pos_paradas.get(parada_1)[1] - 10,
                            fill="green", tags="trayecto")
    strListaParadas = strListaParadas + f"\t{parada_1}. {nombre_paradas.get(parada_1)}\n"
    for i in range(1, len(paradas) - 1):
        parada_1 = int(paradas[i])  # parada actual
        parada_2 = int(paradas[i + 1])  # parada posterior
        linea_parada1 = int(parada_1 / 100)
        linea_parada2 = int(parada_2 / 100)
        if linea_parada1 != linea_parada2: transbordos += 1
        if not es_linea_curva(parada_1, parada_2):
            canvas_foto.create_line(pos_paradas.get(parada_1)[0], pos_paradas.get(parada_1)[1],
                                    pos_paradas.get(parada_2)[0], pos_paradas.get(parada_2)[1],
                                    fill="yellow", width=4, tags="trayecto")
        canvas_foto.create_oval(pos_paradas.get(parada_1)[0] - 10, pos_paradas.get(parada_1)[1] + 10,
                                pos_paradas.get(parada_1)[0] + 10, pos_paradas.get(parada_1)[1] - 10,
                                fill="yellow", tags="trayecto")
        strListaParadas = strListaParadas + f"\t{parada_1}. {nombre_paradas.get(parada_1)}\n"
    canvas_foto.create_oval(pos_paradas.get(parada_2)[0] - 10, pos_paradas.get(parada_2)[1] + 10,
                            pos_paradas.get(parada_2)[0] + 10, pos_paradas.get(parada_2)[1] - 10, fill="red",
                            tags="trayecto")
    strListaParadas = strListaParadas + f"\t{paradas[len(paradas)-1]}. {nombre_paradas.get(parada_2)}\n"
    strTexto = f"{strListaParadas}\n\n\tPARADAS:\t{len(paradas)-1}\n\tTRANSBORDOS:\t{int(transbordos)}"
    textoInfoItinerario.config(text=strTexto, font=("Helvetica", 14), justify="left")
    return


def es_linea_curva(parada_1, parada_2):
    linea_curva = False

    nodo_1 = 118
    nodo_2 = 119
    if parada_1 == nodo_1 and parada_2 == nodo_2 or parada_1 == nodo_2 and parada_2 == nodo_1:
        canvas_foto.create_line(pos_paradas.get(nodo_1)[0], pos_paradas.get(nodo_1)[1], 242, 360,
                                pos_paradas.get(nodo_2)[0], pos_paradas.get(nodo_2)[1],
                                fill="yellow", width=4, tags="trayecto")
        linea_curva = True

    nodo_1 = 119
    nodo_2 = 120
    if parada_1 == nodo_1 and parada_2 == nodo_2 or parada_1 == nodo_2 and parada_2 == nodo_1:
        canvas_foto.create_line(pos_paradas.get(nodo_1)[0], pos_paradas.get(nodo_1)[1], 273, 312,
                                pos_paradas.get(nodo_2)[0], pos_paradas.get(nodo_2)[1],
                                fill="yellow", width=4, tags="trayecto")
        linea_curva = True

    nodo_1 = 122
    nodo_2 = 123
    if parada_1 == nodo_1 and parada_2 == nodo_2 or parada_1 == nodo_2 and parada_2 == nodo_1:
        canvas_foto.create_line(pos_paradas.get(nodo_1)[0], pos_paradas.get(nodo_1)[1], 462, 312,
                                pos_paradas.get(nodo_2)[0], pos_paradas.get(nodo_2)[1],
                                fill="yellow", width=4, tags="trayecto")
        linea_curva = True

    nodo_1 = 314
    nodo_2 = 315
    if parada_1 == nodo_1 and parada_2 == nodo_2 or parada_1 == nodo_2 and parada_2 == nodo_1:
        canvas_foto.create_line(pos_paradas.get(nodo_1)[0], pos_paradas.get(nodo_1)[1], 295, 375,
                                pos_paradas.get(nodo_2)[0], pos_paradas.get(nodo_2)[1],
                                fill="yellow", width=4, tags="trayecto")
        linea_curva = True

    nodo_1 = 315
    nodo_2 = 316
    if parada_1 == nodo_1 and parada_2 == nodo_2 or parada_1 == nodo_2 and parada_2 == nodo_1:
        canvas_foto.create_line(pos_paradas.get(nodo_1)[0], pos_paradas.get(nodo_1)[1], 365, 375,
                                pos_paradas.get(nodo_2)[0], pos_paradas.get(nodo_2)[1],
                                fill="yellow", width=4, tags="trayecto")
        linea_curva = True

    nodo_1 = 324
    nodo_2 = 325
    if parada_1 == nodo_1 and parada_2 == nodo_2 or parada_1 == nodo_2 and parada_2 == nodo_1:
        canvas_foto.create_line(pos_paradas.get(nodo_1)[0], pos_paradas.get(nodo_1)[1], 536, 604,
                                pos_paradas.get(nodo_2)[0], pos_paradas.get(nodo_2)[1],
                                fill="yellow", width=4, tags="trayecto")
        linea_curva = True

    return linea_curva


ventana.mainloop()