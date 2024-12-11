import tkinter as tk

window = tk.Tk()
window.title("Personality Quiz")

##################################################################################

#MISC THINGS NEEDED BEFOREHAND

zero_value = 0

one_value = 1

neg_one_value = -1


total_ext_int_score = []
total = 0

def add_to_total(value):
    total_ext_int_score.append(value)

def subtract_from_total(value):
    total_ext_int_score.remove(value)

def calculate_score():
    total = 0
    for x in total_ext_int_score:
        total = total+x
    print(total_ext_int_score)
    print(total)
    return total

def reverse_button(button,value):
    subtract_from_total(value)
    button.config(relief = "raised", command = lambda: (pressed_button(button,value)))
    print(total_ext_int_score)

def pressed_button(button,value):
    add_to_total(value)
    button.config(relief="sunken", command = lambda: (reverse_button(button,value)))
    print(total_ext_int_score)



def personality_type():
    while True:
        if -18 <= calculate_score() <= -12:
            #print("extreme introvert")
            return "extreme introvert"
            
        elif -11 <= calculate_score() <= -5:
            #print("a moderate introvert")
            return "a moderate introvert"
            
        elif -4 <= calculate_score() <= 4:
            #print("I am an Ambivert")
            return "I am an Ambivert"
            
        elif 5 <= calculate_score() <= 11:
            #print("moderate extrovert")
            return "moderate extrovert"
            
        elif 12 <= calculate_score() <= 18:
            #print("an Extreme extrovert")
            return "an Extreme extrovert"
            
class Person:
    def __init__(self,fname, lname, age, major):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.major = major
    
    def __str__(self):
        return f"{self.fname} {self.lname} \nAge: {self.age} \nMajor: {self.major}"

def get_demographics():
    p1 = Person(fname_entry.get(), lname_entry.get(), age_entry.get(), major_entry.get())
    print(p1)
    return p1


###################################################################################

#EVERYTHING TO DO WITH THE WELCOME PAGE

page_welcome = tk.Frame(
    master=window, 
    width=790, 
    height=600, 
    bg="light grey"
)



welcome = tk.Label(
    master=page_welcome,
    text= "Welcome! \n Please fill out the information \nthen press the button below to begin your Personality Quiz Journey:",
    bg= "light grey",
    font=12
)
def start_to_p1():
    page_welcome.destroy()
    page_1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


fname_label = tk.Label(
    text="First Name:",
    bg="light grey",
    font=8
)
fname_entry = tk.Entry(

)
lname_label = tk.Label(
    text="Last Name:",
    bg="light grey",
    font=8
)
lname_entry = tk.Entry(

)
age_label = tk.Label(
    text="Age:",
    bg="light grey",
    font=8
)
age_entry = tk.Entry(
)

major_label = tk.Label(
    text="College Major:",
    bg="light grey",
    font=8
)
major_entry = tk.Entry(
)

start = tk.Button(
    master=page_welcome,
    text="Begin",
    command=lambda: (get_demographics(),start_to_p1()) 
)

page_welcome.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
fname_label.place(x= 300, y= 120)
fname_entry.place(x=300, y= 140)
lname_label.place(x= 300, y=170)
lname_entry.place(x=300, y=190)
age_label.place(x=300, y=220)
age_entry.place(x=300, y=240)
major_label.place(x=300, y=270)
major_entry.place(x=300, y=300)
welcome.place(x= 130, y= 50)

start.place(x=340, y=350)

#####################################################################################

#EVERYTHING TO DO WITH PAGE 1 OF QUESTIONS

page_1 = tk.Frame(
    master=window, 
    width=750, 
    height=750, 
    bg="light grey"
)
question_labels_1 = tk.Frame(
    master=page_1,
    bg="light grey",
    width=790, 
    height=600,
)
answers_labels_1 = tk.Frame(
    master=page_1,
    bg="light grey",
    width=500, 
    height=510,
)

def one_to_two():
    page_1.destroy()
    page_2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Next_p1 = tk.Button(
    master=question_labels_1,
    text="Next",
    command=one_to_two
)

Question_1 = tk.Label(                  
    master=question_labels_1,
    text= "1. When a stranger talks to me, I consider it an opportunity to make a connection?",
    bg= "light grey",
    font = 12
)
q1_a1 = tk.Button(                      #Assigning a neutral value of 1 to this answer
    master= question_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command= lambda: pressed_button(q1_a1, one_value)
)
q1_a2 = tk.Button(                      #Assigning a positive value of 0 to this answer
    master=question_labels_1,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q1_a2, zero_value)
)

q1_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=question_labels_1,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q1_a3, neg_one_value)
)



