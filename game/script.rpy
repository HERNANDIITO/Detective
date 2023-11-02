# Personajes

define a = Character("Aarón", color="#ece256")
define n = Character(what_italic = True)

define j = Character("Joana",  color="#8a21bb")
define r = Character("Raquel", color="#df4ad7")
define c = Character("Carlos", color="#b33d2d")
define e = Character("Eric",   color="#2ebb21")

python:
    renpy.play("menu_click.wav")

# Branches

# --- Carlos ---

define carlosBranch0 = True
define carlosBranch1 = True
define carlosBranch2 = True
define carlosBranch3 = True
define carlosBranch4 = False
define carlosBranch5 = False
define carlosBranch6 = False

define carlosBranch5AlreadyFound = False

# --- Eric ---

define ericBranch0 = True
define ericBranch1 = True
define ericBranch2 = False
define ericBranch3 = False
define ericBranch4 = False

# --- Raquel ---

define raquelBranch0 = True
define raquelBranch1 = True
define raquelBranch2 = True
define raquelBranch3 = True
define raquelBranch4 = True

# --- Joana ---

define joanaBranch0 = True
define joanaBranch1 = True
define joanaBranch2 = True
define joanaBranch3 = True
define joanaBranch4 = False
define joanaBranch5 = False
define joanaBranch6 = False

# Animaciones

transform toLeft:
    xalign 0.5 yalign 1.0
    linear 1 xalign 0.0
    
transform toRight:
    xalign 0.5 yalign 1.0
    linear 1 xalign 1.0

transform fromLeft:
    xalign -1.0 yalign 1.0
    linear 1 xalign 0.0

transform fromBottom:
    xalign 0.0 yalign 2.0
    linear 1 yalign 1.0

transform fromCenterBottom:
    xalign 0.5 yalign 2.0
    linear 1 yalign 0.5

transform toBottom:
    xalign 0.0 yalign 1.0
    linear 1 yalign 2.0

transform fadeOut:
    alpha 1.0
    linear 3 alpha 0.0

# Main loop

label start:

    show black with dissolve

    show text "Recomendamos papel y boli para tomar nota a lo largo de la aventura."
    pause 10 
    hide text

    scene black
    stop music fadeout 1.0
    play sound "alarm.wav" fadein 1.0

    n "Suena la alarma y te despiertas."
    n "Sales de entre las sábanas y te diriges al baño."

    play music "house.wav" volume 0.025 loop

    scene bg bath with dissolve


    show d_fem flipped:
        toLeft
    show d_masc pose:
        toRight
    n "¿Qué ves reflejado en el espejo?"

    menu:
        "Chico":
            hide d_fem with dissolve
            python:
                gen = "d_masc"
            
        "Chica":
            hide d_masc with dissolve
            hide d_fem with dissolve
            show d_fem pose:
                toRight
            python:
                gen = "d_fem"

    n "Tienes lagunas después de haberte destruido a beber anoche y tienes que esforzarte por recordar tu nombre."

    python: 
        nombre = renpy.input("¿Cómo te llamabas?")
        nombre = nombre.strip() or "Noah"

    define d = Character( name = "[nombre]", image = "[gen]", who_xpos=9.0)

    play sound "tap.wav" volume 0.25
    pause 3.0
    n "Terminas de lavarte la cara y te vas a desayunar."
    play sound "footsteps_1.wav" volume 0.25
    pause 1.0

    show bg kitchen with dissolve

    show phone neutral:
        fromBottom
    
    # stop music fadeout 1.0
    # play music "music/llamada.mp3" fadein 1.0 loop

    play sound "incoming_call.wav" volume 0.25

    n "De pronto, suena el móvil."

    d "¿Sí? ¿Quién es?"

    a "Buenos días [nombre], ¿cómo vas?"

    d "Podría estar mejor, pero no puedo quejarme."

    a "Vas a estar mejor, te traigo buenas noticias: tengo un caso para ti."

    d "¿Qué? Pensaba que después del último caso iban a quitarme la placa..."

    a "Y así debería haber sido, pero tengo buenos contactos."
    a "Ahora escucha: ha muerto un chaval en una casa de campo a las afueras, posiblemente ahogado, pero la autopsia todavía está en proceso." 
    
    a "Estamos completamente seguros de que el asesino es una de las personas con las que residía ya que nadie se ha acercado a esa casa desde que ellos la alquilaron." 
    a "Sabemos que quien ha encontrado el cadáver se llama Raquel."
    a "Te he mandado por email toda la información disponible, ponte ya mismo a leer las fichas de los sospechosos y ve a la escena del crimen en cuanto hayas terminado."
    
    d "Muchas gracias. Te debo una."

    a "Esto cuenta por bastante más que una, me estoy jugando el pellejo confiándote un caso después de que metieses la pata estrepitosamente con el anterior..."
    a "Pero bueno, hoy por ti, mañana por mí. Buena suerte."

    n "La llamada termina."
    hide phone with dissolve

    # stop music fadeout 1.0
    # play music "music/menu.mp3" fadein 1.0 loop

    play sound "footsteps_1.wav" volume 0.25
    show bg office with dissolve
    n "Dejas el teléfono en la encimera, te preparas un café y te sientas delante del ordenador: efectivamente, ahí estaba el mensaje."
    n "Lo abres y encuentras cinco fichas, los cuatro sospechosos y la víctima, además de la ubicación de la escena del crimen."
    
    menu fichas:
        "Joana":
            play sound "file.wav"
            show file joana:
                fromCenterBottom

            python:
                renpy.pause(delay=None, modal=True)

            hide file with dissolve
            jump fichas

        "Raquel":
            play sound "file.wav"
            show file raquel:
                fromCenterBottom
            
            python:
                renpy.pause(delay=None, modal=True)

            hide file with dissolve
            jump fichas

        "Eric":
            play sound "file.wav"
            show file eric:
                fromCenterBottom
            
            python:
                renpy.pause(delay=None, modal=True)

            hide file with dissolve
            jump fichas

        "Carlos":
            play sound "file.wav"
            show file carlos:
                fromCenterBottom
            
            python:
                renpy.pause(delay=None, modal=True)

            hide file with dissolve
            jump fichas

        "Lucas (víctima)":
            play sound "file.wav"
            show file lucas:
                fromCenterBottom
            
            python:
                renpy.pause(delay=None, modal=True)

            hide file with dissolve
            jump fichase

        "Viajar a la escena del crimen":
            play sound "crime_scene.wav"
            pause 2
            stop sound fadeout 1.0
            show bg raquel with dissolve
            jump escenaDelCrimen

    return

