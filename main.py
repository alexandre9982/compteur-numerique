nombre_de_personne = 0

def on_button_pressed_a():
    global nombre_de_personne
    if nombre_de_personne < 21:
        nombre_de_personne += 1
    else:
        nombre_de_personne += 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global nombre_de_personne
    nombre_de_personne = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global nombre_de_personne
    nombre_de_personne += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global nombre_de_personne
    basic.show_number(nombre_de_personne)
    if nombre_de_personne > 20:
        nombre_de_personne = 20
        while nombre_de_personne == 20:
            basic.show_leds("""
                . . . . .
                                . # . # .
                                . . # . .
                                . # . # .
                                . . . . .
            """)
basic.forever(on_forever)
