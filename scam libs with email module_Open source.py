#this is a scam email generator
#DISCLAIMER: YOU MUST ENTER YOUR EMAIL & PASSWORD INTO THE SOURCE CODE, it will NOT RUN if you don't do this. MUST BE GMAIL 
#YOU MUST FILL OUT *ONLY* LINES 165 AND 169 DIRECTLY IN THE SOURCE CODE PRIOR TO RUNNING THE SCRIPT.
#you also need to "enable less secure apps" on your gmail (you can disable right after) 
#this is completely safe!!

import time
#import datetime

#if datetime.datetime.now().minute % 2 == 0:

#function so that this can loop
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
                    print(       )
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
                
#WHERE SCRIPT FOR MAD LIBS STARTS:
                
#           Name = input("please re-enter your name: ")               
#           Celebrity = input("please re-enter name of Celebrity: ")
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
#           Email_provider = input("please enter an e-mail provider: ")
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
            
#this is saving the file to your computer as a text file called 'ScamLibs.txt'
            outfile = open('ScamLibs.txt','w') #'w'meant it will rewrite the file each time
            outfile.write(Greeting+" my dear "+Name+","+"\n\nIt's"+ Celebrity+" I am emailing you because I have a very important favor to ask."+
                          " I have recently come into a large inheritance from my late "+Family_member+","+"the sum of "+Amount_of_money+
                          "."+" However, my doctor told me recently that I have a serious sickness, "+Illness+". Because of this, I have "+
                          "decided to donate this fund to a very "+Adjective+" and "+Second_adjective+" person who can claim this money "+
                          "and use it for charitable causes, for "+Charity+", "+Second_charity+" and also to build schools for the less privileged that "+
                          "will be named after my late "+Family_member+" if possible, and to promote the word of "+Influential_figure+"."+"\n\n I do not "+
                          "want a situation where this money will be used in an "+Third_adjective+" manner. That's why I'm making "+
                          "this decision. I'm not afraid of "+Fear+" so I know I'm going to "+Heaven+". I accept this decision because I do "+
                          "not have any "+second_family_member+" who will inherit this money after I die. Please, I want your sincerity and urgent "+
                          "answer to know if you will be able to execute this project, and I will give you more information on how the "+
                          "fund will be transferred to your bank account. I am waiting for your reply. Please kindly reply me in my private "+
                          "e-mail "+Celebrity+"@"+Email_provider+".com"+"\n\n"+Farewell+"\n"+Celebrity+"\n")

            outfile.close()

            import time                                                                                    
            import email                        #This is a package containg a library for managing email messages. Specifically to aid in networking policies
            import smtplib                      #This module for sending emails within Python called Simple Mail Transfer Protocol
            import ssl                          #This module provides access to Secure socket layer (ssl) encryption and authentication
                                                #for network sockets. = Helps manage settings and certificates as well as encrypt and
                                                #decrypt the data going over the network's socket

            from email import encoders              #From email package, importing encoder module
            from email.mime.base import MIMEBase    
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            print()

            subject = 'I, '+Celebrity+', need your help'                      

            body = (Greeting+" my dear "+Name+","+"\n\nIt's "+ Celebrity+" I am emailing you because I have a very important favor to ask."+
                          " I have recently come into a large inheritance from my late "+Family_member+","+"the sum of "+Amount_of_money+
                          "."+" However, my doctor told me recently that I have a serious sickness, "+Illness+". Because of this, I have "+
                          "decided to donate this fund to a very "+Adjective+" and "+Second_adjective+" person who can claim this money "+
                          "and use it for charitable causes, for "+Charity+", "+Second_charity+" and also to build schools for the less privileged that "+
                          "will be named after my late "+Family_member+" if possible, and to promote the word of "+Influential_figure+"."+"\n\n I do not "+
                          "want a situation where this money will be used in an "+Third_adjective+" manner. That's why I'm making "+
                          "this decision. I'm not afraid of "+Fear+" so I know I'm going to "+Heaven+". I accept this decision because I do "+
                          "not have any "+second_family_member+" who will inherit this money after I die. Please, I want your sincerity and urgent "+
                          "answer to know if you will be able to execute this project, and I will give you more information on how the "+
                          "fund will be transferred to your bank account. I am waiting for your reply. Please kindly reply me in my private "+
                          "e-mail "+Celebrity+"@"+Email_provider+".com"+"\n\n"+Farewell+"\n"+Celebrity+"\n")       

#below, enter email address from which email will be SENT in quotations here. 
            celebrity_email = 'ENTER GMAIL ADDRESS HERE!' #fill this out BEFORE running the code! 
#the RECEIEVER EMAIL is the inbox where the EMAIL will be SENT TO. Can be the same address or different one 
            receiver_email = input('please enter your email (PLEASE SPELL CORRECTLY):  ') #don't change this                  
            print('Sending email from',Celebrity+"@"+Email_provider+".com...")
            sending_password = 'ENTER PASSWORD TO THAT GMAIL ADDRESS HERE' #fill this out BEFORE running the code! 

            message = MIMEMultipart()
            message['From'] = celebrity_email                                   #Each of these appears in the Gmail's
            message['To'] = receiver_email                                      #interface and needs to be written and 
            message['Subject'] = subject                                        #addressed for the program to work
            message['Bcc'] = receiver_email

            #message.attach(MIMEText(body, 'plain))
            message.attach(MIMEText(body))
            filename = 'ScamLibs.txt'

            with open(filename, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')                  #add file as application/octet-stream
                part.set_payload(attachment.read())

#sending binary files to an emailing server like Gmail's, they need to be encoded first before
#being transported. This is where the encoding function base64 comes from
#The following statements are used to attach the txtfile into the mail being sent to the receiver_email. 

            encoders.encode_base64(part)                                        #encoding function to set the header to be 
                                                                                #(part = MIMEbase)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            message.attach(part)
            text = message.as_string()
                
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:        #Used port 465
                server.login(celebrity_email, sending_password)
                server.sendmail(celebrity_email, receiver_email, text)

            initiating_send = ['1','2','3']                                     #Did a little bit of a visualization of
            for seconds in initiating_send:                                     #a loading screen to send the email.
                time.sleep(1)
                print(seconds, ". . .")
            print('check your spam folder')

          
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

#mad libs script to respond to the celebrity 
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
