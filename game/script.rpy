# Define characters
define u = Character("You", color="#93e436")
define un = Character("Unknown", color="#e49336")
define c = Character("Cleiton", color="#4363e4")
define n = Character(" ", color="#e4e243")

# The game starts here.

label start:

    scene bg blackscreen
    scene bg bakery

    u "Yikes!"
    u "I arrived a late to open the store today..."
    u "I'll have to get things moving before the customers arrive."

    play music "audio/bakery_theme.ogg" fadein 1.0

    scene bg view_from_balcony

    play music "audio/doorbell.ogg" fadein 1.0

    u "Oh! The first customer of the day has arrived"

    default was_gentle = False
    menu First_Customer_First_Choice:
        "What should i do?"
        "Greet the customer":
            u "Good morning! Welcome to my bakery! How can I help you today?"
            un "Hi!"
            un "Could I get two double shots, please? To go."
            u "Sure thing! Coming right up."
            un "Oh! And do you have bread with scrambled eggs?"
            u "Yes, we do! I'll get that for you as well."
            un "Great! Thank you so much."
            u "My pleasure! Could you just tell me your name?"
            c "It's Cleiton"
            u "Such a nice name!"
            c "Thanks!"
            u "Alright, Cleiton, your order will be ready in just a moment."
            jump First_Customer_First_Choice_1a

        "Be indiferent":
            u "..."
            n "He looks at the menu"
            un "Hum... Could I get two double shots? To go."
            u "Sure. What's your name?"
            c "It's Cleiton."
            u "Okay."
            jump First_Customer_First_Choice_1b


    label First_Customer_First_Choice_1a:
        $ was_gentle = True
        jump First_Customer_Common_End
    label First_Customer_First_Choice_1b:
        jump First_Customer_Common_End

    label First_Customer_Common_End:
        n "While you prepare the order, Cleiton looks around the bakery."
        n "He seems nervous and keep tapping his foot."




    return