# ----------------- Escena del crimen ------------------
label escenaDelCrimen:
    stop music fadeout 1.0
    play music "crime_house.wav" volume 0.025 fadein 1.0 loop
    menu escenaDelCrimenMenu:

        "Interrogar a Carlos":
            show bg carlos with dissolve
            play sound "footsteps_1.wav" volume 0.25
            jump CarlosInt

        "Interrogar a Joana":
            show bg joana with dissolve
            play sound "footsteps_1.wav" volume 0.25
            jump JoanaInt

        "Interrogar a Raquel":
            show bg raquel with dissolve
            play sound "footsteps_1.wav" volume 0.25
            jump RaquelInt

        "Interrogar a Eric":
            show bg eric with dissolve
            play sound "footsteps_1.wav" volume 0.25
            jump EricInt

        "Cerrar el caso":
            jump acusaciones

# ----------------- ------ --- ------ ------------------

# ----------------- Escena del crimen ------------------
label acusaciones:
    # stop music fadeout 1.0
    # play music "music/acusando.mp3" fadein 1.0 loop
    menu acusacionesMenu:

        "Acusar a Carlos":
            jump CarlosEnd

        "Acusar a Joana":
            jump JoanaEnd

        "Acusar a Raquel":
            jump RaquelEnd

        "Acusar a Eric":
            jump EricEnd

        "Volver":
            jump escenaDelCrimen

# ----------------- ------ --- ------ ------------------

# ----------------- Inte. Carlos -----------------

