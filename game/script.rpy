# Define characters (General)
define pov = Character("You", color="#93e436")
define un = Character("Unknown", color="#e49336")
define n = Character(" ", color="#e4e243", what_prefix="{i}", what_suffix="{/i}")

# Define characters (Specific)
define c = Character("Cleiton", color="#4363e4")
define j = Character("João", color="#e44393")
define l = Character("Lúcia", color="#43e4d4")
define r = Character("Roberto", color="#e44343")
define f = Character("Flora", color="#a843e4")

# The game starts here.

label start:

    #Entry first customer

    scene bg blackscreen
    scene bg bakery

    pov "Yikes!"
    pov "I arrived late to open the store today..."
    pov "I'll have to get things moving before the customers arrive."

    play music "audio/bakery_theme.ogg" fadein 1.0

    scene bg view_from_balcony

    play music "audio/doorbell.ogg" fadein 1.0

    n "Dings the doorbell"
    pov "Oh! The first customer of the day has arrived"

    #Greeting the first customer desicion

    default gentleness = 0
    menu First_Customer_First_Choice:
        "What should i do?"
        "Greet the customer":
            pov "Good morning! Welcome to my bakery! How can I help you today?"
            un "Hi!"
            un "Could I get two double shots, please? To go."
            pov "Sure thing! Coming right up."
            un "Oh! And do you have bread with scrambled eggs?"
            pov "Yes, we do! I'll get that for you as well."
            un "Great! Thank you so much."
            pov "My pleasure! Could you just tell me your name?"
            c "It's Cleiton"
            pov "Such a nice name!"
            c "Thanks!"
            pov "Alright, Cleiton, your order will be ready in just a moment."
            jump First_Customer_First_Choice_1a

        "Be indiferent":
            pov "..."
            n "He looks at the menu"
            un "Hum... Could I get two double shots? To go."
            pov "Sure. What's your name?"
            c "It's Cleiton."
            pov "Okay."
            jump First_Customer_First_Choice_1b


    label First_Customer_First_Choice_1a:
        $ gentleness += 1
        jump First_Customer_Common_End

    label First_Customer_First_Choice_1b:
        jump First_Customer_Common_End

    #Common ending for first customer interaction

    label First_Customer_Common_End:
        n "While you prepare the order, Cleiton looks around the bakery."
        n "He seems nervous and keep tapping his foot."

        if gentleness >= 1:
            pov "Is everything alright, Cleiton? You seem a bit nervous."
            c "Oh, um, yeah. I'm just... I'll visit my grandson today."
            pov "That's wonderful! Grandchildren are such a blessing."
            c "Yeah... It's been a while since I last saw him. Ten years, actually."
            pov "Wow, ten years is a long time. I'm sure your grandson will be thrilled to see you."
            c "Not so sure about that... "
            c "His name is Gabriel. When he said he wanted to be a musician..."
            c "I didn't take it well. We fought a lot before he moved here, to this big city. We just stopped talking."
            pov "I'm sorry to hear that. Maybe this visit will be a chance to reconnect."
            c "I hope so..."
            c "Anyways, thanks for being so kind."
            pov "Of course! Here's your order, Cleiton."
            c "Thanks a lot."
            n "Cleiton takes his order with a small smile and leaves the bakery, looking more hopeful than before."

            pov "That was an interesting encounter. Hope everything goes well for him."

        else:
            pov "Here's your order."
            c "Thanks."
            n "Cleiton quickly takes his order and leaves the bakery without another word."
            n "You sight hoping that the next customer will be a bit more friendly."    
        
    #After first customer interaction
    
    default dedication = 0
    label after_first_customer:
        menu:
            "What do you want to do now?"
            "Clean the counter":
                pov "Better clean the counter before the next customer arrives."
                n "You quickly clean the counter, making sure everything is spotless for the next customer."
                $ dedication += 1
                jump Second_Customer_entry

            "Wait for the next customer":
                pov "Might as well wait for the next customer to arrive."
                n "You stand behind the counter, waiting for the next customer to enter the bakery."
                jump Second_Customer_entry

            "Take one of the candies in display":
                pov "I could use a little treat while I wait."
                n "You sneakily take one of the candies from the display and enjoy it."
                n "Feeling a bit more energized, you prepare for the next customer."
                $ dedication -= 1
                jump Second_Customer_entry

    #Entry second customer

    label Second_Customer_entry:

        n "Dings the doorbell again"
        pov "Another customer! Time to get back to work."
        n "A little kid enters the bakery, looking around excitedly. He's using a school uniform and has
        a small backpack."
        n "His large glasses make his eyes look even bigger, giving him an innocent and curious appearance."
        n "He aproches the counter eagerly."
        un "H-hello! I would like a C-Cueca Virada, please."
        pov "What's your name?"
        j "It is- is João."

        #Second customer interaction first desicion

        menu Second_Customer_Choice:
            "How to respond?"

            "Be friendly":
                pov "Awesome! A Cueca Virada is a great choice. Would you like anything to drink with that?"
                j "U-um... Yes, please! Could I ha-have a juice box?"
                pov "Sure thing! Anything else?"
                j "N-no, that's all. Thank you!"
                pov "You're welcome! That will be R$15,00."
                j "Hmm ..." 
                n "He rummages through his backpack and pulls out a 20 reais bill."
                j "Could you gi-give me the change in candy, please?"
                pov "I'm so sorry João, but I can't do that."
                j "Bu-bu-but I see some candies over t-there..."
                $ gentleness += 1

                #Second customer interaction second desicion

                menu Kid_Candy_Choice_a:
                    "Give him candy as change":
                        pov "Alright, I'll give you some candy as change this time."
                        n "You hand the kid some candy from the display."
                        j "Yay! Thank you so much!"
                        n "The kid happily takes the candy."
                        $ gentleness += 1
                        $ dedication -= 1
                        jump Kid_Order_Preparation
                    
                    "No candy change":
                        pov "As I said, we don't do that here. Here's your change in cash."
                        n "The kid looks disappointed but accepts the cash."
                        jump Kid_Order_Preparation
                        $ dedicated += 1

                label Kid_Order_Preparation:
                n "You prepare the order while João waits patiently."
                n "Once it's ready, you hand it over to him with a smile."
                pov "Here you go! Enjoy your Cueca Virada and juice box!"
                j "Th-thank you so much!"
                n "The kid takes his order happily and leaves the bakery, waving goodbye."

                pov "That was a nice interaction. It's always great to see kids enjoying their treats."

            "Be indifferent":
                pov "Here's your Cueca Virada."
                pov "That will be R$15,00."
                n "The boy hands you a 20 reais bill."
                j "Could you give me the change in candy, please?"
                pov "Sorry, we don't do that here."
                j "But I see some candies over there..."

                #Second customer interaction second desicion
                
                menu Kid_Candy_Choice_b:
                    "Give him candy as change":
                        pov "Alright, I'll give you some candy as change this time."
                        n "You hand the kid some candy from the display."
                        j "Yay! Thank you so much!"
                        n "The kid happily takes the candy and leaves the bakery."
                        $ gentleness += 1
                        pov "I pity him. Kids can be so cruel to each other at school."
                    
                    "No candy change":
                        pov "As I said, we don't do that here. Here's your change in cash."
                        n "The kid looks disappointed but accepts the cash."
                        n "He takes his order and leaves the bakery quietly."

                        pov "I'm sure he suffers bullying at school with this stutter."

    #After second customer interaction

    #Plant atribute
    #adicionar Jiboia
    default watered_plants = False

    label after_second_customer:
        if gentleness >= 2:
            menu:
                "What do you want to do now?"
                "Take a break":
                    pov "I think it's time for a short break."
                    n "You step away from the counter to take a breather."
                    n "A small cat aproaches you, rubbing against your leg."
                    n "It have a calico pattern with patches of orange, black, and white fur. It also have a collar on it's neck with the name 'Muffin' engraved on a small tag."
                    pov "Well, hello there, little one! Are you lost? Do you want some food?"
                    n "The cat meows softly, looking up at you with big, pleading eyes."
                    n "You give Muffin some scraps from the bakery, and it happily devours the food."
                    pov "It probably belongs to someone nearby. I should put up a notice."
                    n "You take a photo of Muffin and edit a quick online notice."
                    n "After posting the notice in social media, you return to the counter feeling refreshed."
                    n "Muffin follows you back to the counter and sits nearby, purring contentedly."
                    pov "Stay there while I finish my shift, okay?"
                    $ gentleness += 1
                
                "Prepare for the next customer":
                    pov "Better get things ready for the next customer."
                    n "You tidy up the counter and prepare for the next customer."
                    $ dedication += 1

                "Water plants":
                    pov "The plants could use some water."
                    n "You take a moment to water the plants around the bakery, giving them some much-needed hydration."
                    n "Feeling a bit more connected to the space, you return to the counter."
                    $ dedication += 1
                    $ watered_plants = True

        #If you weren't kind enough till now

        else:
            menu:
                "What do you want to do now?"
                "Prepare for the next customer":
                    pov "Better get things ready for the next customer."
                    n "You tidy up the counter and prepare for the next customer."
                    $ dedication -= 1

                "Wait for the next customer":
                    pov "Might as well wait for the next customer to arrive."
                    n "You stand behind the counter, waiting for the next customer to enter the bakery."

                "Water plants":
                    pov "The plants could use some water."
                    n "You take a moment to water the plants around the bakery, giving them some much-needed hydration."
                    n "Feeling a bit more connected to the space, you return to the counter."
                    $ dedication += 1

    #Entry third customer

    label thrid_customer_entry:

        n "Dings the doorbell again"
        pov "Another customer! Let's see who it is this time."
        n "A young woman enters the bakery, looking around with a smile."
        n "She has long, flowing hair and is dressed in a casual yet stylish outfit."
        n "She also carries some books and a tote bag with a floral pattern. Seems like she just came from the library by the side of the bakery."
        n "She approaches the counter with a friendly demeanor and take some time looking at the menu."
        un "Hi there! I would like a coffee with a dash of milk and this dry tomato tapioca, please."
        pov "What's your name?"
        l "I'm Lúcia. Why do you ask?"

        menu Third_Customer_Choice:
            "How to respond?"
            "Be friendly":
                pov "Just trying to get to know my customers better! It's nice to meet you, Lúcia."
                l "Nice to meet you too!"
                pov "Actually... this is top secreat information..."
                n "You lower your voice conspirationally, take a look around and lean closer to Lúcia."
                pov "I was supposed to call clients by their names when their order is ready."
                pov "But as the bakery is still new, and as there aren't many customers yet it would be awkward to call out names all the time. Hahaha."
                l "Hahaha, I understand. No worries! Your secret is safe with me."
                n "You both look at each other and share a laugh."
                pov "I'll get your order ready right away"
                $ gentleness += 1
                
                menu Third_Customer_Choice_a:
                    "Compliment her tote bag":
                        pov "By the way, I love your tote bag! The floral pattern is so pretty."
                        l "Thank you! I got it from a local artisan market. I'm glad you like it."
                        pov "It's always nice to support local artists."
                        $ gentleness += 1
                        jump Third_Customer_Order_Preparation

                    "Say nothing more":
                        "..."
                jump Third_Customer_Order_Preparation

            "Be indiferent":
                pov "Just for my records."
                l "Oh, okay."

                menu:
                    "Comment on her tote bag":
                        pov "That's a nice tote bag you have there."
                        l "Thanks, I got it from a local artisan market."
                        pov "Hmm."
                        jump Third_Customer_Order_Preparation

                    "Say nothing more":
                        "..."
                jump Third_Customer_Order_Preparation 

        if gentleness > 7:
            l "You seem like a really kind person. It's nice to see someone so dedicated to their work."
            pov "Thank you, Lúcia! I really appreciate that."
            l "I can tell you care a lot about this bakery. It shows in the atmosphere and the quality of your products."
            l "Do you own this place?"
            pov "Yes, I do! It's been a dream of mine to run my own bakery since I was little."
            pov "I remember baking with my mother and helping her sell treats in the street early in the day."
            pov "Her only goal back then was to provide for our family, but she inspired me to pursue my passion for baking."
            l "Well, you're doing an amazing job. I'll definitely be coming back here often."
            pov "That means a lot to me. Thank you for your support!"

        if gentleness > 5 and watered_plants==True:
            l "DId you water this plants earlier? They look really healthy and vibrant!"
            pov "Yeah, Thanks! I try to take good care of them. A little greenery goes a long way in making the bakery feel welcoming."
            l "Absolutely! It really adds to the ambiance."
            l "You know what? I think I'll come here more often. This place has a great vibe. I'll even bring my friends! You guys really deserve more customers."
            pov "That's wonderful to hear! I appreciate your support."


        label Third_Customer_Order_Preparation:
            n "You prepare Lúcia's order while she waits patiently."
            n "Once it's ready, you hand it over to her with a smile."
            pov "Here you go! Enjoy your coffee and tapioca!"
            l "Thank you so much!"
            n "Lúcia takes her order happily and leaves the bakery, waving goodbye."

            pov "That was a pleasant interaction. I hope she enjoys her order."

    return


#Free cookie