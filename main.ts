let nombre_de_personne = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (nombre_de_personne < 21) {
        nombre_de_personne += 1
    } else {
        nombre_de_personne += 0
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    nombre_de_personne = 0
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    nombre_de_personne += -1
})
basic.forever(function on_forever() {
    
    basic.showNumber(nombre_de_personne)
    if (nombre_de_personne > 20) {
        nombre_de_personne = 20
        while (nombre_de_personne == 20) {
            basic.showLeds(`
                . . . . .
                                . # . # .
                                . . # . .
                                . # . # .
                                . . . . .
            `)
        }
    }
    
})
