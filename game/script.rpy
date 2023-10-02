# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define a = Character("Aarón")

define n = Character(what_italic = True)
define j = Character("Joana")
define r = Character("Rachel")
define e = Character("Eileen")
define e = Character("Eileen")


transform toLeft:
    xalign 0.5 yalign 1.0
    linear 1 xalign 0.0
    
transform toRight:
    xalign 0.5 yalign 1.0
    linear 1 xalign 1.0

transform fadeOut:
    alpha 1.0
    linear 3 alpha 0.0
# El juego comienza aquí.

label start:

    scene bg room

    n "Suena la alarma y te despiertas."
    n "Sales de entre las sábanas y te diriges al baño."

    n "¿Qué ves?"

    show d_fem pose:
        toLeft
    show d_masc pose:
        toRight

    menu:
        "Chico":
            hide d_fem with dissolve
            python:
                gen = "d_masc"
            
        "Chica":
            hide d_masc with dissolve
            python:
                gen = "d_fem"

    n "Tienes lagunas después de haberte destruido a beber anoche y tienes que esforzarte por recordar tu nombre."

    python: 
        nombre = renpy.input("¿Cómo te llamabas?")
        nombre = nombre.strip() or "Noah"

    define d = Character( name = "[nombre]", image = "[gen]" )

    n "Terminas de lavarte la cara y procedes a desayunar, cuando de repente suena el teléfono."

    d "¿Sí? ¿Quién es?"

    a "Buenos días [nombre], ¿cómo vas?"

    d "Podría estar mejor, pero no puedo quejarme."

    a "Vas a estar mejor, te traigo buenas noticias: tengo un caso para ti."

    d "¿Qué? Pensaba que después del último iban a quitarme la placa..."

    a "Y así debería de haber sido, pero tengo buenos contactos."
    a "Ahora escucha:\nha muerto un chaval en una casa de campo a las afueras, posiblemente ahogado, pero la autopsia todavía está en proceso."
    a "Estamos completamente seguros de que el asesino es uno de las personas con las que residía ya que nadie se ha acercado a esa casa desde que ellos la alquilaron."
    a "Te he mandado por email toda la información disponible, ponte ya mismo a leer las fichas de los sospechosos y ve a la escena del crimen en cuanto estés listo."
    
    d "Muchas gracias, tío. Te debo una."

    a "Esto cuenta por bastante más que una, me estoy jugando el pellejo confiándote un caso después de que metieses la pata estrepitosamente con el anterior..."
    a "Pero bueno, hoy por ti, mañana por mí. Buena suerte."

    n "La llamada termina"
    n "Dejas el teléfono en la encimera, te preparas un café y te sientas delante del ordenador: efectivamente, ahí estaba el mensaje."
    n "Lo abres y encuentras cinco fichas, los cuatro sospechosos y la víctima, además de la ubicación de la escena del crimen."

    
    menu fichas:
        "Joana":
            n "lorem ipsum"
            jump fichas

        "Rachel":
            n "lorem ipsum"
            jump fichas

        "Eric":
            n "lorem ipsum"
            jump fichas

        "VICTIMA":
            n "lorem ipsum"
            jump fichas

        "PORRETA":
            n "lorem ipsum"
            jump fichas

        "Viajar a la escena del crimen":
            n "lorem ipsum definitivo"
            jump escenaDelCrimen
    
    menu escenaDelCrimen:
        "Interrogar a Joana":
            n "lorem ipsum"
            jump JoanaInt

        "Interrogar a Rachel":
            n "lorem ipsum"
            jump fichas

        "Interrogar a Eric":
            n "lorem ipsum"
            jump fichas

        "Interrogar a PORRETA":
            n "lorem ipsum"
            jump fichas

        "Viajar a la escena del crimen":
            n "lorem ipsum definitivo"

    menu JoanaInt:
        d "Buenos días, Joana. "
        "¿Dónde estabas tú la noche del asesinato?":
            j "Durmiendo"
        "¿Dónde estabas tú la noche del asesinato?":
            j "Durmiendo"
        "¿Dónde estabas tú la noche del asesinato?":
            j "Durmiendo"
        "¿Dónde estabas tú la noche del asesinato?":
            j "Durmiendo"
        "¿Dónde estabas tú la noche del asesinato?":
            j "Durmiendo"
        "Terminar":
            jump escenaDelCrimen

    return
