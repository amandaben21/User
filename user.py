class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"First: {self.first_name}")
        print(f"Last: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age} years old!")
        print(f"Is a member: {self.is_rewards_member}")
        print(f"Current Points:{self.gold_card_points}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def enroll(self):
        if self.is_rewards_member:
            print("Already a memeber!")
            return False

        #set to true
        self.is_rewards_member = True

        #set to 200
        self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points < amount:      #we put an if statement 1st b/c we dont want the points to show negative
            print(f"You dont't have enough points to spend {amount}, below you will see your current points")
            return #stop running

        self.gold_card_points = self.gold_card_points - amount


amanda = User("Amanda", "Contreras", "xyz@gmail.com", 100)
toby = User("Toby", "Benitez", "abc@gmail.com", 50)
hunter = User("Hunter", "Love", "efg@gmail.com", 20)

########################################################

amanda.display_info() #shows before enrolling
amanda.enroll() #enroll the user
amanda.display_info() #after enrollment 

amanda.spend_points(50) #user spent 50 points
amanda.display_info() #display after points should be 150

#############################################################

toby.display_info()
toby.enroll()
toby.spend_points(800) #I put 800 because i wanted to see the message
toby.display_info()

##############################################################
