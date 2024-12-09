import tkinter as tk

window = tk.Tk()
window.title("Window")

##################################################################################

#MISC THINGS NEEDED BEFOREHAND

zero_value = 0

one_value = 1

neg_one_value = -1


total_ext_int_score = []

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

def reverse_button(button,value):
    subtract_from_total(value)
    button.config(relief = "raised", command = lambda: (pressed_button(button,value)))
    print(total_ext_int_score)

def pressed_button(button,value):
    add_to_total(value)
    button.config(relief="sunken", command = lambda: (reverse_button(button,value)))
    print(total_ext_int_score)


###################################################################################

#EVERYTHING TO DO WITH THE WELCOME PAGE

page_welcome = tk.Frame(
    master=window, 
    width=750, 
    height=475, 
    bg="light grey"
)



welcome = tk.Label(
    master=page_welcome,
    text= "Welcome! \n Please press the button below to begin your Personality Quiz Journey:",
    bg= "light grey"
)
def start_to_p1():
    page_welcome.destroy()
    page_1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
start = tk.Button(
    master=page_welcome,
    text="Begin",
    command=start_to_p1
)

page_welcome.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
welcome.place(x= 200, y= 200)
start.place(x=275, y=260)

#####################################################################################

#EVERYTHING TO DO WITH PAGE 1 OF QUESTIONS

page_1 = tk.Frame(
    master=window, 
    width=750, 
    height=475, 
    bg="light grey"
)
question_labels_1 = tk.Frame(
    master=page_1,
    bg="light grey",
    width=275, 
    height=475,
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
    master=answers_labels_1,
    text="Next",
    command=one_to_two
)

Question_1 = tk.Label(                  #Measuring Agreableness
    master=question_labels_1,
    text= "When a stranger talks to me, I consider it an opportunity to make a connection?",
    bg= "light grey"
)
q1_a1 = tk.Button(                      #Assigning a neutral value of 1 to this answer
    master= answers_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command= lambda: pressed_button(q1_a1, one_value)
)
q1_a2 = tk.Button(                      #Assigning a positive value of 0 to this answer
    master=answers_labels_1,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q1_a2, zero_value)
)

q1_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q1_a3, neg_one_value)
)



Question_2 = tk.Label(               #Measuring Agreableness
    master=question_labels_1,
    text= "Being out with a big group of friends all night can be exhausting.",
    bg= "light grey"
)
q2_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master=answers_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q2_a1, neg_one_value)
)

q2_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_1,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q2_a2, zero_value)
)
q2_a3 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_1,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q2_a3, one_value)
)

Question_3 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_1,
    text= "I consider myself to be an assertive person.",
    bg= "light grey"
)
q3_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q3_a1, one_value)
)
q3_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_1,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q3_a2, zero_value)
)
q3_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q3_a3, neg_one_value)
)

Question_4 = tk.Label(                  #Measuring Consientiousness
    master=question_labels_1,
    text= "It’s not unusual for me to get lost in thought around other people.",
    bg= "light grey"
)
q4_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master=answers_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q4_a1, neg_one_value)
)
q4_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_1,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q4_a2, zero_value)
)
q4_a3 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_1,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q4_a3, one_value)
)
Question_5 = tk.Label(                  
    master=question_labels_1,
    text= "I think that being on a reality show would be a nightmare.",                
    bg= "light grey"
)
q5_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master=answers_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q5_a1, neg_one_value)
)
q5_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_1,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q5_a2, zero_value)
)
q5_a3 = tk.Button(                      #Assigning a value of 1 to this answer
   master=answers_labels_1,
   text="Disagree.",
   command=lambda: pressed_button(q5_a3, one_value)
)

Question_6 = tk.Label(                  #Measuring Agreableness
    master=question_labels_1,
    text= "I don’t mind talking about anything, even if I’m not that knowledgeable about it.",
    bg= "light grey")

q6_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q6_a1, one_value)
)
q6_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_1,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q6_a2, zero_value)
)
q6_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q6_a3, neg_one_value)
)


question_labels_1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
answers_labels_1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Question_1.place(x= 0, y= 0)
q1_a1.place(x=00, y=0)
q1_a2.place(x=00, y=30)
q1_a3.place(x=00, y=60)

Question_2.place(x= 0, y= 120)
q2_a1.place(x=00, y=120)
q2_a2.place(x=00, y=150)
q2_a3.place(x=00, y=180)

