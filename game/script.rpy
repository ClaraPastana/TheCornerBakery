#finalBossGame Variables
default player_x = 320
default player_y = 240
default player_hp = 20
default boss_hp = 50

default battle_active = True

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
    
    menu _1c_First_Choice:
        "What do you say?"
        "\"Good Morning!\"":
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
            jump _1c_First_Choice_1a

        "\"It's hot today, isn't it?\"":
            pov "It's hot today, isn't it?"
            un "Hmm, yeah...kind of."
            n "The client seem a little unconfortable."
            n "After some awkward seconds, he takes a look at the menu"
            un "Hum... Could I get two double shots? To go."
            pov "Sure. What's your name?"
            c "It's Cleiton."
            pov "Okay."
            jump _1c_First_Choice_1b


        "\"...\"":
            pov "..."
            n "He looks at the menu"
            un "Hum... Could I get two double shots? To go."
            pov "Sure. What's your name?"
            c "It's Cleiton."
            pov "Okay."
            jump _1c_First_Choice_1b


    label _1c_First_Choice_1a:
        $ gentleness += 1
        jump _1c_Common_End

    label _1c_First_Choice_1b:
        jump _1c_Common_End

    #Common ending for first customer interaction

    label _1c_Common_End:
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
    label after_1c:
        menu:
            "What do you want to do now?"
            "Clean the counter":
                pov "Better clean the counter before the next customer arrives."
                n "You quickly clean the counter, making sure everything is spotless for the next customer."
                $ dedication += 1
                jump _2c_entry

            "Wait for the next customer":
                pov "Might as well wait for the next customer to arrive."
                n "You stand behind the counter, waiting for the next customer to enter the bakery."
                jump _2c_entry

            "Take one of the candies in display":
                pov "I could use a little treat while I wait."
                n "You sneakily take one of the candies from the display and enjoy it."
                n "Feeling a bit more energized, you prepare for the next customer."
                $ dedication -= 1
                jump _2c_entry

    #Entry second customer

    label _2c_entry:

        n "Dings the doorbell again"
        pov "Another customer! Time to get back to work."
        n "A little kid enters the bakery, looking around wary. He's using a school uniform and has
        a small backpack."
        n "His large glasses make his eyes look even bigger, giving him an innocent appearance."
        n "He aproches the counter apprehensive."
        un "H-hello! I could I get a C-Cueca Virada, please."
        pov "What's your name?"
        j "My name? It is- is João."

        #Second customer interaction first desicion

        menu _2c_Choice:
            "How to respond?"

            "\"Such a nice name!\"":
                pov "Such a nice name! A Cueca Virada is a great choice. Would you like anything to drink with that?"
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

                menu kidCandyChoice:
                    "Give him candy as change":
                        pov "Alright, I'll give you some candy as change this time."
                        n "You hand the kid some candy from the display."
                        j "Yay! Thank you so much!"
                        n "The kid happily takes the candy."
                        $ gentleness += 1
                        $ dedication -= 1
                        
                        if gentleness == 2
                            jump kidOrderPreparation_A
                        else 
                            jump kidOrderPreparation_B
                
                    "No candy change":
                        pov "As I said, we don't do that here. Here's your change in cash."
                        n "The kid looks disappointed but accepts the cash."
                        $ dedicated += 1
                        jump kidOrderPreparation_B

                label kidOrderPreparation_A:
                    n "You prepare the order while João waits patiently."
                    n "Once it's ready, you hand it over to him with a smile."
                    pov "Here you go! Enjoy your Cueca Virada and juice box!"
                    j "Th-thank you so much!"
                    n "The kid takes his order happily and leaves the bakery, waving goodbye."

                    pov "That was a nice interaction. It's always great to see kids enjoying their treats."

                label kidOrderPreparation_B:
                    n "You prepare the order while João waits patiently."
                    n "Once it's ready, you hand it over to him."
                    j "..."
                    n "The kid takes his order and leave more nervous than when he arrived.."

            "Take a Cueca Virada from the display":
                n "You take a Cueca Virada from the display"
                pov "Here's your Cueca Virada."
                pov "That will be R$7,00."
                n "The boy hands you a 10 reais bill."
                j "Could you give me the change in candy, please?"
                pov "Sorry, we don't do that here."
                j "But I see some candies over there..."
                jump kidCandyChoice                 

    
    #Comentarios pós cliente
    
    pov "I pity him. Kids can be so cruel to each other at school."

    pov "I'm sure he suffers bullying at school with this stutter."

    #After second customer interaction

    #Plant atribute
    #Adicionar Jiboia?
    default wateredPlants = False
    default catInteraction = False

    label after_2c:
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
                    $ catInteraction = True

                
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
                    $ dedication += 1

                "Wait for the next customer":
                    pov "Might as well wait for the next customer to arrive."
                    n "You stand behind the counter, waiting for the next customer to enter the bakery."

                "Water plants":
                    pov "The plants could use some water."
                    n "You take a moment to water the plants around the bakery, giving them some much-needed hydration."
                    n "Feeling a bit more connected to the space, you return to the counter."
                    $ dedication += 1

    #Entry 3c

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

        menu _3c_Choice:
            "How to respond?"
            "Trying to get to know my customers better":
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
                
                menu _3c_Choice_a:
                    "Compliment her tote bag":
                        pov "By the way, I love your tote bag! The floral pattern is so pretty."
                        l "Thank you! I got it from a local artisan market. I'm glad you like it."
                        pov "It's always nice to support local artists."
                        $ gentleness += 1
                        jump _3c_Order_Preparation

                    "Say nothing more":
                        "..."
                jump _3c_Order_Preparation

            "Just for my records":
                pov "Just for my records."
                l "Oh, okay."

                menu:
                    "Comment on her tote bag":
                        pov "That's a nice tote bag you have there."
                        l "Thanks, I got it from a local artisan market."
                        pov "Hmm."
                        jump _3c_endB

                    "Say nothing more":
                        "..."
                jump _3c_endC
    

        if gentleness > 7:
            l "You seem like a really kind person. It's nice to see someone so dedicated to their work."
            pov "Thank you, Lúcia! I really appreciate that."
            l "I can tell you care a lot about this bakery. It shows in the atmosphere and the quality of your products."
            l "Do you own this place?"
            pov "Yes, I do! It's been a dream of mine to run my own bakery since I was little."
            pov "I remember baking with my mother and helping her sell treats in the street early in the day."
            pov "Her only goal back then was to provide for our family, but she inspired me to pursue my passion for baking."
            l "Well, you're doing an amazing job. This place is amazing!"
            pov "That means a lot to me. Thank you for your support!"

        if gentleness > 5 and watered_plants==True:
            l "DId you water this plants earlier? They look really healthy and vibrant!"
            pov "Yeah, Thanks! I try to take good care of them. A little greenery goes a long way in making the bakery feel welcoming."
            l "Absolutely! It really adds to the ambiance."
            l "You know what? I think I'll come here more often. This place has a great vibe. I'll even bring my friends! You guys really deserve more customers."
            pov "That's wonderful to hear! I appreciate your support."

        jump _3c_endA

