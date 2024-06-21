meme_dict = {
            "RUNEAR": "Forma de correr de algun jugador en un juego",
            "XD": "Una cara que tiene el proposito de representar que la persona se esta muriendo de la risa.",
            "MEME": "Ilustracion digital hilarante con toques sarcásticos, irónicos y satíricos que reflejan claramente un contexto en el cual no se debe tomar en serio, ya que es solo una representacion de un chiste.",
            }
for i in range(5):
    word = input("Que palabra quieres entender?").upper()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Aun falta agregar elementos al diccionario")
