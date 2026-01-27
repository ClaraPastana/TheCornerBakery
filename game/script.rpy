# Define characters
define u = Character("You", color="#93e436")
define un = Character("Unknown", color="#e49336")
define c = Character("Cleiton", color="#4363e4")
define n = Character(" ", color="#e4e243", what_prefix="{i}", what_suffix="{/i}")

# The game starts here.

label start:

    #Entry first customer

    scene bg blackscreen
    scene bg bakery

    u "Yikes!"
    u "I arrived late to open the store today..."
    u "I'll have to get things moving before the customers arrive."

    play music "audio/bakery_theme.ogg" fadein 1.0

    scene bg view_from_balcony

    play music "audio/doorbell.ogg" fadein 1.0

    n "Dings the doorbell"
    u "Oh! The first customer of the day has arrived"

    #Greeting the first customer desicion

    default gentleness = 0
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
        $ gentleness = 1
        jump First_Customer_Common_End

    label First_Customer_First_Choice_1b:
        jump First_Customer_Common_End

    #Common ending for first customer interaction

    label First_Customer_Common_End:
        n "While you prepare the order, Cleiton looks around the bakery."
        n "He seems nervous and keep tapping his foot."

        if gentleness:
            u "Is everything alright, Cleiton? You seem a bit nervous."
            c "Oh, um, yeah. I'm just... I'll visit my grandson today."
            u "That's wonderful! Grandchildren are such a blessing."
            c "Yeah... It's been a while since I last saw him. Ten years, actually."
            u "Wow, ten years is a long time. I'm sure your grandson will be thrilled to see you."
            c "Not so sure about that... "
            c "His name in Gabriel. When he said he wanted to be a musician..."
            c "I didn't take it well. We fought a lot before he moved here, to the big city. We just stopped talking."
            u "I'm sorry to hear that. Maybe this visit will be a chance to reconnect."
            c "I hope so..."
            c "Anyways, thanks for being so kind."
            u "Of course! Here's your order, Cleiton."
            c "Thanks a lot."
            n "Cleiton takes his order with a small smile and leaves the bakery, looking more hopeful than before."

            u "That was an interesting encounter. Hope everything goes well for him."

        else:
            u "Here's your order."
            c "Thanks."
            n "Cleiton quickly takes his order and leaves the bakery without another word."
            n "You sight hoping that the next customer will be a bit more friendly."    
        
    default dedication = 0
    label after_first_customer:
        menu:
            "What do you want to do now?"
            "Clean the counter":
                u "Better clean the counter before the next customer arrives."
                n "You quickly clean the counter, making sure everything is spotless for the next customer."
                $ dedication = 1
                jump Second_Customer_entry

            "Wait for the next customer":
                u "Might as well wait for the next customer to arrive."
                n "You stand behind the counter, waiting for the next customer to enter the bakery."
                jump Second_Customer_entry

    #Entry second customer

    label Second_Customer_entry:

        n "Dings the doorbell again"
        u "Another customer! Time to get back to work."
        n "A little kid enters the bakery, looking around excitedly. He's using a school uniform and has
        a small backpack."
        n "His large glasses make his eyes look even bigger, giving him an innocent and curious appearance."
        n "He aproches the counter eagerly."
        un "H-hello! I would like a Cueca Virada, please."

        menu Second_Customer_Choice:
            "How to respond?"

            #Edit this after testing
            "Be friendly":
                u "Of course! A Cueca Virada is a great choice. Would you like anything to drink with that?"
                un "U-um... Yes, please! Could I have a hot chocolate?"
                u "Sure thing! Anything else?"
                un "N-no, that's all. Thank you!"
                u "You're welcome! That will be $5.50."
                un "Here you go!"
                u "Thanks! Your order will be ready in just a moment."
                n "You prepare the order while the kid waits patiently."
                n "Once it's ready, you hand it over to him with a smile."
                u "Here you go! Enjoy your Cueca Virada and hot chocolate!"
                un "Th-thank you so much!"
                n "The kid takes his order happily and leaves the bakery, waving goodbye."

                u "That was a nice interaction. It's always great to see kids enjoying their treats."

            "Be indifferent":
                u "Here's your Cueca Virada."
                u "That will be R$25,00."
                n "The boy hands you a 30 reais bill."
                un "Could you give me the change in candy, please?"
                u "Sorry, we don't do that here."
                un "But I see some candies over there..."
                
                menu Kid_Candy_Choice:
                    "Give him candy as change":
                        u "Alright, I'll give you some candy as change this time."
                        $ gentleness += 1
                    
                    "No candy change":
                        u "As I said, we don't do that here. Here's your change in cash."

        

    return


