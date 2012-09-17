# Eliza (as a baby) - a very simply psychotherapist

# This program is modelled on the famous "Eliza" program by Joseph
# Weizenbaum, that mimics a psychotherapist.
#
# This is a highly simplistic version, but fun to play with.
#
# Written as a introductory demo to Python programming
# by Giovanni Moretti
#    Giovanni@reflections.co.nz
#    November 27, 2010
#------------------------------------------------------------------------
# For details of the original
#  see http://en.wikipedia.org/wiki/ELIZA
# For some really fun conversations, see:
#      http://megahal.alioth.debian.org/  
# esp. http://megahal.alioth.debian.org/Classic.html

#========================================================================
# HOW IT WORKS
# While the program can appear to carry on a conversation, it's a trick.
# The program looks for keywords and then responds either by modifying
# the user's reply e.g. "I'm tired" causes a response of "You're tired?"
# or particular words (e.g. mum) cause a related topic ("tell me about
# your family") to be raised, as do emotional words (sad, angry ...)  If
# no keywords are found, a generic reply designed to solicit more input
# is given: e.g. "I'm not sure I understand you fully"
#========================================================================
import random       # Need this for getting random numbers

#========================================================================
listOfFamilyMembers = ["Mum", "mother", "Dad", "father", "brother",
                       "sister", "niece", "nephew", "granddaughter",
                       "grandson", "child", "baby"]

previousFamilyMember = None      # Remember last family member mentioned

#========================================================================
# Generic responses for when no keywords are found

generalResponses = ["That's interesting, tell me more.",
                    "Are you sleeping well?",
                    "Do you have any disturbing dreams?",
                    "How did you imagine your life turning out?",
                    "Please carry on.",
                    "Are you happy with your life?",
                    "Do you like your job?",
                    "Does the world situation worry you?",
                    "Do you have many friends?",
                    "Are your relationships satisfying?",
                    "What sort of books do you read?",
                    "Do you have money worries?",
                    "How are you feeling now?",
                    "Why?",
                    "I'm not sure I understand you fully.",
                    "Is that the real reason?",
                    "Are you sure?",
                    "What does that suggest to you?",
                    "Why won't you talk about it?",
                    "Can you elaborate?",
		    "Please go into more detail."]

recentResponse = ""  # remember what we said so we don't repeat replies

#========================================================================
# A tiny function named to make it clear what it does:
# pick one option from the supplied list of responses and return it.

def pickOne (listOfOptions):
    option = random.choice(listOfOptions)   
    return option

#========================================================================
# Go through the supplied list of words, picking out a word at a time and
# see if it appears in the patient's reply.
# If a word is found in the reply, exit immediately and return the word.
# If none of the words are found, return None.

def findInReply(listOfWords, reply):
    """ Go through the list of words, picking out a word at a time and
    see if it appears in the patient's reply. If so, exit immediately
    and return the word.
    If none of the words in the list appear, return None."""
    
    for word in listOfWords:
       if word in reply:
         return word
    return None

#========================================================================
# Main Program Starts Here 
    
print "======================================================================="
print "I'm  Doctor Eliza."
print "English is not my first language, so please answer in single sentences."
print "======================================================================="
print "What is your most serious problem?"

lastReply = None
while True: 
    reply = raw_input()                   # Get the user's to reply

    if reply in ['bye', "quit", "exit"]:  # Finished?
        exit()                            # If so, exit the program
    #==========================================================================
    # Check for replies that are blank lines 

    if reply.strip() == "":        # use strip() to remove space/tabs
        print "Please talk to me."
        continue

    #==========================================================================
    if reply == lastReply:         # Same reply as last time?
        print "Please stop repeating yourself."
        continue                   # skip the rest, jump to while loop above

    lastReply = reply              # remember their reply for next time

    #==========================================================================
    # See if a family member is mentioned. If so, save who for later

    # Find the first family member mentioned in the reply (if anyone is)

    thisPerson = findInReply(listOfFamilyMembers, reply) 
    if thisPerson != None:               # a family member was found
        
       if previousFamilyMember != None:  # have they mentioned someone earlier?
           print "Did", thisPerson,"and", previousFamilyMember, "get on?"
       else:
           print pickOne(["Tell me about your family.",
                          "Were you happy as a child?",
                          "Did you have an imaginary friend?",
                          "How were your teenage years?",
                          "Did you feel loved",
                          "Did you parents get on?"])
       previousFamilyMember = thisPerson
       continue
    #==========================================================================
    # If they say "I want" (something), turn their reply into a question:
    # i.e. "I want XXX"" into "What would it mean to you if you got XXX"
    
    # Do the same for "I wanted" or "I need"    

    if "I want" in reply or "I wanted" in reply or "I need" in reply:
        reply = reply.replace("I wanted", "I want")  # Change both to 'I want'
        reply = reply.replace("I need"  , "I want")  # so code below works

        # Split the reply into the part before and after "I want"
        before, middle, after = reply.partition("I want")
        print "What would it mean to you if you got " + after + "?"
        continue

    #==========================================================================
    # Check for negative feelings
    negativeKeywords = ["don't like", "don't want", "sad", "hate",
                        "angry", "annoyed", "jealous", "disappointed",
                        "bitter", "frustrated", "depressed", "guilt",
                        "inadequate", "lonely"]

    emotionRelatedResponses = ["How long have you felt that way?",
                       "How do you think things could change?",
                       "Have you started drinking?",
                       "Does any particular person affect you badly?",
                       "Are you always this negative?",
                       "Do you believe in positive thinking?",
                       "Do you want to talk about it?",
                       "Do you think you're getting worse?",
                       "Do you watch much television?",
                       "What preys on your mind?",
                       "Does the world situation worry you?",
                       "Is that why you came to me?",
                       "Are you comfortable discussing your feelings?"]

    negativeFeeling = findInReply(negativeKeywords, reply)
    if negativeFeeling is not None:
        print pickOne(emotionRelatedResponses)
        continue         # Go back to the While and get their reply

    #==========================================================================
    # Don't let the patient focus on the therapist

    if findInReply(["you ", "your ", "you're", "?"], reply) != None:
        print pickOne(["We're discussing you, not me.",
                       "Why do you want to talk about me?",
                       "Could we focus on you.",
                       "Are you avoiding talking about yourself?"])
        continue

    #==========================================================================
    # Turn statements into questions
    # e.g. "I'm hungry"        -> "you're hungry?"
    #      "We chased the ferret" -> "You chased the ferret?"

    myReply = None
    if   "I am" in reply:  myReply = reply.replace( "I am" , "You are")
    elif "I'm"  in reply:  myReply = reply.replace( "I'm"  , "You're" )
    elif "I "   in reply:  myReply = reply.replace( "I "   , "You "   )
    elif " me " in reply:  myReply = reply.replace(" me "  , " You "  )
    elif " we " in reply:  myReply = reply.replace(" we "  , " You "  )

    if myReply != None:
        print myReply + "?"                     # Make it a question
        continue

    #==========================================================================
    # Nothing specific so ask a general question. Remember the most recent
    # general reponse so we don't say it twice in a row.

    genericReply = pickOne(generalResponses)     # Pick a response randomly
    
    while genericReply == recentResponse:        # If it's same as last time
        genericReply = pickOne(generalResponses) #  try again
        
    print genericReply
    recentResponse = genericReply                # Remember what we've said

    # End of the While loop. Go back and get the patient's reply        

        
