
import time
#import datetime

    #if datetime.datetime.now().minute % 2 == 0:
def script():
            
            
            Name = input("please enter your name: ")
            URL = input("please enter a URL: ") 
            Exclamation = input("please enter a common exclamation: " ) 
            Webpage_component = input("please enter a common thing you may see on a webpage: ")
            Number_of_emails = input("please enter a number: ")
            Ordinal_number = input("please enter an ordinal number (ex: 1st, 2nd, 3rd, 81st...): ")
            Celebrity = input("please enter a celebrity: ") 
            Dessert = input("please enter a dessert (plural): ")
            Email_provider = input("please enter an e-mail provider: ")
            Another_number = input("please enter another number: ")
            Second_exclamation = input("please enter another exclamation: ")

            print(           )

            print("As",Name,"was surfing The Web one night, they came across the website",URL,".A"\
              " little dialogue box opens up.",Name,"reads it aloud:")
            print(           )
            print("This website uses",Dessert,"in order to offer you the most relevant information."\
              " Please accept",Dessert,"for optimal performance.")

            print(           )

#do you want to accept cookies dialogue box 
            Accept = input("do you want to accept " + Dessert +"? Enter 'Y' for yes to accept or"\
               "'N' for NO to change settings: ")
            if Accept == "Y" or Accept == "y":
                    print(       )
                    print("Great, back to",URL,Name,"thought.",Exclamation,"they thought. I wonder what"\
                      ,Webpage_component,"I will find on here. But first, let me check my e-mail. I have"\
                      ,Number_of_emails,"new messages!",Name,"clicked on the",Ordinal_number,"one. It was from"\
                      ,Celebrity,"@",Email_provider,".com")
            else:
                    print("that's a shame")
                    print(       )
                    print("Great, back to",URL,Name,"thought.",Exclamation,"they thought. I wonder what"\
                      ,Webpage_component,"I will find on here. But first, let me check my e-mail. I have"\
                      ,Number_of_emails,"new messages!",Name,"clicked on the",Ordinal_number,"one. It was from"\
                      ,Celebrity,"@",Email_provider,".com")

            print(             )

#do you want to open Celebrity e-mail?
            question = input("do you want to open the e-mail from " + Celebrity + "? Enter 'Y' for"\
                         " YES or 'N' for NO: ")
            if question == "Y"or question == "y":
                print()
                print("great! But in order to unlock this e-mail from", Celebrity," you have to answer a few questions: ")
            else:
                print()
                print("hmm. Are you sure about that? I think",Celebrity," could really use your help.")
#WHERE SCRIPT FOR MAD LIBS STARTS: (copy and pasted directly instead of importing the module)
#            Name = input("please re-enter your name: ")               
#            Celebrity = input("please re-enter name of Celebrity: ")
            Greeting = input("please enter a Greeting: ")
            Family_member = input("please enter a family member: ")
            Amount_of_money = input("please enter an amount of money: ")
            Illness = input("please enter an illness: ")
            Adjective = input("please enter an adjective: ")
            Second_adjective = input("please enter another adjective: ")
            Charity = input("please enter a cause for which you might donate money: ")
            Second_charity = input("please enter another cause: ")
            Influential_figure = input("please enter an Influential figure: ")

            Third_adjective = input("please enter another adjective: ")
            Fear = input("please enter something you are afraid of: ")
            Heaven = input("please enter a place you go when you die: ")
            second_family_member= input("please enter another type of family member: ")
#            Email_provider = input("please enter an e-mail provider: ")
            Movie = input("please enter a movie title: ")
            Adjective2 = input("please enter another adjective: ")
            Verb = input("please enter a verb: ")
            Location = input("please enter a location: ")

            Farewell = input("please enter a common goodbye phrase: ")


            print(     )


            print(Greeting,"my dear",Name,"")
            print(              )

            print("It's",Celebrity,"I am emailing you because I have a very important favor to ask. "
                          "I have recently come into a large inheritance from my late",Family_member,",""the sum of",Amount_of_money,
                          ".""However, my doctor told me recently that I have a serious sickness,",Illness,". Because of this, I have "
                          "decided to donate this fund to a very",Adjective,"and",Second_adjective,"person who can claim this money "
                          "and use it for charitable causes, for",Charity,Second_charity,"and also to build schools for the less privileged that "
                          "will be named after my late",Family_member,"if possible, and to promote the word of",Influential_figure,".")
            print(              )
            print("I do not want a situation where this money will be used in an",Third_adjective,"manner. That's why I'm making "
                          "this decision. I'm not afraid of",Fear," so I know I'm going to",Heaven,". I accept this decision because I do "
                          "not have any",second_family_member,"who will inherit this money after I die. Please, I want your sincerity and urgent "
                          "answer to know if you will be able to execute this project, and I will give you more information on how the "
                          "fund will be transferred to your bank account. I am waiting for your reply. Please kindly reply me in my private "
                          "e-mail",Celebrity,"@",Email_provider,".com")
            print(Farewell)
            print(Celebrity)

            print()
            print()


          
            print(              )

                      
#do you want to send the money that celebrity requested? 
            question_2 = input(Second_exclamation + ". It seems like " + Celebrity + " is in desperate need of "\
                   "your help. Do you want to send " + Celebrity +" "+ Amount_of_money + "? Enter 'Y'"\
                   "for yes or 'N' for NO.")
            if question_2 == "N" or question_2 == "n":
                print()
                print("That's too bad. Now,",Celebrity,"will suffer from",Illness,". As you know,"\
                  "only",Another_number, "of people survive",Illness,".")
    
            if  question_2 == "Y" or question_2 == "y":
                print (         )
                print ("it's wonderful news that you want to help",Celebrity,". After all, their performance in",Movie,\
                   "was",Adjective2,". Especially the part where they",Verb,"to",Location,"." )
                print()

                follow_up = input("Please enter your Credit Card Number below:")
                if follow_up == float:
                        print ("Thanks!")
                else:
                        print()
                        print("hmm. That does not appear to be a Credit Card Number.")
                        print()
    
                Routing_Number = input("want to try again? Type 'Y' for yes or 'N' for no.")
                if Routing_Number == "N" or Routing_Number == "n":
                        print()
                        print("That's too bad. Now,",Celebrity,"will suffer from",Illness,". As you know,"\
                          "only",Another_number,"of people survive",Illness,".")
                        print()
                        print()

            Get_Well = input("want to at least send "+ Celebrity+" a feel better card? Enter Y for yes.")
            print()                       
    
            print (Name, ":")

            Second_Greeting = input("please enter another greeting: ")
            Organ = input("please enter an Organ: ")
            Group_of_people = input("please enter a group of people: ")
            Feeling = input("please enter a feeling in past-tense: ")
            Art_form = input("please enter any art form: ") #followed by 'project'
            Email_Ending = input("please enter a way you might end an e-mail: ")

            print(                          )
            print(Second_Greeting,Celebrity,)
            print(                          )

            print("I am so sorry to hear that you have",Illness,". My",Organ," goes out to you and your"
                  ,Group_of_people,"I would love to help out and send you",Amount_of_money,".")
            print(                          )
            print("By the way, I",Feeling,"your performance in",Movie,". Are you in any upcoming",Art_form,\
                  "that I can see?")

            print(                          )
            print(Email_Ending,",")
            print(Name)
            print()
            print()
            print()
            print()
            print()
            print()

            script()
script()
    #time.sleep(60)

           
    
    