Question_2 = tk.Label(               
    master=question_labels_1,
    text= "2. Being out with a big group of friends all night can be exhausting.",
    bg= "light grey",
    font = 12
)
q2_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master=question_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q2_a1, neg_one_value)
)

q2_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_1,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q2_a2, zero_value)
)
q2_a3 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_1,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q2_a3, one_value)
)

Question_3 = tk.Label(                 
    master=question_labels_1,
    text= "3. I consider myself to be an assertive person.",
    bg= "light grey",
    font = 12
)
q3_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q3_a1, one_value)
)
q3_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_1,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q3_a2, zero_value)
)
q3_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=question_labels_1,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q3_a3, neg_one_value)
)

Question_4 = tk.Label(                 
    master=question_labels_1,
    text= "4. It’s not unusual for me to get lost in thought around other people.",
    bg= "light grey",
    font = 12
)
q4_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master=question_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q4_a1, neg_one_value)
)
q4_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_1,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q4_a2, zero_value)
)
q4_a3 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_1,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q4_a3, one_value)
)
Question_5 = tk.Label(                  
    master=question_labels_1,
    text= "5. I think that being on a reality show would be a nightmare.",                
    bg= "light grey",
    font = 12
)
q5_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master=question_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q5_a1, neg_one_value)
)
q5_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_1,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q5_a2, zero_value)
)
q5_a3 = tk.Button(                      #Assigning a value of 1 to this answer
   master=question_labels_1,
   text="Disagree.",
   bg= "grey",
   command=lambda: pressed_button(q5_a3, one_value)
)

Question_6 = tk.Label(                  
    master=question_labels_1,
    text= "6. I don’t mind talking about anything, even if I’m not that knowledgeable about it.",
    bg= "light grey",
    font = 12
    )

q6_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q6_a1, one_value)
)
q6_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_1,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q6_a2, zero_value)
)
q6_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=question_labels_1,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q6_a3, neg_one_value)
)


question_labels_1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#answers_labels_1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True,)

Question_1.place(x= 0, y= 0)
q1_a1.place(x=100, y=30)
q1_a2.place(x=160, y=30)
q1_a3.place(x=250, y=30)

Question_2.place(x= 0, y= 90)
q2_a1.place(x=100, y=120)
q2_a2.place(x=160, y=120)
q2_a3.place(x=250, y=120)

Question_3.place(x= 0, y= 180)
q3_a1.place(x=100, y=210)
q3_a2.place(x=160, y=210)
q3_a3.place(x=250, y=210)

Question_4.place(x= 0, y= 270)
q4_a1.place(x=100, y=300)
q4_a2.place(x=160, y=300)
q4_a3.place(x=250, y=300)

Question_5.place(x= 0, y= 360)
q5_a1.place(x=100, y=390)
q5_a2.place(x=160, y=390)
q5_a3.place(x=250, y=390)

Question_6.place(x= 0, y= 450)
q6_a1.place(x=100, y=480)
q6_a2.place(x=160, y=480)
q6_a3.place(x=250, y=480)

Next_p1.place(x=160, y= 530)

##########################################################################################################

#EVERYTHING TO DO WITH PAGE 2 OF QUESTIONS

page_2 = tk.Frame(
    master=window, 
    width=750, 
    height=750, 
    bg="light grey"
)
question_labels_2 = tk.Frame(
    master=page_2,
    bg="light grey",
    width=790, 
    height=600,
)
answers_labels_2 = tk.Frame(
    master=page_2,
    bg="light grey",
    width=500, 
    height=510,
)
def two_to_three():
    page_2.destroy()
    page_3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Next_p2 = tk.Button(
    master=question_labels_2,
    text="Next",
    command=two_to_three
)

Question_7 = tk.Label(                  
    master=question_labels_2,
    text= "7. I'd rather spend one-on-one time with a close friend than get together with a friend group.",
    bg= "light grey",
    font = 12
)
q7_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master= question_labels_2,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command= lambda: pressed_button(q7_a1, neg_one_value)
)
q7_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q7_a2, zero_value)
)
q7_a3 = tk.Button(                      #Assigning a value to 1 to this answer
    master=question_labels_2,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q7_a3, one_value)
)

Question_8 = tk.Label(                
    master=question_labels_2,
    text= "8. It's better to have a roommate than to live alone.",
    bg= "light grey",
    font = 12
)
q8_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_2,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q8_a1, one_value)
)
q8_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q8_a2, zero_value)
)
q8_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=question_labels_2,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q8_a3, neg_one_value)
)

Question_9 = tk.Label(                  
    master=question_labels_2,
    text= "9. It's disappointing to review my weekly schedule and see that it includes no social plans.",
    bg= "light grey",
    font = 12
)
q9_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_2,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q9_a1, one_value)
)
q9_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q9_a2, zero_value)
)
q9_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=question_labels_2,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q9_a3, neg_one_value)
)