label CarlosInt:

    # stop music fadeout 1.0
    # play music "music/carlos.mp3" fadein 1.0 loop
    show carlos neutral:
        fromLeft

    if (carlosBranch0):
        d "Buenos días, Carlos."
        d "¿Podrías decirme qué ocurrió anoche?"

        c "Yo no sé nada, ha sido Raquel quién lo ha encontrado muerto en la piscina."

        d "¿Estuviste presente cuando Raquel lo encontró?"

        c "No, yo estaba en mi habitación. Estaba dormido. Me despertó su grito."

        d "Y entonces acudiste a la cocina."

        c "Así es."

        python:
            carlosBranch0 = False

    menu CarlosIntMenu:
    
        "¿Cómo era tu relación con Lucas? ¿Os llevábais bien?" if carlosBranch1:
            c "Era un buen amigo. Se llevaba bien con todos."
            c "Una pena su pérdida."

            d "Entiendo que él y Joana eran pareja. ¿Qué me podrías decir sobre eso?"

            c "Joana ha tenido varios problemas a lo largo de su vida: perdió a su madre cuando tenía quince años y, al ser la mayor, tuvo que cuidar de sus hermanos pequeños."
            c "Su padre entró en depresión tras el fallecimiento y ya nada fue igual en su casa."
            c "Está un poquillo loca, la verdad... No sé qué hacían esos dos juntos... Ahora, ¿su relación? Casi no sé nada de ella. Lucas apenas se abría y no me creo nada de lo que dice Joana. Creo que miente más que otra cosa."
            
            menu:
                "Conoces demasiado bien la vida de Joana...":
                    c "Nos llevábamos bien. Llegamos a estar bastante unidos."

                    d "¿Y ahora ya no?"

                    c "Las cosas han cambiado desde la muerte de su madre. Ya nunca fue la misma."

                    d "¿Llegaste a sentir algo por ella?"
                    
                    c "No veo cómo ese dato es relevante al caso."

                    d "Todo es relevante."

                    c "No. No llegué a sentir nada por ella."

                "Casi no has hablado de Lucas...": 
                    c "No hay mucho de qué hablar. Era buena gente, se llevaba bien con todo el mundo."
                    c "Nadie le haría daño a no ser que se la tuviesen bien guardada."

                    d "¿Qué insinuas?"

                    c "Como he dicho antes, Joana nunca fue igual desde la pérdida de su madre. Su mente no funciona muy bien: a veces cuenta cosas que no han pasado y nos intenta convencer de que sí."

                    d "¿Crees que podría haberle matado ella?"

                    c "Eh, yo no he dicho nada de eso. Descubrirlo es parte de tu trabajo. "
                    
            python:
                carlosBranch1 = False
            jump CarlosIntMenu

        "Cuéntame con todo lujo de detalles lo que ocurrió anoche." if carlosBranch2:
            c "Pues a ver..."
            c "Estábamos jugando juegos de mesa y pasando un buen rato, cuando de repente Lucas se mosqueó por una tontería. Al rato fue Joana a hablar con él."
            c "No sabemos de qué hablaron pero se les oyó discutir."
            c "Después, Joana se unió al grupo, cosa que no entiendo, mientras que Lucas se quedó solo un rato más antes de decirnos que se iba a dormir."

            d "Continúa."

            c "Pues tampoco hay mucho más. Seguimos todos hablando y pasándolo bien hasta que decidimos irnos a dormir."

            menu CarlosQ2:
                "¿Y os fuisteis todos a dormir en ese momento?":
                    c "Sí."

                    d "¿Escuchaste algo raro esa noche?"

                    c "No, tengo un sueño muy profundo."

                "Continúa, por favor":
                    c "Nos despedimos, nos dimos las buenas noches y cada uno se fue a su cuarto."

                    d "¿No ocurrió nada más?"

                    c "Que me despertó el grito de Raquel."
                     
            python:
                carlosBranch2  = False
            jump CarlosIntMenu

        "¿Sabes si alguien se llevaba mal con Lucas?" if carlosBranch3:
            c "¿Te refieres a que si sé quién lo ha podido matar?"
            c "Pues no, no lo sé. Lucas se llevaba bien con todos. No creo que nadie quisiera hacerle daño."

            d "¿Crees que ha podido ser un accidente?"

            c "¿Accidente o sucuidio?"

            d "¿Tenía motivos para suicidarse?"

            c "Ni idea."
            python:
                carlosBranch3  = False
            jump CarlosIntMenu

        "¿Por qué se molestó Lucas mientras jugábais?" if carlosBranch4:
            c "Nada, una tontería. Como bien has dicho: sólo estábamos jugando."

            d "¿Seguro que no hubo un beso involucrado que pudiese molestar a nuestra víctima?"

            c "¿Un beso?"
            c "Ojalá. Ni si quiera se le puede llamar un beso a eso. Un reto que puso el subnormal de Eric. Un reto que seguramente haya olvidado porque seguro que va completamente fumado."

            python:
                carlosBranch4  = False
            jump CarlosIntMenu

        "¿Llegaste a tener algún vínculo romántico con Joana?" if (carlosBranch5 and (not carlosBranch1) and (not carlosBranch2) and (not carlosBranch3)):
            c "¿Quién te ha dicho eso?"
            show carlos angry at left
            c "Vaya panda de mentirosos que tengo por amigos."

            d "¿Entonces lo niegas?"

            c "Claro que sí. Jamás hubo ni habrá nada entra esa loca y yo."
            python:
                carlosBranch5  = False
            jump CarlosIntMenu

        "Me he enterado de que Joana y tú estuvisteis saliendo. ¿Por qué has mentido?" if (carlosBranch5 and (not carlosBranch1) and (not carlosBranch2) and (not carlosBranch3)):
            c "Fue hace unos años. Nunca funcionó."
            python:
                carlosBranch5  = False
            jump CarlosIntMenu

        "¿Estuviste en la piscina por la noche?" if (carlosBranch6 and (not carlosBranch1) and (not carlosBranch2) and (not carlosBranch3)):
            c "¿En la piscina?"
            c "Pero si yo me fui a dormir a la misma hora que todos. ¿Por qué me quedaría yo solo en la piscina? ¿Crees que soy yo el asesino?"

            d "Alguien te escuchó hablar con Lucas por la noche."
            d "En la piscina."

            c "..."

            d "Habla."

            c "Me desperté en mitad de la noche... No me podía dormir y me cansé de dar vueltas en la cama, por lo que salí al porche a tomar el aire y al rato apareció Lucas."

            menu:
                "Por favor, continúa.":
                    c "Sí... voy..."

                "Termina la historia. Dudo que quedase ahí":
                    show carlos angry at left
                    c "Voy, voy..."
            
            show carlos neutral at left
            c "Pues le pregunté si estaba todo bien. Me comentó que había discutido con su querida novia y que además no podía dormir por lo que había salido a dar un paseo."
            c "Yo, como buen mejor amigo, me ofrecí a acompañarle."

            d "¿Sobre qué hora ocurrió esto?"

            c "Sobre la una y media... ¿Dos quizás?"

            d "Está bien, continúa."

            c "Dimos una vuelta a la parcela, estuvimos hablando simplemente. Nada relevante, hablar por hablar. A la vuelta nos sentamos en el borde de la piscina a seguir hablando."


            d "¿Ocurrió algo en la piscina?"

            c "Pfff..."
            c "Nos enfadamos. Mejor dicho: se enfadó."
            c "Y eso me enfadó a mí."
            c "¿Por qué le cuesta tanto escuchar al chaval?"
            show carlos angry at left
            c "A veces me saca de quicio."

            d "Sí, pero qué pasó."

            c "Lo empujé a la piscina."

            d "Ya veo..."

            c "No. No murió ahí. Salió de la piscina, yo lo vi."
            c "Eric también."
            show carlos neutral at left

            d "¿Eric?"

            c "Sí. Llegó justo cuando lo empujé a la piscina y lo ayudó a secarse y después se fueron a no sé dónde."

            d "¿Y tú qué hiciste después?"

            c "Me fui a dar un paseo. Estaba cabreadísimo, pero cuando volví se me había pasado y me fui directo a la cama."

            d "¿Cuándo llegaste a casa después de tu paseo?"

            c "A las 4:03 AM. Esto sí que lo se bien. Lo vi en el despertador justo antes de dormirme."
            python:
                carlosBranch6  = False
                ericBranch2 = True
            jump CarlosIntMenu

        "¿Viste a Lucas durante la noche?" if (carlosBranch6 and (not carlosBranch1) and (not carlosBranch2) and (not carlosBranch3)):
            c "¿Por qué me preguntas esto? ¿En serio crees que he sido yo? ¿Su mejor amigo?"
 
            show carlos angry at left
            c "Pff... llévame preso si tan seguro estás."

            d "Tengo información que te hace el principal sospechoso ahora mismo."

            c "Pues sí. Sí que lo vi. No podía dormir anoche, por lo que salí a tomar el aire y al rato apareció él."

            d "¿Sobre qué hora fue esto?"

            c "Yo qué sé."
            c "Lo único de lo que estoy seguro es de que yo ya estaba en la cama a las cuatro."
            show carlos neutral at left

            d "¿Puedo saber de qué hablásteis?"
            
            c "De la vida."
            c "Nos pusimos al día. Hacía bastante que no nos veíamos."

            d "¿Y en ningún momento pasásteis por la piscina?"

            c "Qué va. Hacía frío a esas horas. No sé cómo acabó muerto allí. Pero por mi culpa no fue."
           
            python:
                carlosBranch6 = False
                ericBranch3 = True
            jump CarlosIntMenu
            
        "Muchas gracias. Con esto es suficiente.":
            hide carlos with dissolve
            jump escenaDelCrimen
     
