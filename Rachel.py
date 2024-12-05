import tkinter as tk

window = tk.Tk()
window.title("Window")

##################################################################################

#MISC THINGS NEEDED BEFOREHAND

a1_value = 0

a2_value = 1

a3_value = -1

Extraversion_list = []
Openness_list = []
Conscientiousness_list = []
Agreeableness_list = []
Neuroticism_list = []

def add_to_ext(value):
    Extraversion_list.append(value)

def add_to_opn(value):
    Openness_list.append(value)

def add_to_ctn(value):
    Conscientiousness_list.append(value)

def add_to_agr(value):
    Agreeableness_list.append(value)
    print(f"I have returned the value of {value} to the Agreeableness list")

def add_to_nrt(value):
    Neuroticism_list.append(value)

def print_agr():
    print(Agreeableness_list)


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
    page_welcome.forget()
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
    page_1.forget()
    page_2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Next_p1 = tk.Button(
    master=page_1,
    text="Next",
    command=one_to_two
)
p1_working = tk.Label(
    master=question_labels_1,
    text= "is p1 working"
)

question_labels_1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
answers_labels_1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
p1_working.pack()
# Question_1.place(x= 0, y= 0)
# q1_a1.place(x=00, y=0)
# q1_a2.place(x=00, y=30)
# q1_a3.place(x=00, y=60)

# Question_2.place(x= 0, y= 120)
# q2_a1.place(x=00, y=120)
# q2_a2.place(x=00, y=150)
# q2_a3.place(x=00, y=180)

# Question_3.place(x= 0, y= 240)
# q3_a1.place(x=00, y=240)
# q3_a2.place(x=00, y=270)
# q3_a3.place(x=00, y=300)

# Question_4.place(x= 0, y= 360)
# q4_a1.place(x=00, y=360)
# q4_a2.place(x=00, y=390)
# q4_a3.place(x=00, y=420)

Next_p1.place(x=0, y= 480)

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
    page_2.forget()
    page_3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Next_p2 = tk.Button(
    master=page_2,
    text="Next",
    command=two_to_three
)
p2_working = tk.Label(
    master=question_labels_2,
    text= "is page 2 working?"
)

Question_7 = tk.Label(                  #Measuring Conscientiousness
    master=question_labels_2,
    text= "I'd rather spend one-on-one time with a close friend than get together with a friend group.",
    bg= "light grey"
)
q7_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master= answers_labels_2,
    text= "Sometimes.",
    relief= "raised",
    bg= "grey",
    command= lambda: add_to_ctn(a1_value)
)
q7_a2 = tk.Button(                      #Assigning a positive value of -1 to this answer
    master=answers_labels_2,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_ctn(a2_value)
)

q7_a3 = tk.Button(                      #Assigning a negative value of 1 to this answer
    master=answers_labels_2,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_ctn(a3_value)
)

Question_8 = tk.Label(                  #Measuring Extraversion
    master=question_labels_2,
    text= "It's better to have a roommate than to live alone.",
    bg= "light grey"
)
q8_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_2,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_ext(a1_value)
)
q8_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_2,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=add_to_ext(a2_value)
)
q8_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=add_to_ext(a3_value)
)

question_labels_2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
answers_labels_2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
p2_working.pack()

# Question_5.place(x= 0, y= 0)
# q5_a1.place(x=00, y=0)
# q5_a2.place(x=00, y=30)
# q5_a3.place(x=00, y=60)

# Question_6.place(x= 0, y= 120)
# q6_a1.place(x=00, y=120)
# q6_a2.place(x=00, y=150)
# q6_a3.place(x=00, y=180)

# Question_7.place(x= 0, y= 240)
# q7_a1.place(x=00, y=240)
# q7_a2.place(x=00, y=270)
# q7_a3.place(x=00, y=300)

# Question_8.place(x= 0, y= 360)
# q8_a1.place(x=00, y=360)
# q8_a2.place(x=00, y=390)
# q8_a3.place(x=00, y=420)

Next_p2.place(x=0, y= 480)

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
    page_3.forget()
    page_4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


Next_p3 = tk.Button(
    master=page_3,
    text="Next",
    command=three_to_four
)
p3_working = tk.Label(
    master=question_labels_3,
    text= "this is working"
)

Question_9 = tk.Label(                  #Measuring openness
    master=question_labels_3,
    text= "It's disappointing to review my weekly schedule and see that it includes no social plans.",
    bg= "light grey"
)
q9_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_3,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=add_to_opn(a1_value)
)
q9_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_3,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=add_to_opn(a2_value)
)
q9_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_3,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=add_to_opn(a3_value)
)

Question_10 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_3,
    text= "At work meetings I think it's important to speak up often.",
    bg= "light grey"
)
q10_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_3,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a1_value)
)
q10_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_3,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a2_value)
)
q10_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_3,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a3_value)
)

Question_11 = tk.Label(                  #Measuring Openness
    master=question_labels_3,
    text= "I have a lot of fun playing tricks on my friends and family.",
    bg= "light grey"
)
q11_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_3,
    text= "Sometimes",
    relief= "raised",
    bg= "grey"
)
q11_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_3,
    text= "Agree",
    relief= "raised",
    bg= "grey"
)
q11_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_3,
    text= "Disagree",
    relief= "raised",
    bg= "grey"
)

