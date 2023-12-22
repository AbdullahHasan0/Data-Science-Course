print("Welcome to the Treasure Hunt Game!")
print("Where your choices determine your fate.")
print("I am your guide. Please tell me your name.")
name = input("Enter Your Name: \n")
print("\nHello", name + "! Let's Begin The Adventure!\n")

print("Once upon a time, in a distant land, there was a notorious pirate named Captain Blackbeard.")
print("Legend has it that Captain Blackbeard had hidden a great treasure on a mysterious island.")
print("Many have tried to find the treasure, but none have succeeded.")

print("You have come across an ancient map that is believed to lead to Blackbeard's treasure.")
print("Your mission is to follow the map's clues, overcome challenges, and claim the treasure for yourself.")

print("You set sail on your ship and reach the island mentioned in the map.")
print("As you step onto the sandy beach, you notice two paths before you. One is going left and other is right")

valid_choices1 = ["left", "right"]
while True:
    choice1 = input("Where do you want to go? Left or Right?\n").lower()
    if choice1 in valid_choices1:
        break
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")

if choice1 == 'right':
    print("As you turn right, you see a large cave in front of you.\n")
    print("You cautiously enter the cave, taking careful steps forward.")
    print("However, just a few steps in, the ground beneath you gives way!")
    print("You plummet into a seemingly endless abyss, your screams echoing into the darkness.")
    print("The fall is merciless, your body battered and broken.")
    print("You lie there, pain coursing through every limb, unable to move.")
    print("Hours turn into days as you lie in that cold, desolate pit, hoping for rescue.")
    print("But rescue never comes. Your treasure hunt ends here, forgotten in the depths of the earth.")
    print("Your tragic fate serves as a solemn reminder of the perils of the unknown.")
    print("Game Over.")

else:
    print("You chose to go left. The adventure continues!\n")
    print("As you turn Left, you see a dense jungle.\n")
    print("The path through the jungle is narrow and winding,\nbut you are determined to find the treasure.")
    print("After hours of walking, you finally spot a glimmer of light coming from a clearing up ahead.")
    print("You continue along the path and come across a rushing lake.")
    print("The water is turbulent, with powerful waves crashing against the shore.")
    print("You notice a small boat tied to a nearby tree.")
    print("As you look across the lake, you spot a treasure box shimmering under a tree.")
    print("Your heart races with excitement. You have two options:")
    print("1. Use the boat to cross the rushing lake.")
    print("2. Wait for the lake to calm down before attempting to swim across.")

valid_choices2 = ["swim", "wait"]
while True:
    choice2 = input("What will you do? Enter 'swim' to use the boat or 'wait' to wait for the lake to calm down.\n")
    
    if choice2 in valid_choices2:
        break
    else:
        print("Invalid choice. Please enter 'swim' or 'wait'.")

if choice2 == 'swim':
    print("You decide to use the boat to cross the rushing lake.")
    print("With careful maneuvering, you navigate the boat through the turbulent waters.")
    print("Just as you reach the middle of the lake, a massive trout jumps out of the water!")
    print("Its razor-sharp teeth sink into your flesh, tearing through muscle and bone.")
    print("You let out a scream of agony as the trout thrashes, dragging you deeper into the lake.")
    print("Desperate and gasping for air, you struggle against the trout's powerful grip.")
    print("But your strength wanes, and darkness engulfs your vision as the water fills your lungs.")
    print("With your last breath, you realize that your adventure has come to a tragic end.")
    print("Game over.")
    
else :
    print("You choose to wait for the lake to calm down.")
    print("Patiently, you observe the wild waves gradually subside.")
    print("As you wait, your eyes wander and notice a peculiar sight in the distance.")
    print("A magical house reveals itself, standing amidst the serene landscape.")
    print("Intrigued by the enchanting aura, you decide to investigate further.")
    print("You approach the mystical house and push open its creaking door.")
    print("Inside, you discover a mesmerizing sight - a room filled with colorful doors.")
    print("Each door beckons with its vibrant hues, promising untold wonders within.")
    print("There are four doors in front of you: a red door, a blue door, a yellow door, and a door that shimmers like a rainbow.")
    


valid_choices3 = ["red", "blue","yellow","rainbow"]
while True:
    choice3 = input("Where do you want to go? red ,blue,yellow or rainbow \n").lower()
    if choice3 in valid_choices3:
        break
    else:
        print("Invalid choice. Please enter 'red' , blue , yellow or rainbow .")
        


if choice3 == "red":
    print("You open the red door and step into a room bathed in warm, fiery light.")
    print("The air is filled with the scent of adventure and the crackling of flames.")
    print("Excitement courses through your veins as you explore further.")
    print("To your horror, you realize that the door you entered from has disappeared, leaving you trapped.")
    print("The flames dance and flicker, their tongues licking at the edges of your sanity.")
    print("As you gaze into the fiery abyss, you notice shadowy forms moving within the inferno.")
    print("Eyes of molten lava peer out from the depths, filled with malevolence and hunger.")
    print("Creatures born from the very essence of fire emerge, their forms wreathed in flames.")
    print("Their skin is charred and cracked, exuding an intense heat that sears the air around them.")
    print("With each step, they leave behind scorch marks on the ground, a testament to their destructive nature.")
    print("The creatures move with an otherworldly grace, their movements a macabre ballet of pain and despair.")
    print("Desperation sets in as you search for an escape, but the fiery inferno closes in around you.")
    print("The scorching heat intensifies, blistering your skin and making it difficult to breathe.")
    print("The smoke fills your lungs, choking your cries for help, as the flames consume everything in their path.")
    print("In the midst of the searing agony, your strength wanes, and your vision fades.")
    print("You collapse to the ground, overwhelmed by the merciless blaze.")
    print("As the flames devour your body, your treasure hunt ends in a tragic demise.")
    print("Game over.")