# ----------------- ----- ------ -----------------

# ----------------- Inte. Eric -----------------

label EricInt:

    # stop music fadeout 1.0
    # play music "music/eric.mp3" fadein 1.0 loop
    show eric sleeping:
        fromLeft

    if ericBranch0:
        d "Buenos días. ¿Eric verdad?"

        e "Aaaaagh..."

        d "Me gustaría hacerte unas preguntas."

        e "Hhmmm..."

        d "Veo que esto va a ser difícil..."
        
        python:
            ericBranch0 = False

    menu EricIntMenu:
        "¿Eric?" if ericBranch1:
            e "Aargh... "
            e "Cuidado Lucas... Te vas a caer..."
            d "¿Qué has dicho?"
            e "Déjame en paz..."
            python:
                ericBranch1 = False
            jump EricIntMenu

        "¿Estás mejor?" if (ericBranch2 and (not ericBranch1)):
            e "Sí... Más o menos..."
            show eric high

            d "¿Estuviste anoche en la piscina?"

            e "Hmm... sí... estaban Carlos y Lucas peleando..."

            d "¿Qué ocurrió?"

            e "Hmm..."

            show eric sleeping

            menu:
                "¿Qué pasó en la piscina, Eric? ":
                    e "Aaargh..."
                
                "Eric, concéntrate, tú puedes.":

                    e "Hmmm..."
                
            show eric high
            e "Se estaban gritando... y los separé..."
            show eric sleeping

            menu:
                "Esto es importante, necesito detalles, por favor.":
                    show eric high
                    e "¿Por qué es importante...? ¿Tú quién eres...?"
                
                "Espabila, Eric, no tenemos todo el día.":
                    show eric high
                    e "Voy... voy..."
                
            
            e "Los separé... y me fui con Lucas... a la azotea..."
            e "Conseguí que se fumase uno, hehehe"
            e "Nunca lo había visto tan contento..."

            show eric sleeping

            menu:
                "¿Lo drogaste?":
                    show eric high
                    e "Hehehe... solo un poco... nada que pudiese matarlo..."
                
                "¿Y qué pasó después?":
                    show eric high
                    e "Aaargh... no me acuerdo..."
            

            d "Eric, dame un segundo."

            e "Si..."
            show eric sleeping
            hide eric with dissolve
            show phone neutral:
                fromBottom

            play sound "phone_call.mp3"
            n "Haces una llamada a la Agencia"
            pause 20
            stop sound fadeout 1.0

            a "¿Sí?"

            d "Aarón, soy yo, [nombre]."
            d "Necesito la información de la autopsia."

            a "Tenemos pocos datos, de momento."
            a "Parece ser que tiene un par de costillas rotas y que terminó de morir ahogado."
            a "No sé cómo acabaría así el chiquillo pero tuvo que sufrir cosa mala."

            d "¿Se han encontrado restos de estupefacientes en la sangre?"
            d "Marihuana, concretamente."

            a "Justo. Perdona. No sé cómo he pasado eso por alto."

            d "Perfecto. Muchas gracias."

            n "Terminas la llamada."

            hide phone with dissolve

            show eric high:
                fromLeft

            python:
                ericBranch2 = False
                ericBranch4 = True
            jump EricIntMenu
        
        "¿Podemos hablar un momento?" if (ericBranch3 and (not ericBranch1)):
            e "Sí... Más o menos..."
            show eric high

            d "¿Ocurrió algo anoche?"

            e "Hmm... No lo sé... Oí a gente discutir..."
            
            d "¿Te acuerdas de quienes eran?"

            e "Agh..."
            show eric sleeping
           
            menu:
                "Esto es importante, necesito detalles, por favor.":
                    show eric high
                    e "¿Por qué es importante...? ¿Tú quién eres...?"
                
                "Espabila, Eric, no tenemos todo el día":
                    show eric high
                    e "Voy... voy..."

            e "Eran Carlos y Lucas... se estaban gritando en la piscina..."
            e "Para variar... hehehe"

            d "¿Qué ocurrió?"

            e "Hmm... No lo sé... No me acuerdo..."

            d "¿Pasó algo más después de eso?"

            e "Eh... me cogí una botella...hehehe..."

            d "¿Fuiste a la cocina a por ella?"

            e "Sí... ahora que lo recuerdo... ocurrió algo más..."

            d "¿Qué fue?"

            e "Me pareció ver entrar a Carlos... Entró a la casa... mientras yo asaltaba la bodega... hehehe..."
            e "Me escondí... no me vió..."
            e "Y menos mal... sino me hubiese llevado a rastras a mi cuarto..."

            show eric sleeping

            python:
                ericBranch3 = False
            jump EricIntMenu

        "¿Dónde estuvisteis Lucas y tú fumando?" if (ericBranch4 and (not ericBranch1)):
            show eric high
            e "Hmmm..."
            e "Aaargh..."
            e "A la azotea, mirando cómo un mapache bebía de la piscina, creo..."

            menu:
                "¿Supiste algo más de Carlos en toda la noche?":
                    e "Hmmm..."
                    e "No..."
                
                "¿Qué hiciste después?":
                    e "¿Después de que se fuera Lucas...?"
            
            d "¿Cuándo se fue Lucas?"

            e "A mitad de tronco."
            e "Ni se lo terminó el desagradecido... Con lo que le estaba gustando..."

            d "¿A dónde se fue Lucas?"

            e "No lo sé. Con su novia, seguramente..."

            d "¿Y tú qué hiciste después?"

            e "Beber... Necesitaba beber... me lo pedía el cuerpo..."
            show eric sleeping
            
            python:
                ericBranch4 = False
            jump EricIntMenu

        "Terminar.":
            hide eric with dissolve
            jump escenaDelCrimen

