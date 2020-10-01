#Chatbot
from random import choice

def chooseResourceType(user_response):
    if user_response == "OpenCourseWare":
        return 0
    else:
        return 1



def get_bot_response(user_response):

    dataSci = [["Math for Machine Learning: https://ocw.mit.edu/courses/mathematics/18-657-mathematics-of-machine-learning-fall-2015/",
    "Artificial Intelligence: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-spring-2005/index.htm",
    "Machine Vision: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-801-machine-vision-fall-2004/"],
    ["https://techdevguide.withgoogle.com/paths/machine-learning/","https://www.kaggle.com/learn/overview","https://aihub.cloud.google.com/u/0/s?category=notebook"]
    ]
    webDev = [["Web-Applications Software Studio: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-software-studio-spring-2013/",
    "Computer Systems Security: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-858-computer-systems-security-fall-2014/index.htm",
    "Industry Database Course: https://ocw.mit.edu/courses/civil-and-environmental-engineering/1-264j-database-internet-and-systems-integration-technologies-fall-2013/"],
    ["https://www.khanacademy.org/computing/computer-programming","https://andreasbm.github.io/web-skills/","https://www.reddit.com/r/webdev/wiki/faq"]]
    mobileDev = [["React Native App Development: https://cs50.harvard.edu/mobile/2018/",
    "iOS App Development https://cs50.harvard.edu/x/2020/tracks/mobile/ios/",
    "Android App Development https://cs50.harvard.edu/x/2020/tracks/mobile/android/"],
    ["Modern iPhone App Development Tutorial: https://www.youtube.com/watch?v=hwkL_jNWCBw", "Info on App Frameworks: https://www.youtube.com/watch?v=4m7msadL5iA"]]

    concentrationChoice = user_response
    
    resourceTypeChoice = raw_input("Choose from OpenCourseWare or General: ")

    if user_response == "Data Science":
        return choice(dataSci[chooseResourceType(resourceTypeChoice)])
    elif user_response == "Web Development":
        return choice(webDev[chooseResourceType(resourceTypeChoice)])
    elif user_response == "Mobile Development":
        return choice(mobileDev[chooseResourceType(resourceTypeChoice)])
    else:
        return "Input Not Recognized"



#Greet the user using print() statements and explain what the chat bot topic is and what kind of responses it expects.
while True:
    print("-----------------------------------------")
    print("Welcome to Computer Science Resource Bot")
    print("Please enter which Concentration you'd like resources from, from the following selection:")
    #Get user input using the input() function and pass that user input to the get_bot_response() function you will write
    user_input = raw_input("Data Science, Web Development, or Mobile Development: ")
    if user_input == "done":
        break
    bot_response = get_bot_response(user_input)
    #Print out the chat bots response that is returned from the get_bot_response function
    print(bot_response)
    #Use a while() loop to keep running your chat bot until the user enters "done".
