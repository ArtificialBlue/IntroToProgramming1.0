#Chatbot

def 

def get_bot_response(user_response):

    dataSci = [["Math for Machine Learning: https://ocw.mit.edu/courses/mathematics/18-657-mathematics-of-machine-learning-fall-2015/",
    "Artificial Intelligence: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-spring-2005/index.htm",
    "Machine Vision: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-801-machine-vision-fall-2004/"],
    ["https://techdevguide.withgoogle.com/paths/machine-learning/","https://www.kaggle.com/learn/overview","https://aihub.cloud.google.com/u/0/s?category=notebook"],
    ["https://research.duolingo.com","2","3"]]
    webDev = [["Web-Applications Software Studio: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-170-software-studio-spring-2013/",
    "Computer Systems Security: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-858-computer-systems-security-fall-2014/index.htm",
    "Industry Database Course: https://ocw.mit.edu/courses/civil-and-environmental-engineering/1-264j-database-internet-and-systems-integration-technologies-fall-2013/"],
    ["https://www.khanacademy.org/computing/computer-programming",],
    ["Internship Links"]]
    mobileDev = [["React Native App Development: https://cs50.harvard.edu/mobile/2018/",
    "iOS App Development https://cs50.harvard.edu/x/2020/tracks/mobile/ios/",
    "Android App Development https://cs50.harvard.edu/x/2020/tracks/mobile/android/"],
    ["Other Useful Resources"],
    ["Internship Links"]]

    if user_response == "Data Science":
        return choice(dataSci)
  elif user_response == "Web Development":
        return choice(webDev)
  elif user_response == "Mobile Development":
        return choice(mobileDev)
  else:
    return "Input Not Recognized"



#Greet the user using print() statements and explain what the chat bot topic is and what kind of responses it expects.
print("Welcome to Computer Science ")
print("Please enter how you are feeling")

#Get user input using the input() function and pass that user input to the get_bot_response() function you will write

#Print out the chat bot’s response that is returned from the get_bot_response() function

#Use a while() loop to keep running your chat bot until the user enters "done".