# ----------------- ----- ---- -----------------

# ----------------- Inte. Raquel -----------------

label RaquelInt:

    # stop music fadeout 1.0
    # play music "music/raquel.mp3" fadein 1.0 loop
    show raquel neutral:
        fromLeft

    if ( raquelBranch0 ):
        r "Sniff sniff"

        d "¿Necesitas un pañuelo?"

        r "No, no hace falta... Tengo por aquí uno. Lo siento..."

        d "No te preocupes."

        show raquel sad
        r "Es que... Esta mañana... yo... Nunca volveré a verle... está... se ha ido..."

        d "Mira... sé que esto es complicado, pero necesito hacerte unas preguntas... Sé que no te apetece recordarlo todo, pero debes hacerlo por Lucas. Piensa que a él le gustaría que averiguásemos qué pasó realmente."

        r "Tiene razón..."

        d "No hace falta que me trates de usted, somos un equipo. Solo quiero saber la verdad y suponogo que tú también, ¿no?"

        r "Sí. Sí quiero. Lucas no se merece esto. Hay que averiguar qué ocurrió, porque... cómo alguien le... haya matado..."
        show raquel neutral

        d "Tranquila. Para eso estoy aquí. Para que se haga justicia. Si alguien hizo algo, lo descubriremos y pagará, ¿vale?"

        r "Sí... empecemos..."

        d "Perfecto."

        python:
            raquelBranch0 = False

    menu RaquelIntMenu: 
        "¿Qué ocurrió anoche?" if raquelBranch1:
            r "Vale... a ver que piense... Estuvimos mucho rato charlando en la mesa que hay en la entrada de la casa, en el patio. Luego se nos ocurrió juegar al juego de la botella y para ello nos fuimos al salón de la casa."
            r "Si no hubiésemos jugado a ese juego..."

            show raquel sad

            d "Lo estás haciendo muy bien. Continúa, por favor."

            show raquel neutral

            r "No sé si sabes qué juego es: se gira una botella y a la persona a la que apunte le haces hacer una cosa. Nosotros jugamos a verdad o reto."

            d "Entiendo."

            r "Eric giró la botella, que apuntó a Joana y ésta eligió reto. El tonto de Eric le dijo que le diese un beso a Carlos, y Joana se lo dio. Fue un pico, nada más."

            menu RaquelQ1:
                "¿Cómo reaccionó Lucas?":
                    r "No le gustó."
                    show raquel sad

                    d "¿Qué ocurre?"

                    r "Carlos y Joana estuvieron saliendo hace unos años. Al final no funcionó y decidieron quedar como amigos, pero Lucas seguía sin aceptar eso. A día de hoy sigue... seguía... manteniendo un cierto recelo hacia Carlos."
                   
                    show raquel neutral

                    python:
                        if carlosBranch5AlreadyFound == False:
                            carlosBranch5 = True
                            carlosBranch5AlreadyFound = True

                        joanaBranch5 = True


                "¿Por qué Eric le pondría ese reto a Joana?":
                    r "Así es Eric. Yo creo que a veces no sabe ni lo que hace. Seguramente ya ni se acordaba de que hubo algo entre Carlos y Joana."

                "¿Qué le pareció ese reto a Joana? ¿Se quejó o algo?":
                    r "No. Se quedó seria, se levantó y lo cumplió. Después se volvió a su sitio, seguramente sin darle demasiada importancia, como hace con todo en esta vida."
            
            d "Entiendo, continúa."

            r "Giramos la botella un par de veces más... hasta que Lucas se levantó y nos dijo que se iba a tomar el aire."

            d "¿Y seguisteis jugando todos?"

            r "Sí, pero al rato se levantó Joana y fue tras él. Yo creo que fue a asegurarse de que Lucas estaba bien. Tardaron bastante en volver y se llegaron a oir gritos de una discusión."

            show raquel sad
            r "Luego entró Joana a la habitación. Se sentó de nuevo en su sitio y no dijo nada. Al nosotros nos dio miedo sacar el tema, por lo que hicimos como si nada hubiese pasado. Charlamos un rato y seguimos jugando."

            d "¿Y qué pasó después?"

            show raquel neutral

            r "Pasado el rato entró Lucas diciendo que se iba a dormir. Le dimos las buenas noches y subió a su cuarto."

            d "¿Actuó de manera extraña?"

            r "No, en absoluto. Estaba tranquilo."

            d "¿Ocurrió algo más después de eso?"

            r "No, nos quedamos un poco más y después cada uno subió a su cuarto a dormir. "
            
            python:
                raquelBranch1 = False
                carlosBranch4 = True
                joanaBranch4 = True
            jump RaquelIntMenu

        "Entiendo que fuiste tú quién encontró primero el cuerpo." if raquelBranch2:
            r "Sí..."

            d "¿Ocurrió algo antes de que lo encontrases?"

            r "Por la noche... me despertaron... al principio eran murmullos... luego pude distinguir las voces..."

            d "¿Qué ocurre, Raquel? ¿De quién eran las voces?"

            r "De Carlos y Lucas... Estaban en la piscina, parecía que estaban discutiendo..."
            r "Carlos parecía muy alterado... También oí agua... Creo que alguien se cayó a la piscina..."

            d "¿Crees que Carlos podría hacer algo así?"

            r "No lo sé... Él... él nunca haría nada así... Es verdad que a veces se enfada y grita mucho, pero nos quiere a todos..."

            d "Tranquilízate. Respira..."

            r "Lo siento."

            d "No pasa nada. Ahora procede. ¿Qué oíste?"

            r "A Carlos y Lucas. Estaban en la piscina, no sé qué decían pero por el tono de voz sé que Carlos estaba enfadado."

            menu RaquelQ2:
                "¿Hiciste algo? ¿Te acercaste a ellos?":
                    show raquel sad
                    r "No... me seguí durmiendo... En su momento no le di importancia, ¿sabe? Pensé que simplemente estarían jugando..."

                "¿Esto se lo has contado a alguien más?":
                    r "No... Nadie más lo sabe... O por lo menos yo no lo he contado..."

            d "¿Sobre qué hora fue esto?"

            r "No lo recuerdo... Sería sobre la una, una y pico..."

            show raquel neutral

            d "Muy bien."

            python: 
                raquelBranch2 = False
                carlosBranch6 = True
                joanaBranch6 = True
            jump RaquelIntMenu

        "¿Cómo era Lucas?" if raquelBranch3:
            r "Muy buena gente."
            show raquel sad
            r "Se llevaba bien con todos. Era un chico educado... Todavía no me creo que le haya pasado esto a él..."
        
            show raquel neutral
            python:
                raquelBranch3 = False
            jump RaquelIntMenu

        "¿Ocurrió algo esta mañana?" if raquelBranch4:
            r "Fui a la cocina a por algo para comer... Saqué algo de la despensa, me preparé un café y cuando fui a sentarme en la mesa, vi un cuerpo flotando boca abajo en la piscina... Enseguida lo reconocí..."

            show raquel sad

            d "Me estás ayudando mucho, continúa, por favor."

            r "Abrí el ventanal y me acerqué... estaba pálido..."

            d "Y fue ahí cuándo gritaste, ¿no?"

            r "Sí..." 
            show raquel neutral
            python:
                raquelBranch4 = False
            jump RaquelIntMenu

        "Muchas gracias por todo.":
            hide raquel with dissolve
            jump escenaDelCrimen