Question_10 = tk.Label(          
    master=question_labels_2,
    text= "10. At work meetings I think it's important to speak up often.",
    bg= "light grey",
    font = 12
)
q10_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_2,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q10_a1, one_value)
)
q10_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q10_a2, zero_value)
)
q10_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=question_labels_2,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q10_a3, neg_one_value)
)

Question_11 = tk.Label(                
    master=question_labels_2,
    text= "11. I have a lot of fun playing tricks on my friends and family.",
    bg= "light grey",
    font = 12
)
q11_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_2,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q11_a1, one_value)
)
q11_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q11_a2, zero_value)
)
q11_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=question_labels_2,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q11_a3, neg_one_value)
)

Question_12 = tk.Label(                 
    master=question_labels_2,
    text= "12. I like to get my friends and co-workers excited about our plans.",
    bg= "light grey",
    font = 12
)
q12_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_2,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q12_a1, one_value)
)
q12_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q12_a2,zero_value)
)
q12_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=question_labels_2,
    text="Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q12_a3, neg_one_value)
)

question_labels_2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#answers_labels_2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Question_7.place(x= 0, y= 0)
q7_a1.place(x=100, y=30)
q7_a2.place(x=160, y=30)
q7_a3.place(x=250, y=30)

Question_8.place(x= 0, y= 90)
q8_a1.place(x=100, y=120)
q8_a2.place(x=160, y=120)
q8_a3.place(x=250, y=120)

Question_9.place(x= 0, y= 180)
q9_a1.place(x=100, y=210)
q9_a2.place(x=160, y=210)
q9_a3.place(x=250, y=210)

Question_10.place(x= 0, y= 270)
q10_a1.place(x=100, y=300)
q10_a2.place(x=160, y=300)
q10_a3.place(x=250, y=300)

Question_11.place(x= 0, y= 360)
q11_a1.place(x=100, y=390)
q11_a2.place(x=160, y=390)
q11_a3.place(x=250, y=390)

Question_12.place(x= 0, y= 450)
q12_a1.place(x=100, y=480)
q12_a2.place(x=160, y=480)
q12_a3.place(x=250, y=480)

Next_p2.place(x=160, y= 530)

###################################################################################################################

#EVERYTHING TO DO WITH PAGE 3 OF QUESTIONS

page_3 = tk.Frame(
    master=window, 
    width=750, 
    height=750, 
    bg="light grey"
)
question_labels_3 = tk.Frame(
    master=page_3,
    bg="light grey",
    width=790, 
    height=600,
)
answers_labels_3 = tk.Frame(
    master=page_3,
    bg="light grey",
    width=500, 
    height=510,
)
def three_to_four():
    page_3.destroy()
    page_4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


Next_p3 = tk.Button(
    master=question_labels_3,
    text="Next",
    command= lambda: (three_to_four(), calculate_score(), personality_type())
)

Question_13 = tk.Label(                 
    master=question_labels_3,
    text= "13. I don't like to feel pushed into dancing at parties.",
    bg= "light grey",
    font = 12
)
q13_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master= question_labels_3,
    text= "Agree.",
    relief= "raised",
    bg= "grey",
    command= lambda: pressed_button(q13_a1, neg_one_value)
)
q13_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_3,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q13_a2, zero_value)
)

q13_a3 = tk.Button(   
    master=question_labels_3,                   #Assigning a value of 1 to this answer
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q13_a3, one_value)
)



Question_14 = tk.Label(                
    master=question_labels_3,
    text= "14. When I'm in charge, I prefer meeting with people one-on-one to holding large brainstomring sessions.",
    bg= "light grey",
    font = 12
)
q14_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master=question_labels_3,
    text= "Agree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q14_a1, neg_one_value)
)

q14_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_3,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q14_a2, zero_value)
)
q14_a3 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_3,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q14_a3, one_value)
)

Question_15 = tk.Label(                 
    master=question_labels_3,
    text= "15. When I go to a party, I often think about how early it would be approproiate to leave.",
    bg= "light grey",
    font = 12
)
q15_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master=question_labels_3,
    text= "Agree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q15_a1, neg_one_value)
)
q15_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_3,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q15_a2, zero_value)
)
q15_a3 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_3,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q15_a3, one_value)
)

Question_16 = tk.Label(                
    master=question_labels_3,
    text= "16. If someone is interesting enough, I could happily spend an evening just listening to their stories.",
    bg= "light grey",
    font = 12
)
q16_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_3,
    text= "Agree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q16_a1, one_value)
)
q16_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_3,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q16_a2, zero_value)
)
q16_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=question_labels_3,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q16_a3, neg_one_value)
)