#Good gentleness path
label _3c_endA:
    n "You prepare Lúcia's order while she waits patiently."
    n "Once it's ready, you hand it over to her with a smile."
    pov "Here you go! Enjoy your coffee and tapioca!"
    l "Thank you so much!"
    n "Lúcia takes her order happily and leaves the bakery, waving goodbye."

    pov "That was a pleasant interaction. I hope she enjoys her order."
    jump after_3c

#A bit bad gentleness path
label _3c_endB:
    n "You prepare Lúcia's order while she waits patiently."
    n "Once it's ready, you hant it over to her"
    pov "Here you go."
    n "Lúcia takes her order and leave giving the space a new tone of solitude."
    n "You feel a bit disheartened by the lack of connection with your customers today."
    n "After all, the only reason you started doing this was to meet new people and spread gentleness."
    n "You sigh, hoping the next customer will be more engaging."
    jump after_3c

#Worst gentleness path
label _3c_endC:
    n "You prepare Lúcia's order while she waits patiently."
    n "Once it's ready, you hant it over to her"
    n "Lúcia takes her order and leave giving the space a new tone of solitude."
    n "You feel a disheartened by the lack of connection with your customers today."
    n "After all, one of the reasons you started doing this was to meet new people and spread gentleness."
    n "You sigh, hoping the next customer will be more engaging."
    jump after_3c

label after_3c:
    #If hadn't have cat interaction and have gentleness >=3
    if catInteraction == False and gentleness >=3:
        menu:
            "What do you want to do now?"
            "Prepare for the next customer":
                pov "Better get things ready for the next customer."
                n "You tidy up the counter and prepare for the next customer."
                pov "Oh! What is this?"
                n "You find a small note left on the counter by Lúcia."
                n "It reads: 'Thank you for your kindness and dedication. Your bakery is a true gem in this city. Keep up the great work!' and her phone number below."
                pov "Haha, this Lúcia is truly something. That's so nice of her! I should give her a call sometime."
                $ dedication += 1

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
                $ catInteraction = True

            "Do some stretches":
                        pov "My back is a bit sore. I should do some stretches."
                        n "You take a moment to stretch your arms and legs, relieving some tension."

    #If hadn't have water plants interaction and have dedication >=3
    if else wateredPlants == False and dedication >=3:
        menu:
            "What do you want to do now?"
            "Prepare for the next customer":
                        pov "Better get things ready for the next customer."
                        n "You tidy up the counter and prepare for the next customer."
                        pov "Oh! What is this?"
                        n "You find a small note left on the counter by Lúcia."
                        n "It reads: 'Thank you for your kindness and dedication. Your bakery is a true gem in this city. Keep up the great work!' and her phone number below."
                        pov "Haha, this Lúcia is truly something. That's so nice of her! I should give her a call sometime."
                        $ dedication += 1

            "Water plants":
                    pov "The plants could use some water."
                    n "You take a moment to water the plants around the bakery, giving them some much-needed hydration."
                    n "Feeling a bit more connected to the space, you return to the counter."
                    $ dedication += 1
                    $ watered_plants = True
                    
            "Take a break":
                pov "I think it's time for a short break."
                n "You step away from the counter to take a breather."
            

    #If had cat and water plants interaction or didn't reach the gentleness/dedication threshold
    else:
        menu:
            "What do you want to do now?"
            "Prepare for the next customer":
                        pov "Better get things ready for the next customer."
                        n "You tidy up the counter and prepare for the next customer."
            "Take a break":
                        pov "I think it's time for a short break."
                        n "You step away from the counter to take a breather."
            "Do some stretches":
                        pov "My back is a bit sore. I should do some stretches."
                        n "You take a moment to stretch your arms and legs, relieving some tension."
return
#Free cookie