# ----------------- ----- ------ -----------------

# ----------------- Inte. Joana -----------------

label JoanaInt:

    # stop music fadeout 1.0
    # play music "music/joana.mp3" fadein 1.0 loop
    show joana neutral:
        fromLeft

    if joanaBranch0:

        d "Buenos días. ¿Estás preparada para hablar de lo de anoche?"

        show joana sad

        j "Ha sido por mi culpa... Nada de esto hubiese ocurrido si yo no..."

        d "¿Qué pasó?"

        j "Hice algo que no debería haber hecho... Pero tampoco esperaba que fuese a molestarle tanto a Lucas... Era solo un juego..."

        d "¿Jugásteis a un juego?"

        j "Sí... hemos jugado ya varias veces y es realmente una tontería..." 

        d "Continúa."
        
        j "Me tocó darle un beso a Carlos..."
       
        show joana neutral

        d "Entiendo."

        show joana angry

        j "El caso es que tampoco tendría que habérselo tomado tan mal Lucas, no era para tanto. ¿Qué iba a hacer yo? Hice lo que tenía que hacer y punto."

        show joana neutral
        python:
            joanaBranch0 = False

    menu JoanaIntMenu:
        "Entonces, ¿Lucas y tú erais pareja?" if joanaBranch1:
            show joana sad
            j "Por favor, no hables de él en pasado..."

            d "Lo siento."

            j "Da igual..."
            show joana neutral
            j "Lucas y yo llevábamos un año juntos."

            python:
                joanaBranch1 = False
            jump JoanaIntMenu

        "¿Crees que Lucas pudo haberse suicidado por el beso?" if joanaBranch2:
            j "Creo que sí... si no, ¿qué otra cosa podría ser?\nEs todo por mi culpa..."
            show joana sad

            d "Es importante que entiendas que nosotros no somos responsables de las emociones de los demás. Cuando te pusieron el reto, ¿llegaste a pensar que le podría molestar a Lucas?"

            j "..."
            j "No..."
            j "Creía que todo estaba bien entre Carlos y Lucas... Juraría que eran incluso mejores amigos..."
            show joana neutral

            python:
                joanaBranch2 = False
            jump JoanaIntMenu

        "¿Qué ocurrió después de ese reto?" if joanaBranch3:
            j "Al rato Lucas salió fuera a tomar el aire. Le di un poco de tiempo y después salí a verle."

            d "Y ¿cómo estaba?"

            j "Sentado en el porche, tranquilo."

            d "Continúa."

            j "Me senté a su lado y le dije lo que ya sabía: que le quería mucho y que no se preocupase por la tontería esa."

            d "¿Y qué dijo?"

            j "No mucho..."

            python:
                joanaBranch3 = False
            jump JoanaIntMenu

        "Tengo entendido que Lucas y tú discutisteis en el porche. ¿Es eso cierto?" if (joanaBranch4 and (not joanaBranch1) and (not joanaBranch2) and (not joanaBranch3)):
            show joana sad
            j "S... sí..."
            j "La verdad es que acabé levantando un poco la voz..."

            show joana angry
            j "Creo que tendría que haberme quedado dentro y dejar que otro saliese a buscarle... Solo empeoré las cosas..."
            show joana neutral

            python:
                joanaBranch4 = False
            jump JoanaIntMenu

        "¿Carlos y tú fuisteis pareja?" if (joanaBranch5 and (not joanaBranch1) and (not joanaBranch2) and (not joanaBranch3)):
            j "Supongo que te lo habrá contado alguien... Sí, estuvimos juntos unos meses y me arrepiento, nunca llegó a funcionar."
            
            d "¿Cuándo ocurrió todo esto?"

            j "Un par de años antes se salir con Lucas."

            d "¿Lucas sabía todo esto?"

            j "Claro."

            show joana neutral

            python:
                if carlosBranch5AlreadyFound == False:
                    carlosBranch5 = True
                    carlosBranch5AlreadyFound = True
                joanaBranch5 = False
            jump JoanaIntMenu

        "¿Crees que Carlos podría estar involucrado en el presunto asesinato?" if (joanaBranch6 and (not joanaBranch1) and (not joanaBranch2) and (not joanaBranch3)):
            j "¿Carlos?"

            d "Sí."

            j "¿Crees que Carlos lo ha matado?"

            d "¿Se te ocurre algún motivo que lo pudiese empujar a hacerlo?"

            j "No, la verdad es que no."

            d "¿Y no oíste nada por la noche?"

            j "No..."

            menu joanaQ6:
                "¿Seguro?":
                    j "Bueno..."

                    d "¿Qué ocurre?"
                    j "Se me ocurrió que quizás sería buena idea que Carlos hablase con Lucas... así que... fui a la habitación de Carlos a buscarlo... pero no estaba."
                    
                    d "Continúa, por favor."

                    j "Al volver a mi habitación oí a Eric y Lucas riéndose. Estaban en la azotea."

                    d "¿Sabrías decirme sobre qué hora les oíste?"

                    j "Sobre las tres, creo."

                    d "¿Y qué hiciste?"

                    j "Nada. Me fui a mi cuarto y me dormí."

                "Me da la sensación de que ocultas algo...":
                    j "No. En absoluto. Simplemente estoy cansada."

            python:
                joanaBranch6 = False
            jump JoanaIntMenu

        "Terminar.":
            hide joana with dissolve
            jump escenaDelCrimen