Question_17 = tk.Label(                 
    master=question_labels_3,
    text= "17. In work or in life, I'd rather take some time to consider the next steps even if others are eager to rush ahead.",
    bg= "light grey",
    font = 12
)
q17_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master=question_labels_3,
    text= "Agree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q17_a1, neg_one_value)
)
q17_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_3,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q17_a2, zero_value)
)
q17_a3 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_3,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q17_a3, one_value)
)

Question_18 = tk.Label(                 
    master=question_labels_3,
    text= "18. As a kid, I was always the first to volunteer to read aloud.",
    bg= "light grey",
    font = 12
)
q18_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=question_labels_3,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q18_a1, one_value)
)
q18_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=question_labels_3,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q18_a2, zero_value)
)
q18_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=question_labels_3,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q18_a3, neg_one_value)
)

question_labels_3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#answers_labels_3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Question_13.place(x= 0, y= 0)
q13_a1.place(x=100, y=30)
q13_a2.place(x=160, y=30)
q13_a3.place(x=250, y=30)

Question_14.place(x= 0, y= 90)
q14_a1.place(x=100, y=120)
q14_a2.place(x=160, y=120)
q14_a3.place(x=250, y=120)

Question_15.place(x= 0, y= 180)
q15_a1.place(x=100, y=210)
q15_a2.place(x=160, y=210)
q15_a3.place(x=250, y=210)

Question_16.place(x= 0, y= 270)
q16_a1.place(x=100, y=300)
q16_a2.place(x=160, y=300)
q16_a3.place(x=250, y=300)

Question_17.place(x= 0, y= 360)
q17_a1.place(x=100, y=390)
q17_a2.place(x=160, y=390)
q17_a3.place(x=250, y=390)

Question_18.place(x= 0, y= 450)
q18_a1.place(x=100, y=480)
q18_a2.place(x=160, y=480)
q18_a3.place(x=250, y=480)

Next_p3.place(x=160, y= 530)

#################################################################################################################

#EVERYTHING TO DO WITH THE RESULTS PAGE

page_4 = tk.Frame(
    master=window, 
    width=1000, 
    height=600, 
    bg="light grey"
)
def close():
    window.destroy()

def explanation():
    results.place_forget()
    results.config(
        text="finish",
        command= lambda: close()
    )
    command = personality_type()
    demographics = tk.Label(
        bg = "light grey",
        font=12,
        text=get_demographics()
    )
    exp_of_results = tk.Label(
        master=page_4,
        bg="light grey",
        font=12
    )
    match command: 
        case "extreme introvert":
            exp_of_results.config(text="You scored highly introverted. \nThis means that being around people drains your energy, \nyou enjoy solitude, you have a small group of close friends, people might find it difficult to get to know you, \ntoo much stimulation leaves you feeling distracted, you are very self- aware, and you tend to be more independent. ")
            exp_of_results.place(x=40, y=270)
            demographics.place(x=215, y= 200)
            results.place(x= 480, y= 400)
        case "a moderate introvert":
            exp_of_results.config("You scored moderately introverted. \nThis means that being around people can drain your energy, you prefer solitude to a crowd,\n you might have a smaller group of friends. You prefer to do things on your own. ")
            exp_of_results.place(x=40, y=270)
            demographics.place(x=215, y= 200)
            results.place(x= 365, y= 400)
        case "I am an Ambivert":
            exp_of_results.config(text="You scored as ambient which is the range between an introvert and an extrovert. \nThis means that you’re a good listener and communicator, You have an ability to regulate behavior, \nYou feel comfortable in social settings, but also value your alone time, Empathy comes naturally to you, You’re able to provide balance")
            exp_of_results.place(x=40, y=270)
            demographics.place(x=215, y= 200)
            results.place(x= 480, y= 400)
        case "moderate extrovert":
            exp_of_results.config(text="You scored as moderately extroverted. \nThis means that being around people can energize you, you prefer to solve problems through discussion, \noften described as friendly/approachable, usually enjoys conversing with people, tends to think out loud.")
            exp_of_results.place(x=40, y=270)
            demographics.place(x=175, y= 200)
            results.place(x= 380, y= 400)
        case "an Extreme extrovert":
            exp_of_results.config(text="You scored as highly extroverted. \nThis means that being around people energizes you, people describe you as friendly and approachable, \nand highly enjoys conversing with others.")
            exp_of_results.place(x=40, y=270)
            demographics.place(x=215, y= 200)
            results.place(x= 370, y= 400)

results = tk.Button(
    master=page_4,
    text= "Click for results",
    command= lambda: explanation()
)

results.place(x= 480, y=270)

window.mainloop()