Question_3.place(x= 0, y= 240)
q3_a1.place(x=00, y=240)
q3_a2.place(x=00, y=270)
q3_a3.place(x=00, y=300)

Question_4.place(x= 0, y= 360)
q4_a1.place(x=00, y=360)
q4_a2.place(x=00, y=390)
q4_a3.place(x=00, y=420)

Question_5.place(x= 0, y= 480)
q5_a1.place(x=00, y=480)
q5_a2.place(x=00, y=510)
q5_a3.place(x=00, y=540)

Question_6.place(x= 0, y= 600)
q6_a1.place(x=00, y=600)
q6_a2.place(x=00, y=630)
q6_a3.place(x=00, y=660)

Next_p1.place(x=0, y= 720)

##########################################################################################################

#EVERYTHING TO DO WITH PAGE 2 OF QUESTIONS

page_2 = tk.Frame(
    master=window, 
    width=750, 
    height=475, 
    bg="light grey"
)
question_labels_2 = tk.Frame(
    master=page_2,
    bg="light grey",
    width=275, 
    height=475,
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
    master=answers_labels_2,
    text="Next",
    command=two_to_three
)

Question_7 = tk.Label(                  #Measuring Conscientiousness
    master=question_labels_2,
    text= "I'd rather spend one-on-one time with a close friend than get together with a friend group.",
    bg= "light grey"
)
q7_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master= answers_labels_2,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command= lambda: pressed_button(q7_a1, neg_one_value)
)
q7_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q7_a2, zero_value)
)
q7_a3 = tk.Button(                      #Assigning a value to 1 to this answer
    master=answers_labels_2,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q7_a3, one_value)
)

Question_8 = tk.Label(                  #Measuring Extraversion
    master=question_labels_2,
    text= "It's better to have a roommate than to live alone.",
    bg= "light grey"
)
q8_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_2,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q8_a1, one_value)
)
q8_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q8_a2, zero_value)
)
q8_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q8_a3, neg_one_value)
)

Question_9 = tk.Label(                  #Measuring openness
    master=question_labels_2,
    text= "It's disappointing to review my weekly schedule and see that it includes no social plans.",
    bg= "light grey"
)
q9_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_2,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q9_a1, one_value)
)
q9_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q9_a2, zero_value)
)
q9_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q9_a3, neg_one_value)
)

Question_10 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_2,
    text= "At work meetings I think it's important to speak up often.",
    bg= "light grey"
)
q10_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_2,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q10_a1, one_value)
)
q10_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q10_a2, zero_value)
)
q10_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q10_a3, neg_one_value)
)

Question_11 = tk.Label(                  #Measuring Openness
    master=question_labels_2,
    text= "I have a lot of fun playing tricks on my friends and family.",
    bg= "light grey"
)
q11_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_2,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q11_a1, one_value)
)
q11_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q11_a2, zero_value)
)
q11_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q11_a3, neg_one_value)
)

Question_12 = tk.Label(                  #Measuring Conscientiousness
    master=question_labels_2,
    text= "I like to get my friends and co-workers excited about our plans.",
    bg= "light grey"
)
q12_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_2,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q12_a1, one_value)
)
q12_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q12_a2,zero_value)
)
q12_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text="Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q12_a3, neg_one_value)
)

question_labels_2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
answers_labels_2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Question_7.place(x= 0, y= 0)
q7_a1.place(x=00, y=0)
q7_a2.place(x=00, y=30)
q7_a3.place(x=00, y=60)

Question_8.place(x= 0, y= 120)
q8_a1.place(x=00, y=120)
q8_a2.place(x=00, y=150)
q8_a3.place(x=00, y=180)

Question_9.place(x= 0, y= 240)
q9_a1.place(x=00, y=240)
q9_a2.place(x=00, y=270)
q9_a3.place(x=00, y=300)

Question_10.place(x= 0, y= 360)
q10_a1.place(x=00, y=360)
q10_a2.place(x=00, y=390)
q10_a3.place(x=00, y=420)

Question_11.place(x= 0, y= 480)
q11_a1.place(x=00, y=480)
q11_a2.place(x=00, y=510)
q11_a3.place(x=00, y=540)

Question_12.place(x= 0, y= 600)
q12_a1.place(x=00, y=600)
q12_a2.place(x=00, y=630)
q12_a3.place(x=00, y=660)

Next_p2.place(x=0, y= 720)

###################################################################################################################

#EVERYTHING TO DO WITH PAGE 3 OF QUESTIONS

