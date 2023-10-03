define a = Character("Aarón")
define n = Character(what_italic = True)

define j = Character("Joana")
define r = Character("Raquel")
define c = Character("Carlos")
define e = Character("Eric")


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

        "Raquel":
            n "lorem ipsum"
            jump fichas

        "Eric":
            n "lorem ipsum"
            jump fichas

        "Carlos":
            n "lorem ipsum"
            jump fichas

        "Lucas":
            n "lorem ipsum"
            jump fichas

        "Viajar a la escena del crimen":
            n "lorem ipsum definitivo"
            jump escenaDelCrimen

    return

# ----------------- Escena del crimen ------------------

menu escenaDelCrimen:
    "Interrogar a Joana":
        jump JoanaInt

    "Interrogar a Raquel":
        jump RaquelInt

    "Interrogar a Eric":
        jump EricInt

    "Interrogar a Carlos":
        jump CarlosInt

    "Cerrar el caso":
        n "lorem ipsum definitivo"
        jump acusaciones

# ----------------- ------ --- ------ ------------------

# ----------------- Escena del crimen ------------------

menu acusaciones:
    "Acusar a Joana":
        n "lorem ipsum"
        jump JoanaEnd

    "Acusar a Raquel":
        n "lorem ipsum"
        jump RaquelEnd

    "Acusar a Eric":
        n "lorem ipsum"
        jump EricEnd

    "Acusar a Carlos":
        jump CarlosEnd

    "Volver":
        n "lorem ipsum definitivo"

# ----------------- ------ --- ------ ------------------

# ----------------- Inte. Carlos -----------------


define carlosBranch1 = True
define carlosBranch2 = True
define carlosBranch3 = True