# ----------------- ----- ----- -----------------

label JoanaEnd:
    show black with dissolve

    show text "Dos semanas más tarde..."
    pause 2 
    hide text
    hide black

    stop music fadeout 1.0
    play music "house.wav" volume 0.025 loop

    show bg office with dissolve
    pause 5
    show phone neutral:
        fromBottom
    
    play sound "incoming_call.wav" volume 0.25
    pause 1.0
    n "Estás revisando las facturas cuando de repente comienza a sonar el móvil..."
    stop sound fadeout 1.0

    a "Me acaban de llegar los resultados del juicio."

    d "Y... ¿bien?"

    a "Te di una oportunidad y la has desperdiciado..."
    a "Sinceramente... creo que hasta aquí llega nuestra colaboración..."

    d "..."

    a "¿Cómo narices se te pasó por la cabeza que podría ser Joana?"
    a "¿En qué estabas pensando?"

    d "..."

    a "Era imposible de atacar en el juicio, ¡si es que no ha hecho nada!"
    a "Sinceramente, no pienso volver a llamarte para pedirte que resuelvas nada. Has terminado complicándolo todo mucho más."

    n "Cuelga la llamada abruptamente."

    show black with dissolve
    pause 10

    return

label EricEnd:
    show black with dissolve

    show text "Dos semanas más tarde..."
    pause 2 
    hide text
    hide black

    stop music fadeout 1.0
    play music "house.wav" volume 0.025 loop

    show bg office with dissolve
    pause 5
    show phone neutral:
        fromBottom
    
    play sound "incoming_call.wav" volume 0.25
    pause 1.0
    n "Estás revisando las facturas cuando de repente comienza a sonar el móvil..."
    stop sound fadeout 1.0
    
    a "Tú, [nombre], el juicio ha ido viento en popa. Ese rufián yonki va a pasar un merecido tiempo entre rejas."
    a "Y a ti te llamarán próximamente para ponerte al cargo de un caso nuevo. Enhorabuena."

    d "Bueno, seguramente tampoco fue algo hecho a conciencia, espero que se haya tenido en cuenta..."

    a "Así es, se ha tenido en cuenta, pero el consumo abusivo de drogas no lo ha dejado muy bien parado."

    d "Pobre chaval..."

    a "Sí, pero hoy estamos de celebración: acabas de remontar tu carrera como detective..."
    a "...y todo gracias a mí o sea que cuelgo ya mismo y me invitas a unas copas."

    n "Cuelga la llamada de manera rempentina."

    show black with dissolve
    pause 10

    return
    
