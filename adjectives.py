

str_taste="""
            Bitter Lemon-flavored Spicy Bland Minty Sweet Delicious Pickled Tangy Fruity Salty Tasty Gingery Sour  Yummy
        """
list_taste=[str_taste.split()]


str_touch="""
        Boiling Fluffy Sharp Breezy Freezing Silky Bumpy Fuzzy Slick Chilly Greasy

Slimy Cold Hard Slippery Cool Hot Smooth Cuddly Icy Soft Damp Loose Solid Dirty Melted Sticky Dry

Painful Tender Dusty Prickly Tight Encrusted Rough Uneven Filthy Shaggy Warm Flaky Shaky Wet
        """   
list_touch=[str_touch.split()]

        
str_sound="""
        Blaring Melodic Screeching Deafening

Moaning Shrill Faint Muffled Silent Hoarse Mute Soft High-pitched Noisy Squealing Hissing

Purring Squeaking Hushed Quiet Thundering Husky Raspy Voiceless Loud Resonant Whispering
        """
list_sound=[str_sound.split()]


str_color="""
Azure Gray Pinkish

Black Green Purple Blue Indigo Red Bright Lavender Rosy Brown Light Scarlet Crimson Magenta

Silver Dark Multicolored Turquoise Drab Mustard Violet Dull Orange White Gold Pink Yellow
        """  
list_color=[str_color.split()]



str_size="""
        Abundant Jumbo Puny Big-boned Large Scrawny Chubby Little Short Fat Long Small Giant Majestic Tall Gigantic

Mammoth Teeny Great Massive Thin Huge Miniature Tiny Immense Petite Vast
        """        
list_size=[str_size.split()]



str_shape="""
        Blobby Distorted Rotund Broad Flat Round Chubby Fluffy Skinny Circular Globular

Square Crooked Hollow Steep Curved Low Straight Cylindrical Narrow Triangular Deep Oval Wide
        """        
list_shape=[str_shape.split()]



str_time="""
        Annual Futuristic Rapid Brief Historical Regular Daily Irregular Short Early

Late Slow Eternal Long Speed Fast Modern Speedy First Old Swift Fleet Old-fashioned Waiting Future Quick Young
        """        
list_time=[str_time.split()]



str_amount="""
        All Heavy One Ample Hundreds Paltry Astronomical Large Plentiful Bountiful Light

Profuse Considerable Limited Several Copious Little Sizable Countless Many Some Each Measly

Sparse Enough Mere Substantial Every Multiple Teeming Few Myriad Ten Full Numerous Very
        """ 
list_amount=[str_amount.split()]



str_emotion="""
        Abrasive Embarrassed Grumpy Abrupt Energetic Kind Afraid Enraged Lazy Agreeable

Enthusiastic Lively Aggressive Envious Lonely Amiable Evil Lucky Amused Excited Mad Angry Exhausted

Manic Annoyed Exuberant Mysterious Ashamed Fair Nervous Bad Faithful Obedient Bitter Fantastic

Obnoxious Bewildered Fierce Outrageous Boring Fine Panicky Brave Foolish Perfect Callous Frantic

Persuasive Calm Friendly Pleasant Calming Frightened Proud Charming Funny Quirky Cheerful Furious Relieved Combative

Gentle Repulsive Comfortable Glib Rundown Defeated Glorious Sad Confused Good Scary Cooperative

Grateful Selfish Courageous Grieving Silly Cowardly Gusty Splendid Crabby Gutless Successful

Creepy Happy Tedious Cross Healthy Tense Cruel Heinous Terrible Dangerous Helpless Thankful

Defeated Hilarious Thoughtful Defiant Hungry Thoughtless Delightful Hurt Tired Depressed

Hysterical Troubled Determined Immoral Upset Disgusted Impassioned Weak Disturbed Indignant

Weary Eager Irate Wicked Elated Itchy Worried Embarrassed Jealous Zany Enchanting Jolly Zealous
        """        
list_emotion=[str_emotion.split()]




str_personality="""
        Aggressive

Famous

Restless

Agoraphobic

Fearless

Rich

Ambidextrous

Fertile

Righteous

Ambitious

Fragile

Ritzy

Amoral

Frank

Romantic

Angelic

Functional

Rustic

Brainy

Gabby

Ruthless

Breathless

Generous

Sassy

Busy

Gifted

Secretive

Calm

Helpful

Sedate

Capable

Hesitant

Shy

Careless

Innocent

Sleepy

Cautious

Inquisitive

Somber

Cheerful

Insane

Stingy

Clever

Jaunty

Stupid

Common

Juicy

Super

Complete

Macho

Swanky

Concerned

Manly

Tame

Crazy

Modern

Tawdry

Curious

Mushy

Terrific

Dead

Naughty

Testy

Deep

Odd

Uninterested

Delightful

Old

Vague

Determined

Open

Verdant

Different

Outstanding

Vivacious

Diligent

Perky

Wacky

Energetic

Poor

Wandering

Erratic

Powerful

Wild

Evil

Puzzled

Womanly

Exuberant

Real

Wrong
        """        
list_personality=[str_personality.split()]




str_appearance="""
            Ablaze

Distinct

Quirky

Adorable

Drab

Ruddy

Alluring

Dull

Shiny

Attractive

Elegant

Skinny

Average

Embarrassed

Sloppy

Awkward

Fancy

Smiling

Balanced

Fat

Sparkling

Beautiful

Filthy

Spotless

Blonde

Glamorous

Strange

Bloody

Gleaming

Tacky

Blushing

Glossy

Tall

Bright

Graceful

Thin

Clean

Grotesque

Ugly

Clear

Handsome

Unattractive

Cloudy

Homely

Unbecoming

Clumsy

Interior

Uncovered

Colorful

Lovely

Unsightly

Confident

Magnificent

Unusual

Cracked

Murky

Watery

Crooked

Old-fashioned

Weird

Crushed

Plain

Wild

Curly

Poised

Wiry

Cute

Pretty

Wooden

Debonair

Puffy

Worried

Dirty

Quaint

Zaftig
            """        
list_appearance=[str_appearance.split()]





str_situations="""
Accidental

Doubtful

Main

Achievable

Elementary

Minor

Advantageous

Finger-printed

Nasty

Alcoholic

Groundless

Nutritious

Animated

Hard

Obsolete

Aquatic

Harmful

Optimal

Aromatic

High

Organic

Aspiring

Honest

Premium

Bad

Horrible

Quizzical

Bawdy

Illegal

Rainy

Biographical

Illegible

Redundant

Bizarre

Imperfect

Remarkable

Broken

Impossible

Simple

Careful

Internal

Tangible

Credible

Inventive

Tricky

Creepy

Jazzy

Wholesale

Cumbersome

Juvenile

Worse

Disastrous

Legal

Wry

Dismissive

Logical

X-rated
            """
list_situations=[str_situations.split()]






list_adjectives=list_taste+list_touch+list_sound+list_color+list_size+list_shape+list_time+list_amount+list_emotion+list_personality+list_appearance+list_situations

print(list_adjectives)