label CarlosInt:
    d "Buenos días, Carlos."
    d "¿Podrías decirme qué ocurrió anoche?"

    c "Yo no sé nada, ha sido Raquel quién lo ha encontrado muerto en la piscina."

    d "¿Estuviste presente cuando Raquel lo encontró?"

    c "No, yo estaba en mi habitación. Estaba dormido. Me despertó su grito."

    d "Y entonces acudiste a la cocina."

    c "Así es."

    menu CarlosIntMenu:
    
        "¿Cómo era tu relación con Lucas? ¿Os llevábais bien?" if carlosBranch1 == True:
            c "Era un buen amigo. Se llevaba bien con todos."
            c "Una pena su pérdida."

            d "Entiendo que él y Joana eran pareja. ¿Qué me podrías decir sobre eso?"

            c "Joana ha tenido varios problemas a lo largo de su vida:"
            c "perdió a su madre cuando tenía quince años y, al ser la mayor tuvo que cuidar de sus hermanos pequeños"
            c "Su padre entró en depresión tras el fallecimiento y ya nada fue igual en su casa"
            c "Está un poquillo loca, la verdad. No se qué hacían esos dos juntos."
            c "Ahora, ¿su relación? Casi no se nada de ella. Lucas apenas se abría y no me creo nada de lo que dice Joana"
            c "Creo que miente más que otra cosa" 
            
            menu CarlosQ1:
                "Conoces demasiado bien la vida de Joana...":
                    c "Nos llevábamos bien. Llegamos a estar bastante unidos"

                    d "¿Y ahora ya no?"

                    c "Las cosas han cambiado desde la muerte de su madre."
                    c "Ya nunca fue la misma."

                    d "¿Llegaste a tener sentimientos hacia ella?"
                    
                    c "No veo cómo ese dato es relevante al caso"

                    d "Todo es relevante"

                    c "No. No llegué a sentir nada por ella."

                "Casi no has hablado de Lucas...": 
                    c "No hay mucho de qué hablar. Era buena gente, un santo diría yo."
                    c "No todo el mundo sería capaz de soportar a Joana."
                    c "En resumidas cuentas: se llevaba bien con todo el mundo."
                    c "Nadie le haría daño a no ser que se la tuviesen bien guardada."

                    d "¿Qué insinuas?"

                    c "Como he dicho antes, Joana nunca fue igual desde la pérdida de su madre."
                    c "Su mente no funciona muy bien."
                    c "A veces cuenta cosas que no han pasado y nos intenta convencer de que sí."
                    c "Lo dicho, un poco loca..."

                    d "¿Crees que ella podría haber hecho algo así?"

                    c "Eh, yo no he dicho nada de eso. Pero descubrirlo es parte de tu trabajo. "
                    
            python:
                carlosBranch1 = False
            jump CarlosIntMenu

        "Cuéntame con todo lujo de detalles lo que ocurrió anoche." if carlosBranch2 == True:
            c "Pues a ver..."
            c "Estábamos jugando juegos de mesa y pasando un buen rato, cuando de repente Lucas se mosqueó por una tontería. Al rato fue Joana a hablar con él."
            c "No sabemos de qué hablaron pero se les escuchó discutor."
            c "Después Joana se unió al grupo, cosa que no entiendo, mientras que Lucas se quedó solo un rato más antes de decirnos que se iba a dormir."
            c "No se tú, pero yo resolvería los problemas con mi pareja antes de volver al grupo y hacer como si nada..."

            d "Continúa"

            c "Pues tampoco hay mucho más."
            c "Seguimos todos de charreta y pasándolo bien hasta que decidimos irnos a dormir."
            c "Bueno, y como dije antes, Lucas se fue a dormir antes que nosotros."
            c "Nadie le presionó ni hizo comentarios al respecto. Ya hablaría cuando estuviese preparado. "

            menu CarlosQ2:
                "¿Y todos os fuisteis a dormir en ese momento?":
                    c "Sí"

                    d "¿Escuchaste algo raro esa noche?"

                    c "No, tengo un sueño muy profundo."

                "Continúa, por favor":
                    c "Nos despedimos, nos dimos las buenas noches y cada uno se fue a su cuarto."

                    d "¿No ocurrió nada más?"

                    c "Que me despertó el grito de Raquel."
                     
            python:
                carlosBranch2  = False
            jump CarlosIntMenu

        "¿Sabes si alguien se llevaba mal con Lucas?" if carlosBranch3 == True:
            c "¿Te refieres a que si sé quiénl o ha podido matar?"
            c "Pues no, no lo sé. Lucas se llevaba bien con todos."
            c "No creo que nadie quisiera hacerle daño"

            d "¿Crees que ha podido ser un accidente?"

            c "¿Accidente o sucuidio?"

            d "¿Tenía motivos para suicidarse?"

            c "Ni idea."

        "Muchas gracias. Con esto es suficiente.":
            jump escenaDelCrimen
     
# ----------------- ----- ------ -----------------

# ----------------- Inte. Eric -----------------

label EricInt:
menu EricIntMenu:
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

# ----------------- ----- ---- -----------------

# ----------------- Inte. Raquel -----------------

define raquelBranch1 = True
define raquelBranch2 = True
define raquelBranch3 = True