page_3 = tk.Frame(
    master=window, 
    width=750, 
    height=475, 
    bg="light grey"
)
question_labels_3 = tk.Frame(
    master=page_3,
    bg="light grey",
    width=275, 
    height=475,
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
    master=answers_labels_3,
    text="Next",
    command= lambda: (three_to_four(), calculate_score())
)

Question_13 = tk.Label(                  #Measuring Openness
    master=question_labels_3,
    text= "I don't like to feel pushed into dancing at parties.",
    bg= "light grey"
)
q13_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master= answers_labels_3,
    text= "Agree.",
    relief= "raised",
    bg= "grey",
    command= lambda: pressed_button(q13_a1, neg_one_value)
)
q13_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_3,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q13_a2, zero_value)
)

q13_a3 = tk.Button(   
    master=answers_labels_3,                   #Assigning a value of 1 to this answer
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q13_a3, one_value)
)



Question_14 = tk.Label(                  #Measuring Agreableness
    master=question_labels_3,
    text= "When I'm in charge, I prefer meeting with people one-on-one to holding large brainstomring sessions.",
    bg= "light grey"
)
q14_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master=answers_labels_3,
    text= "Agree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q14_a1, neg_one_value)
)

q14_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_3,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q14_a2, zero_value)
)
q14_a3 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_3,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q14_a3, one_value)
)

Question_15 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_3,
    text= "When I go to a party, I often think about how early it would be approproiate to leave.",
    bg= "light grey"
)
q15_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master=answers_labels_3,
    text= "Agree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q15_a1, neg_one_value)
)
q15_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_3,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q15_a2, zero_value)
)
q15_a3 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_3,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q15_a3, one_value)
)

Question_16 = tk.Label(                  #Measuring Consientiousness
    master=question_labels_3,
    text= "If someone is interesting enough, I could happily spend an evening just listening to their stories.",
    bg= "light grey"
)
q16_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_3,
    text= "Agree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q16_a1, one_value)
)
q16_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_3,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q16_a2, zero_value)
)
q16_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_3,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q16_a3, neg_one_value)
)

Question_17 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_3,
    text= "In work or in life, I'd rather take some time to consider the next steps even if others are eager to rush ahead.",
    bg= "light grey"
)
q17_a1 = tk.Button(                      #Assigning a value of -1 to this answer
    master=answers_labels_3,
    text= "Agree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q17_a1, neg_one_value)
)
q17_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_3,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q17_a2, zero_value)
)
q17_a3 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_3,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q17_a3, one_value)
)

Question_18 = tk.Label(                  #Measuring Extraversion
    master=question_labels_3,
    text= "As a kid, I was always the first to volunteer to read aloud.",
    bg= "light grey"
)
q18_a1 = tk.Button(                      #Assigning a value of 1 to this answer
    master=answers_labels_3,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q18_a1, one_value)
)
q18_a2 = tk.Button(                      #Assigning a value of 0 to this answer
    master=answers_labels_3,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q18_a1, zero_value)
)
q18_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_3,
    text= "Disagree.",
    relief= "raised",
    bg= "grey",
    command=lambda: pressed_button(q18_a1, neg_one_value)
)

question_labels_3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
answers_labels_3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Question_13.place(x= 0, y= 0)
q13_a1.place(x=00, y=0)
q13_a2.place(x=00, y=30)
q13_a3.place(x=00, y=60)

Question_14.place(x= 0, y= 120)
q14_a1.place(x=00, y=120)
q14_a2.place(x=00, y=150)
q14_a3.place(x=00, y=180)

Question_15.place(x= 0, y= 240)
q15_a1.place(x=00, y=240)
q15_a2.place(x=00, y=270)
q15_a3.place(x=00, y=300)

Question_16.place(x= 0, y= 360)
q16_a1.place(x=00, y=360)
q16_a2.place(x=00, y=390)
q16_a3.place(x=00, y=420)

Question_17.place(x= 0, y= 480)
q17_a1.place(x=00, y=480)
q17_a2.place(x=00, y=510)
q17_a3.place(x=00, y=540)

Question_18.place(x= 0, y= 600)
q18_a1.place(x=00, y=600)
q18_a2.place(x=00, y=630)
q18_a3.place(x=00, y=660)

Next_p3.place(x=0, y= 720)

#################################################################################################################

#EVERYTHING TO DO WITH THE RESULTS PAGE

page_4 = tk.Frame(
    master=window, 
    width=750, 
    height=475, 
    bg="light grey"
)

window.mainloop()