Question_12 = tk.Label(                  #Measuring Conscientiousness
    master=question_labels_3,
    text= "I like to get my friends and co-workers excited about our plans.",
    bg= "light grey"
)
q12_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_3,
    text= "Neutral",
    relief= "raised",
    bg= "grey"
)
q12_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_3,
    text= "Agree",
    relief= "raised",
    bg= "grey"
)
q12_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_3,
    text= "Disagree",
    relief= "raised",
    bg= "grey"
)

question_labels_3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
answers_labels_3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
p3_working.pack()

# Question_9.place(x= 0, y= 0)
# q9_a1.place(x=00, y=0)
# q9_a2.place(x=00, y=30)
# q9_a3.place(x=00, y=60)

# Question_10.place(x= 0, y= 120)
# q10_a1.place(x=00, y=120)
# q10_a2.place(x=00, y=150)
# q10_a3.place(x=00, y=180)

# Question_11.place(x= 0, y= 240)
# q11_a1.place(x=00, y=240)
# q11_a2.place(x=00, y=270)
# q11_a3.place(x=00, y=300)

# Question_12.place(x= 0, y= 360)
# q12_a1.place(x=00, y=360)
# q12_a2.place(x=00, y=390)
# q12_a3.place(x=00, y=420)

Next_p3.place(x=0, y= 480)

#################################################################################################################

#EVERYTHING TO DO WITH PAGE 4 OF QUESTIONS

page_4 = tk.Frame(
    master=window, 
    width=750, 
    height=475, 
    bg="light grey"
)
question_labels_4 = tk.Frame(
    master=page_4,
    bg="light grey",
    width=275, 
    height=475,
)
answers_labels_4 = tk.Frame(
    master=page_4,
    bg="light grey",
    width=500, 
    height=510,
)

def four_to_five():
    page_4.forget()
    page_5.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Next_p4 = tk.Button(
    master=answers_labels_4,
    text="Next",
    relief="raised",
    command=four_to_five,
)

Question_13 = tk.Label(                  #Measuring Openness
    master=question_labels_4,
    text= "I don't like to feel pushed into dancing at parties",
    bg= "light grey"
)
q13_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master= answers_labels_4,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command= lambda: add_to_opn(a1_value)
)
q13_a2 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_4,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_opn(a2_value)
)

q13_a3 = tk.Button(                      #Assigning a positive value of +1 to this answer
    master=answers_labels_4,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_opn(a3_value)
)



Question_14 = tk.Label(                  #Measuring Agreableness
    master=question_labels_4,
    text= "When I'm in charge, I prefer meeting with people one-on-one to holding large brainstomring sessions.",
    bg= "light grey"
)
q14_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_4,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_agr(a1_value)
)

q14_a2 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_4,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=add_to_agr(a2_value)
)
q14_a3 = tk.Button(                      #Assigning a positive value of +1 to this answer
    master=answers_labels_4,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=add_to_agr(a3_value)
)

Question_15 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_4,
    text= "When I go to a party, I often think about how early it would be approproiate to leave.",
    bg= "light grey"
)
q15_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_4,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a1_value)
)
q15_a2 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_4,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a2_value)
)
q15_a3 = tk.Button(                      #Assigning a positive value of +1 to this answer
    master=answers_labels_4,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a3_value)
)

Question_16 = tk.Label(                  #Measuring Consientiousness
    master=question_labels_4,
    text= "If someone is interesting enough, I could happily spend an evening just listening to their stories.",
    bg= "light grey"
)
q16_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_4,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a1_value)
)
q16_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_4,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a2_value)
)
q16_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_4,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a3_value)
)

question_labels_4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
answers_labels_4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

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

Next_p4.place(x=0, y= 480)

##################################################################################################################

#EVERYTHING TO DO WITH PAGE 5 OF QUESTIONS

page_5 = tk.Frame(
    master=window, 
    width=750, 
    height=475, 
    bg="light grey"
)
question_labels_5 = tk.Frame(
    master=page_5,
    bg="light grey",
     width=275, 
    height=475
)
answers_labels_5 = tk.Frame(
    master=page_5,
    bg="light grey",
     width=500, 
    height=510,
)
def five_to_finish():
    page_5.forget()
    #PACK the final page here 

Question_17 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_5,
    text= "In work or in life, I'd rather take some time to consider the next steps even if others are eager to rush ahead.",
    bg= "light grey"
)
q17_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_5,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a1_value)
)
q17_a2 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_5,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a2_value)
)
q17_a3 = tk.Button(                      #Assigning a positive value of +1 to this answer
    master=answers_labels_5,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a3_value)
)

Question_18 = tk.Label(                  #Measuring Extraversion
    master=question_labels_5,
    text= "As a kid, I was always the first to volunteer to read aloud.",
    bg= "light grey"
)
q18_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_5,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=add_to_ext(a1_value)
)
q18_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_5,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=add_to_ext(a2_value)
)
q18_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_5,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=add_to_ext(a3_value)
)

Next_p5 = tk.Button(
    master=answers_labels_4,
    text="Next",
    relief="raised",
    command=five_to_finish
)

question_labels_5.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
answers_labels_5.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Question_17.place(x= 0, y= 0)
q17_a1.place(x=0, y=0)
q17_a2.place(x=0, y=30)
q17_a3.place(x=0, y=60)
Question_18.place(x= 0, y= 120)
q18_a1.place(x=0, y=120)
q18_a2.place(x=0, y=150)
q18_a3.place(x=0, y=180)

Next_p5.place(x=0, y=480)

###################################################################################################################

#EVERYTHING TO DO WITH THE RESULTS PAGE

window.mainloop()