# Personajes

define a = Character("Aarón")
define n = Character(what_italic = True)

define j = Character("Joana")
define r = Character("Raquel")
define c = Character("Carlos")
define e = Character("Eric")

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

transform fadeOut:
    alpha 1.0
    linear 3 alpha 0.0

# Main loop

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

label CarlosInt:

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

            c "Joana ha tenido varios problemas a lo largo de su vida:"
            c "perdió a su madre cuando tenía quince años y, al ser la mayor tuvo que cuidar de sus hermanos pequeños"
            c "Su padre entró en depresión tras el fallecimiento y ya nada fue igual en su casa"
            c "Está un poquillo loca, la verdad. No se qué hacían esos dos juntos."
            c "Ahora, ¿su relación? Casi no se nada de ella. Lucas apenas se abría y no me creo nada de lo que dice Joana"
            c "Creo que miente más que otra cosa" 
            
            menu:
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

        "Cuéntame con todo lujo de detalles lo que ocurrió anoche." if carlosBranch2:
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

        "¿Sabes si alguien se llevaba mal con Lucas?" if carlosBranch3:
            c "¿Te refieres a que si sé quiénl o ha podido matar?"
            c "Pues no, no lo sé. Lucas se llevaba bien con todos."
            c "No creo que nadie quisiera hacerle daño"

            d "¿Crees que ha podido ser un accidente?"

            c "¿Accidente o sucuidio?"

            d "¿Tenía motivos para suicidarse?"

            c "Ni idea."
            python:
                carlosBranch3  = False
            jump CarlosIntMenu

        "¿Por qué se molestó Lucas mientras jugábais?" if carlosBranch4:
            c "Nada, una tontería. Como bien has dicho: sólo estábamos jugando."

            d "¿Seguro que no hubo un beso involucrado?"
            d "¿Uno que pudiese molestar a nuestra víctima?"

            c "¿Un beso?"
            c "Ojalá. Ni si quiera se le puede llamar un beso a eso."
            c "Un reto que puso el subnormal de Eric"
            c "Un reto que seguramente haya olvidado porque seguro que va completamente fumado."
            python:
                carlosBranch4  = False
            jump CarlosIntMenu

        "¿Llegaste a tener algún vínculo romántico con Joana?" if carlosBranch5:
            c "¿Quién te ha dicho eso?"
            c "Vaya panda de mentirosos que tengo por amigos, joder."

            d "¿Entonces lo niegas?"

            c "Claro que sí. Jamás hubo ni habrá nada entra esa loca y yo."
            python:
                carlosBranch5  = False
            jump CarlosIntMenu

        "Me he enterado de que Joana y tú estuvisteis saliendo. ¿Por qué has mentido?" if carlosBranch5:
            c "Fue hace unos años. Nunca funcionó."
            python:
                carlosBranch5  = False
            jump CarlosIntMenu

        "¿Estuviste en la piscina por la noche?" if carlosBranch6:
            c "¿En la piscina?"
            c "Pero si yo me fui a dormir a la misma hora que todos."
            c "¿Por qué me quedaría yo solo en la piscina?"
            c "¿Crees que soy yo el asesino?"
            c "¿Crees que asesinaría yo a alguien?"
            c "¿A mi mejor amigo?"

            d "Alguien te escuchó hablar con Lucas por la noche."
            d "En la piscina."

            c "Joder."

            d "Habla."

            c "Me desperté en mitad de la noche..."
            c "No me podía dormir y me cansé de dar vueltas en la cama, por lo que salí al porche a tomar el aire."
            c "Y al rato apareció Lucas."

            menu:
                "Por favor, continúa.":
                    c "Sí... voy..."

                "Termina la historia. Dudo que quedase ahí":
                    c "Voy, voy... Joder, cómo estamos..."
            
            c "Pues le pregunté si estaba todo bien."
            c "Me comentó que había discutido con su querida novia y que además no podía dormir por lo que había salido a dar un paseo."
            c "Yo, como buen mejor amigo, me ofercí a acompañarle."

            d "¿Sobre qué hora ocurrió esto?"

            c "Sobre la una y media... ¿Dos quizás?"

            d "Está bien, continúa."

            c "Dimos una vuelta a la parcela, estuvimos hablando simplemente. Nada relevante, hablar por hablar."
            c "A la vuelta nos sentamos en el borde de la piscina a seguir hablando."

            d "¿Ocurrió algo en la piscina?"

            c "Pfff..."
            c "Nos enfadamos. Mejor dicho: se enfadó."
            c "Y eso me enfadó a mí."
            c "¿Por qué le cuesta tanto escuchar al chaval?"
            c "A veces me saca de quicio."

            d "Sí, pero qué pasó."

            c "Lo empujé a la piscina."

            d "Ya veo..."

            c "No. No murió ahí. Salió de la piscina, yo lo vi."
            c "Eric también."

            d "¿Eric?"

            c "Sí. Llegó justo cuando lo empujé a la piscina y lo ayudó a secarse y después se fueron a no sé dónde."

            d "¿Y tú qué hiciste después?"

            c "Me fui a dar un paseo."
            c "Estaba cabreadísimo, pero cuando volví se me había pasado y me fui directo a la cama."
            c "Me dormí rapidísimo."
            c "Enfadarse cansa."

            d "¿Cuándo llegaste a casa después de tu paseo?"

            c "A las 4:03 AM. Esto sí que lo se bien. Lo vi en el despertador justo antes de dormirme."
            python:
                carlosBranch6  = False
                ericBranch2 = True
            jump CarlosIntMenu

        "¿Viste a Lucas durante la noche?" if carlosBranch6:
            c "¿Por qué me preguntas esto?"
            c "¿En serio crees que he sido yo?"
            c "¿Su jodido mejor amigo?"
            c "Pff... llévame preso si tan seguro estás."

            d "Tengo información que te hace el principal sospechoso ahora mismo."

            c "Pues sí. Sí que lo vi."
            c "No podía dormir anoche, por lo que salí a tomar el aire y al rato apareció él."

            d "¿Sobre qué hora fue esto?"

            c "Yo qué sé."
            c "Lo único de lo que estoy seguro es de que yo ya estaba en la cama a las cuatro"

            d "¿Puedo saber de qué hablásteis?"
            
            c "De la vida."
            c "Nos pusimos al día. Hacía bastante que no nos veíamos."

            d "¿Y en ningún momento pasásteis por la piscina?"

            c "Qué va. Hacía frío a esas horas."
            c "No se cómo acabó muerto allí. Pero por mi culpa no fue."
            python:
                carlosBranch6 = False
                ericBranch3 = True
            jump CarlosIntMenu
            
        "Muchas gracias. Con esto es suficiente.":
            jump escenaDelCrimen
     