label CarlosEnd:
    show black with dissolve

    show text "Dos semanas más tarde..."
    pause 2 
    hide text
    hide black

    stop music fadeout 1.0
    play music "house.wav" volume 0.025 loop

    show bg office with dissolve
    pause 5
    show phone neutral:
        fromBottom

    play sound "incoming_call.wav" volume 0.25
    pause 1.0
    n "Estás revisando las facturas cuando de repente comienza a sonar el móvil..."
    stop sound fadeout 1.0
    
    a "Me acaban de llegar los resultados del juicio, han declarado a Carlos culpable."

    d "Ufff, qué alegría, no te haces a la idea de lo tenso que estaba."

    a "Ya… pues el tema es que he estado leyendo y revisando tu investigación y no me cuadra en absoluto…"
    a "Creo que se han llevado al pobre chaval por sus antecedentes más que por este caso… Un poco injusto, la verdad."

    d "..."

    a "En fin, supongo que te volverán a llamar, aunque por un precio que no sé si ha valido la pena pagar: un chavalín que es muy probable que no haya hecho nada va a pasarse los mejores años de la vida pudriéndose en una celda…"
    a "Espero que por lo menos tuviese algo de culpa."

    n "Cuelga abruptamente."
    
    show black with dissolve
    pause 10

    return

label RaquelEnd:
    show black with dissolve

    show text "Dos semanas más tarde..."
    pause 2 
    hide text
    hide black

    stop music fadeout 1.0
    play music "house.wav" volume 0.025 loop

    show bg office with dissolve
    pause 5
    show phone neutral:
        fromBottom

    play sound "incoming_call.wav" volume 0.25
    pause 1.0
    n "Estás revisando las facturas cuando de repente comienza a sonar el móvil..."
    stop sound fadeout 1.0

    a "Me acaban de llegar los resultados del juicio."

    d "Y... ¿bien?"

    a "Te di una oportunidad y la has desperdiciado..."
    a "Sinceramente... creo que hasta aquí llega nuestra colaboración..."

    d "..."

    a "¿Cómo narices se te pasó por la cabeza que podría ser Raquel?"
    a "¿En qué estabas pensando?"

    d "..."

    a "Era imposbiles de atacar en el juicio, ¡si es que no ha hecho nada!"
    a "Sinceramente, no pienso volver a llamarte para pedirte que resuelvas nada. Has terminado complicándolo todo mucho más."

    n "Cuelga la llamada abruptamente."

    show black with dissolve
    pause 10

    return