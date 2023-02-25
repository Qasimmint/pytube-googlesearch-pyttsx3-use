import random,pyttsx3,collections,wikipedia,googlesearch,time as t

class Tech_4:
    def __init__(self):
        print("*****************************\n\n Welcom to Tech_4.0\n\n Here you can access to our differenct services")
        while True:
            self.register = input("press q to start registeration: ")
            if self.register.lower() == 'q':
                self.registeration()  
            else:
                print("Enter the vaid key")
                print(self.register)

    def registeration(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

        while True:
            self.email = input("Enter your email: ")
            cond = "email.com" or "gmail.com"
            if cond in self.email:
                print(f"Hi {self.name.capitalize()} You have been successfully verified.\n Now You can enjoy our services.")
                self.services()
            else:
                print("email is invalid",self.email)
                
    def gooGle(self,greet):
        self.greet = greet
        self.query = input(f"{self.greet} \n Search Here: ")
        for url in googlesearch.search(self.query):
            print("Here are your results\n","-->",url)
        
    def converter(self):
        self.grt = f"Welcom Mr.{self.name.capitalize()} to your pedia\n type the text below to convert that into speech"
        self.talk = pyttsx3.init()
        voice = self.talk.getProperty('voices')
        vocal = int(input("chose voice {'0':'Male','1':'Female'}"))
        if vocal == 1:
            self.talk.setProperty('voice',voice[1].id)
        elif vocal == 0:
            self.talk.setProperty('voice',voice[0].id)
        else:
            print("inappropriate number")

        set_vol = int(input("set the volume between 0 and 1 :"))
        if set_vol in range(0,2):
            self.talk.setProperty('volume',set_vol)
        else:
            print("NOTE you can only chose between 1 and 0")

        self.speech = input("Enter text: ")
        self.talk.say(self.speech)
        self.talk.runAndWait()

    def wiki(self,query,sentence=4):
        self.sen = sentence
        self.query = query
        print(f"Hi, Mr.{self.name.capitalize()}, Welcome to Your pedia")
        sentence = input("how much sentences you want: ")
        pedia = wikipedia.summary(self.query,sentences=sentence)
        print(pedia,end="")

    def play(self):
        self.name = input("what's your name: ")
        self.merit = input("your bold merit: ")
        self.love = input("whom you love the most: ")
        self.subject = input("Your favorite subject: ")
        rep_n=self.name.replace(self.name, "fool")
        choices = ["lazy",'Crazy',"bad apple","couch potato","watching TV"]
        merit = random.choice(choices)
        rep_cho=self.merit.replace(self.merit, merit)
        madlibs = (f"My name is {rep_n}. My only quality is that i am {rep_cho}. I only love {self.love}\n My favorite subject is {self.subject}.") 
        print("Here i am going to introduce myself with just, all i have said is aboslutely right\n",madlibs)
        
                
    def services(self):
        self.tupname = collections.namedtuple('Services',['Googlesearching','WikipediaExploring','TextSpeechconversions','playingmadlibsrandomly'])
        self.tup = self.tupname("search","Explore","conversion","playing")
        self.service = input(f"{self.tup}\ntype the corresponding word to enjoy a certain service:")

        if self.service.lower() == 'search':
            self.gooGle(f"Welcome Mr.{self.name.capitalize()} to Your own Private Google search engine.")

        elif self.service.lower() == 'explore':
            self.converter()

        elif self.service.lower() == 'conversion':
            self.wiki(input("Type Here: "))
        
        elif self.service.lower() == 'playing':
            self.play()

        else:
            print("Enter a valid key")

t = Tech_4()