label RaquelInt:
    r "Sniff sniff"

    d "¿Necesitas un pañuelo?"

    r "No, no hace falta... Tengo pro aquí uno. *llora* Lo siento..."

    d "No te preocupes."

    r "Es que... Esta mañana... yo... *llora* Nunca volveré a verle... *llora* está... se ha ido..."

    d "Mira... sé que esto es complicado, pero necesito que hacerte unas preguntas... Sé que no te apetece recordarlo todo, pero debes hacerlo por Lucas. Piensa que a él le gustaría que averiguásemos qué pasó realmente."

    r "Tiene razón..."

    d "No hace falta que me trates de usted, somos un equipo. Solo quiero saber la verdad y suponogo que tú también, ¿no?"

    r "Sí. Sí quiero. Lucaas no se merece esto. Hay que averiguar qué ocurrió, porque... cómo alguien le... haya matado... *llora*"

    d "Tranquila. Para eso estoy aquí. Para que se haga justicia. Si alguien hizo algo, lo descubriremos y pagará, ¿vale?"

    r "Sí... empecemos..."

    d "Perfecto"

    menu RaquelIntMenu: 
        "¿Qué ocurrió anoche?" if raquelBranch1:
            r "Vale... a ver que piense... Estuvimos mucho rato charlando en la mesa que hay en la entrada de la casa, en el patio."
            r "Luego se nos ocurrió juegar al juego de la botella y para ello nos fuimos al salón de la casa, allí gira bien la botella en el suelo."
            r "Si no hubiésemos jugado a ese juego..."

            d "Lo estás haciendo muy bien. Continúa, por favor."

            r "No sé si sabes qué juego es: se gira un aboterlla y a la persona a la que apunte le haces hacer una cosa, bueno, hay muchas versiones del juego, pero nosotros jugamos a verdad o reto."

            d "Entiendo."

            r "Eric giró la botella, que apuntó a Joana y ésta eligió reto."
            r "Y el tonto de Eirc le dijo que le diese un beso a Carlos, y Joana se lo dio."
            r "Fue un pico, nada más."

            menu RaquelQ1:
                "¿Cómo reaccionó Lucas?":
                    r "No le gustó. Obviamente, sabía que era un juego estúpido y que no significaba nada... *baja la mirada*"

                    d "¿Qué ocurre?"

                    r "Carlos y Joana estuvieron saliendo hace unos años. Al final se dieron cuenta de que no funcionaba y que sería mejor quedar como amigos. Pero Lucas seguía sin aceptar eso."
                    r "A día de hoy sigue... seguía... manteniendo un cierto recelo hacia Carlos."
                    r "Aún así, eran muy buenos amigos y sabía que Joana ya no sentía nada por él." 


                "¿Por qué Eric le pondría ese reto a Joana?":
                    r "Así es Eric. Yo creo que a veces no sabe ni lo que hace."
                    r "Seguramente ya ni se acordaba de que hubo algo entre Carlos y Joana y tan solo quisiera que Luis se picase un poco."

                "¿Qué le pareció ese reto a Joana? ¿Se quejó o algo?":
                    r "No. Se quedó seria, se levantó y lo cumplió. Después se volvió a su sitio, seguramente sin darle demasiada importancia, como hace con todo en esta vida."
            
            d "Entiendo, continúa"

            r "Pasó un rato y giramos la botella un par de veces más... hasta que Lucas se levantó y nos dijo que se iba a tomar el aire."

            d "¿Y seguisteis jugando todos?"

            r "Sí, pero al rato se levantó Joana y fue tras él."
            r "Yo creo que fue a asegurarse de que Lucas estaba bien."
            r "Tardaron bastante en volver y se escucharon gritos de una discusión."
            r "Al rato entró Joana a la habitación y se sentó de nuevo en su sitio con el resto. Parecía furiosa."
            r "Ella es del tipo de persona que no muestra mucho sus emociones, pero a pesar de todo eso se notaba que algo no había ido bien."
            r "Al resto nos dio miedo sacar el tema,p or lo que hicimos como si nada hubiese pasado. Charlamos un rato y seguimos jugando"

            d "¿Y qué pasó después?"

            r "Estuvimos algo de tiempo jugando y pasando el rato hasta que entró Lucas dicineod que se iba a dormir. Le dimos las buenas noches y subió."
            r "Parecía que estaba bien, pero algo cansado."

            d "¿Actuó de manera extraña?"

            r "No, en absoluto. Estaba tranquilo."

            d "¿Ocurrió algo más después de eso?"

            r "No, nos quedamos media horilla más... después cada uno subió a su cuarto a dormir. "
            
            python:
                raquelBranch1 = False
            jump RaquelIntMenu

        "Entiendo que fuiste tú quién encontró primero el cuerpo" if raquelBranch2:
            python:
                raquelBranch2 = False
            jump RaquelIntMenu

        "¿Cómo era Lucas?" if raquelBranch3:
            python:
                raquelBranch3 = False
            jump RaquelIntMenu

        "Muchas gracias por todo.":
            jump escenaDelCrimen



# ----------------- ----- ------ -----------------

# ----------------- Inte. Joana -----------------

label JoanaInt:
menu JoanaIntMenu:
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

# ----------------- ----- ----- -----------------