# ----------------- ----- ------ -----------------

# ----------------- Inte. Eric -----------------

label EricInt:
    if ericBranch0:
        d "Buenas días. ¿Eric verdad?"

        e "Aaaaagh..."

        d "Me gustaría hacerte unas preguntas"

        e "Hhmmm..."

        d "Veo que esto va a ser difícil..."
        
        python:
            ericBranch0 = False

    menu EricIntMenu:
        "¿Eric?" if ericBranch1:
            e "Aargh... "
            e "Déjame en paz..."
            python:
                ericBranch1 = False
            jump EricIntMenu

        "¿Estás mejor?" if ericBranch2:
            e "Sí... Más o menos..."

            d "¿Estuviste anoche en la piscina?"

            e "Hmm... sí... estaban Carlos y Lucas peleando..."

            d "¿Qué ocurrió?"

            e "Hmm..."

            menu:
                "¿Qué pasó en la piscina?, Eric":
                    e "Aaargh..."
                
                "Eric, concéntrate, tú puedes.":
                    e "Hmmm..."
                
            e "Se estaban gritando... y los separé..."

            menu:
                "Esto es importante, necesito detalles, por favor.":
                    e "¿Por qué es importante...? ¿Tú quién eres...?"
                
                "Espabila, Eric, no tenemos todo el día":
                    e "Voy... voy..."
                
            e "Los separé... y me fui con Lucas... a la azotea..."
            e "Conseguí que se fumase uno, hehehe"
            e "Nunca lo había visto tan contento..."

            menu:
                "¿Lo drogaste?":
                    e "Hehehe... un poco solo... nada que pudiese matarlo..."
                
                "Y qué pasó después":
                    e "Aaargh... no me acuerdo..."

            d "Eric, dame un segundo."

            e "Si..."

            n "Haces una llamada a la Agencia"

            a "¿Sí?"

            d "Aarón, soy yo, [nombre]."
            d "Necesito la información de la autopsia."

            a "Tenemos pocos datos, de momento."
            a "Parece ser que tiene un par de costillas rotas y que terminó de morir ahogado."
            a "No se cómo acabaría así el chiquillo pero tuvo que sufrir cosa mala."

            d "¿Se han encontrado restos de estupefacientes en la sangre?"
            d "Marihuana, concretamente."

            a "Justo. Perdona. No se cómo he pasado eso por alto."

            d "Perfecto. Muchas gracias."

            n "Terminas la llamada."

            python:
                ericBranch2 = False
                ericBranch4 = True
            jump EricIntMenu
        
        "¿Estás mejor?" if ericBranch3:
            e "Sí... Más o menos..."

            d "¿Ocurrió algo anoche?"

            e "Hmm... No lo sé... Oí a gente discutir..."
            
            d "¿Te acuerdas de quienes eran?"

            e "Agh..."
           
            menu:
                "Esto es importante, necesito detalles, por favor.":
                    e "¿Por qué es importante...? ¿Tú quién eres...?"
                
                "Espabila, Eric, no tenemos todo el día":
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
            e "Y menos mal... sino me hubiese llevado a rastras a mi cuarto... hehehe..."

            python:
                ericBranch3 = False
            jump EricIntMenu

        "¿Dónde estuvisteis Lucas y tú fumando?" if ericBranch4:
            e "Hmmm..."
            e "Aaargh..."
            e "A la azotea, creo..."

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

            e "No lo se. Con su novia, seguramente..."

            d "¿Y tú qué hiciste después?"

            e "Beber... Necesitaba beber... me lo pedía el cuerpo..." 
            
            python:
                ericBranch4 = False
            jump EricIntMenu

        "Terminar":
            jump escenaDelCrimen