elif choice3 == "blue":
    print("You open the blue door and find yourself in a room surrounded by shimmering waters.")
    print("The sound of gentle waves and the salty breeze fill the air, creating a serene atmosphere.")
    print("As you venture deeper into the room, you notice movement beneath the waters.")
    print("Suddenly, a pair of colossal sea monsters emerge from the depths, their hulking forms sending chills down your spine.")
    print("Their bodies are covered in thick, scaly armor, glistening with a dark, eerie sheen.")
    print("Their eyes, like orbs of cold, unyielding determination, fixate upon you with a hunger for destruction.")
    print("Each sea monster is easily twice the size of a fully grown whale, their vast jaws lined with rows of razor-sharp teeth.")
    print("As they draw closer, you can feel the tremors in the water, a warning of the imminent danger.")
    print("You frantically search for an escape route, but the door you entered from has vanished, leaving you trapped.")
    print("Panic begins to consume you as the sea monsters close the distance with a terrifying swiftness, their massive jaws ready to devour you.")
    print("Their foul breath, a mix of decay and saltwater, fills the air, making it hard to breathe.")
    print("You desperately try to fight back, but your feeble attempts are no match for their monstrous strength.")
    print("Their jaws snap shut around your limbs, crushing bone and tearing flesh, causing searing pain to course through your body.")
    print("You scream in agony, your cries echoing through the water, unheard by any potential saviors.")
    print("As the sea monsters continue their relentless assault, their grip tightens, restricting your movements.")
    print("Your futile struggle only hastens your demise, as their powerful muscles overwhelm your feeble resistance.")
    print("Your strength wanes, and your vision blurs, a mixture of blood and saltwater clouding your sight.")
    print("In your final moments, you realize there is no escape from this watery grave, no reprieve from their insatiable hunger.")
    print("With a final act of brutality, the sea monsters tear you apart, limb by limb, leaving nothing but a trail of blood in their wake.")
    print("Your treasure hunt ends in unspeakable tragedy, consumed by the merciless jaws of the deep sea.")
    print("Game over.")

elif choice3 == "rainbow":
    print("You open the door that shimmers like a rainbow and find yourself in a room of vibrant colors.")
    print("The air is filled with laughter and the scent of joy, luring you deeper into the enchanting space.")
    print("As you explore, the room suddenly shifts, and the vibrant colors turn dark and foreboding.")
    print("The laughter morphs into eerie whispers that send shivers down your spine.")
    print("You realize that you have stumbled into a cursed dimension, trapped in a malevolent realm.")
    print("From the shadows, grotesque and twisted creatures emerge, their eyes gleaming with sadistic delight.")
    print("They are the tormentors of dreams, reveling in the pain and suffering they inflict upon unsuspecting victims.")
    print("With each step, the creatures close in, their claws and fangs bared, thirsting for your anguish.")
    print("You try to fight back, but your efforts are feeble against their supernatural strength.")
    print("They tear into your flesh, rending your body apart while relishing in your agonized screams.")
    print("Blood spills across the darkened room, staining the once vibrant colors with a gruesome reminder of your demise.")
    print("Your pleas for mercy go unanswered, drowned out by the cruel laughter of the malevolent entities.")
    print("In your final moments, you are left broken and defeated, your hopes and dreams shattered.")
    print("As the creatures revel in their sadistic victory, your journey ends in a tragedy of unimaginable pain.")
    print("Game over.")

else:
    print("You open the yellow door and step into a room bathed in radiant golden light.")
    print("The air is filled with the soft tinkling of coins and the scent of opulence, creating an atmosphere of unparalleled grandeur.")
    print("As your eyes adjust to the dazzling brilliance, you realize you are surrounded by heaps of gleaming gold and precious jewels.")
    print("Each gemstone reflects the light in a kaleidoscope of colors, filling the room with a mesmerizing display.")
    print("You run your fingers through the cascading golden coins, feeling the weight of prosperity in your hands.")
    print("With each step, the floor beneath you resonates with a melodic symphony of abundance and success.")
    print("The treasures before you are a testament to the wealth and prosperity that await you, a reward for your unwavering determination.")
    print("Your heart fills with elation as you realize that you have found a fortune beyond your wildest dreams.")
    print("As you bask in the golden glow, you can't help but envision the possibilities that lie ahead.")
    print("With your newfound wealth, you can bring about positive change, fulfill lifelong aspirations, and make a difference in the world.")
    print("The golden room becomes a symbol of the infinite opportunities that await you, a springboard for a life of abundance and fulfillment.")
    print("Congratulations! You have emerged triumphant, unlocking a future filled with prosperity and joy.")
    print("Your journey ends with a well-deserved victory, as you step out of the room, carrying the golden glow of success within you.")
    print("Game over.")
    