# ----------------- ----- ---- -----------------

# ----------------- Inte. Raquel -----------------

label RaquelInt:

    if ( raquelBranch0 ):
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

        python:
            raquelBranch0 = False

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

                    python:
                        if carlosBranch5AlreadyFound == False:
                            carlosBranch5 = True
                            carlosBranch5AlreadyFound = True

                        joanaBranch5 = True


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
                carlosBranch4 = True
                raquelBranch4 = True
            jump RaquelIntMenu

        "Entiendo que fuiste tú quién encontró primero el cuerpo" if raquelBranch2:
            r "Sí..."

            d "¿Ocurrió algo antes de que lo encontrases?"

            r "Por la noche... me despertaron... al principio eran murullos..."
            r "Pero luego pude distinguir las voces..."

            d "¿Qué ocurre, Raquel? ¿De quién eran las voces?"

            r "De Carlos y Lucas... Estaban en la piscina, parecía que estaban discutiendo..."
            r "Carlos parecía muy alterado..."
            r "También escuché agua... Creo que alguien se cayó a la piscina... *llora*"

            d "¿Crees que Carlos podría hacer algo así?"

            r "No lo se..."
            r "Él... él nunca haría nada así..."
            r "Es verdad que a veces es algo... irascible... y se enfada y grita mucho..."
            r "Pero nos quiere a todos... quería mucho a Lucas..."

            d "Tranquilizate. Respira..."

            r "Lo siento"

            d "No pasa nada. Ahora procede. ¿Qué oíste?"

            r "A Carlos y Lucas. Estaban en la piscina, no se qué decían pero por el tono de voz sé que Carlos estaba enfadado. Y escuché agua y más gritos."

            menu RaquelQ2:
                "¿Hiciste algo? ¿Te acercaste a ellos?":
                    r "No... me seguí durmiendo... En su momento no le di importancia, ¿sabe?"
                    r "Pensé que simplemente estarían jugando..."

                "¿Esto se lo has contado a alguien más?":
                    r "No... Nadie más lo sabe..."
                    r "O por lo menos yo no lo he contado..."

            d "¿Sobre qué hora fue esto?"

            r "No lo recuerdo... Sería sobre la una, una y pico..."

            d "Muy bien."

            python: 
                raquelBranch2 = False
                carlosBranch6 = True
                joanaBranch6 = True
            jump RaquelIntMenu

        "¿Cómo era Lucas?" if raquelBranch3:
            r "Muy buena gente."
            r "Se llevaba bien con todos. Era un chico educado..."
            r "Todavía no me creo que le haya pasado esto a él..."
            python:
                raquelBranch3 = False
            jump RaquelIntMenu

        "¿Ocurrió algo esta mañana?" if raquelBranch4:
            r "Fui a la cocina a por algo para comer... Saqué algo de la despensa, me preparé un café y cuando fui a sentarme en la mesa, vi un cuerpo en flotando boca abajo en la piscina..."
            r "Enseguida lo reconocí... *llora*"

            d "Me estás ayudando mucho, continúa, por favor."

            r "Abrí el ventanal y me acerqué... estaba pálido..."

            d "Y fue ahí cuándo gritaste, ¿no?"

            r "Sí..." 
            python:
                raquelBranch4 = False
            jump RaquelIntMenu

        "Muchas gracias por todo.":
            jump escenaDelCrimen


 
# ----------------- ----- ------ -----------------

# ----------------- Inte. Joana -----------------

label JoanaInt:

    if joanaBranch0:

        d "Buenos días. ¿Estás preparada para hablar de lo de anoche?"

        j "Ha sido por mi culpa... Nada de esto hubiese ocurrido si yo no... *llora*"

        d "¿Qué pasó?"

        j "Hice algo que no debería haber hecho... Pero tampoco esperaba que fuese a molestarle tanto... Era solo un juego..."

        d "¿Jugásteis a un juego?"

        j "Sí... hemos jugado ya varias veces y es realmente una tontería... pero el problema aquí es que me tocó darle un beso a Carlos..."

        d "Continúa"

        j "El caso es que tampoco tendría que habérselo tomado tan mal, no es para tanto."
        j "Lucas sabía perfectamente que yo no sentía nada por Carlos, que le quería a él."
        j "Además, me habían puesto ese reto, ¿qué iba a hacer yo?"
        j "Hice lo que tenía que hacer y punto."
        j "No esperaba que fuese a sentarle tan mal..."

        python:
            joanaBranch0 = False

    menu JoanaIntMenu:
        "Entonces, ¿Lucas y tú erais pareja?" if joanaBranch1:
            j "Por favor, no hables de él en pasado..."

            d "Lo siento."

            j "Da igual..."
            j "Lucas y yo llevábamos un año juntos."
            j "Fuimos amigos durante mucho tiempo hasta que nos dimos cuenta de que nos gustábamos."

            python:
                joanaBranch1 = False
            jump JoanaIntMenu

        "¿Crees que Lucas pudo haberse suicidado por el beso?" if joanaBranch2:
            j "Creo que sí... si no, qué otra cosa podría ser..."
            j "Es todo por mi culpa..."

            d "Es importante que entiendas que nosotros no somos responsables de las emociones de los demás"
            d "Antes de darle el beso a Carlos: ¿pensaba que eso podría hacerle daño a Lucas?"

            j "..."
            j "No..."
            j "Creía que todo estaba bien entre Lucas y Carlos..."
            j "Juraría que eran incluso mejores amigos..."
            j "Y además, Lucas sabía perfectamente lo mucho que le quería y que no sentía nada por Carlos"

            python:
                joanaBranch2 = False
            jump JoanaIntMenu

        "¿Qué ocurrió después?" if joanaBranch3:
            j "Al rato Lucas salió fuera, a tomar el aire."
            j "Ahí entendí que le molestó algo, por lo que le di un poco de tiempo y después salí a verle."

            d "Y ¿cómo estaba?"

            j "Sentado en el porche:"
            j "Tranquilo y sereno."

            d "Continúa"

            j "Me senté a su lado y le dije lo que ya sabía"
            j "Que le quería mucho y que no se preocupase por la tontería esta."

            d "¿Y qué dijo?"

            j "No mucho..."

            python:
                joanaBranch3 = False
            jump JoanaIntMenu

        "Tengo entendido que Lucas y tú discutisteis en el porche. ¿Es eso cierto?" if joanaBranch4:
            j "S-sí..."
            j "La verdad es que acabé levantando un poco la voz..."
            j "No tenía ningún sentido que se fuese a enfadar por eso"
            j "Ya no somos niños, ¿sabes?"
            j "Quizás si no hubiese sido tan bruta..."
            j "Si hubiese tenido un poco más de tacto con él..."
            j "Creo que tendría que haberme quedado dentro y dejar que otro saliese a buscarle... Solo empeoré las cosas..."

            python:
                joanaBranch4 = False
            jump JoanaIntMenu

        "¿Carlos y tú fuisteis pareja?" if joanaBranch5:
            j "Supongo que te lo habrá contado alguien."
            j "Sí, estuvimos juntos unos cuatro meses."
            j "Me arrepiento enormemente, nunca llegó a funcionar. Fue un error."
            
            d "¿Cuándo ocurrió todo esto?"

            j "Un par de años antes se salir con Lucas."

            d "¿Lucas sabía todo esto?"

            j "Claro."

            d "¿Sabes si Carlos siente algo por ti a día de hoy?"

            j "Hmm..."
            j "No creo. Me sorprendería mucho."
            j "Sí que es cierto que Carlos se lo echó en cara a Lucas cuando empezamos a salir."
            j "Le dijo el típico comentario fuera de lugar: 'Me la has robado, eh'..."
            j "Dudo que fuese en serio o que le estuviese echando algo en cara."

            d "¿Quizás Lucas pudo entender otra cosa?"

            j "No creo, la verdad."
            j "Pero ahora que lo dices... quizás sí..."
            j "Lucas es-"
            j "Era... bastante dramático"

            python:
                if carlosBranch5AlreadyFound == False:
                    carlosBranch5 = True
                    carlosBranch5AlreadyFound = True
                joanaBranch5 = False
            jump JoanaIntMenu

        "¿Crees que Carlos podría estar involucrado en el presunto asesinato?" if joanaBranch6:
            j "¿Carlos?"

            d "Sí"

            j "¿Crees que Carlos lo ha matado?"

            d "¿Se te ocurre algún motivo que lo pudiese empujar a hacerlo?"

            j "No, la verdad es que no."

            d "¿Y no escuchaste nada por la noche?"

            j "No..."

            menu joanaQ6:
                "¿Seguro?":
                    j "Pff..."
                    j "No pude dormir casi esa noche..."
                    j "Lucas se había enfadado tanto que no había venido ni a nuestra habitación..."
                    j "Entonces estuve pensando cómo solucionarlo"
                    j "y se me ocurrió que quizás sería buena idea que Carlos y Lucas hablasen..."
                    
                    d "Continúa."

                    j "Fui a la habitación de Carlos a buscarlo, pero no estaba."
                    j "Y al volver a la mía escuché a Eric y Lucas partirse de risa en la azotea..."
                    j "Sinceramente, me alegré de que estuviese con alguien y de que además se lo estuviese pasando tan bien"
                    j "No se de qué narices se reirían pero no lo había escuchado reirse así nunca."
                    j "Supongo que gracias a esto mis preocupaciones se fueron y por fin pude pegar ojo."

                    d "¿Sabrías decirme sobre qué hora fue esto?"

                    j "Sobre las tres, creo."

                "Me da la sensación de que ocultas algo...":
                    j "No. En absoluto. Simplemente estoy cansada."

            python:
                joanaBranch6 = False
            jump JoanaIntMenu

        "Terminar":
            jump escenaDelCrimen

# ----------------- ----- ----- -----------------
