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

def add_to_nrt(value):
    Neuroticism_list.append(value)

def print_agr():
    print(Agreeableness_list)

def opn_score():
    total = 0
    for num in Openness_list:
        total += num
    total = float(total/4)
    print(total)

def nrt_score():
    total = 0
    for num in Neuroticism_list:
        total += num
    total = float(total/4)
    print(total)

def agr_score():
    total = 0
    for num in Agreeableness_list:
        total += num
    total = float(total/4)
    print(total)

def ctn_score():
    total = 0
    for num in Conscientiousness_list:
        total += num
    total = float(total/4)
    print(total)

def ext_score():
    total = 0
    for num in Extraversion_list:
        total += num
    total = float(total/4)
    print(total)


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
    text= "How do you react when meeting new people?",
    bg= "light grey"
)
q13_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master= answers_labels_4,
    text= "I don't find myself excited, but I am not scared to.",
    relief= "raised",
    bg= "grey",
    command= lambda: add_to_opn(a1_value)
)
q13_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_4,
    text= "I love to meet new people, and strike up conversation with them.",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_opn(a2_value)
)

q13_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_4,
    text= "I get nervous and tend to avoid meeting new people.",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_opn(a3_value)
)



Question_14 = tk.Label(                  #Measuring Agreableness
    master=question_labels_4,
    text= "How do you typically treat others?",
    bg= "light grey"
)
q14_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_4,
    text= "I don't think I am particularly kind, but I don't think I am mean.",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_agr(a1_value)
)

q14_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_4,
    text= "I try to always treat others with kindness and respect.",
    relief= "raised",
    bg= "grey",
    command=add_to_agr(a2_value)
)
q14_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_4,
    text= "I am typically not sensitive of other peoples feelings.",
    relief= "raised",
    bg= "grey",
    command=add_to_agr(a3_value)
)

Question_15 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_4,
    text= "How Often do you feel sad or depressed?",
    bg= "light grey"
)
q15_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_4,
    text= "I only find myself feeling sad or depressed when a situation warrants it.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a1_value)
)
q15_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_4,
    text= "I dont find myself feeling sad or depressed.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a2_value)
)
q15_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_4,
    text= "I frequently feel sad or depressed.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a3_value)
)

Question_16 = tk.Label(                  #Measuring Consientiousness
    master=question_labels_4,
    text= "What's your process when making decisions?",
    bg= "light grey"
)
q16_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_4,
    text= "Sometimes I plan things out, but I also trust my gut.",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a1_value)
)
q16_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_4,
    text= "I think about the consequences of one decision over another and choose the best one.",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a2_value)
)
q16_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_4,
    text= "I just trust my gut and go with what I feel..",
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
    text= "Do you get stressed easily?",
    bg= "light grey"
)
q17_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_5,
    text= "Yes, but sometimes I am better at managing it than other times.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a1_value)
)
q17_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_5,
    text= "No, but even when I do feel stressed, I bounce back quickly.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a2_value)
)
q17_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_5,
    text= "Yes, and once I'm stressed, it's hard for me to calm down.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a3_value)
)

Question_18 = tk.Label(                  #Measuring Extraversion
    master=question_labels_5,
    text= "How do you feel about small talk?",
    bg= "light grey"
)
q18_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_5,
    text= "It depends on how I am feeling, but occasionally I engage in small talk.",
    relief= "raised",
    bg= "grey",
    command=add_to_ext(a1_value)
)
q18_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_5,
    text= "I consider myself a small talk expert.",
    relief= "raised",
    bg= "grey",
    command=add_to_ext(a2_value)
)
q18_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_5,
    text= "Small talk makes me anxious, and I tend to avoid talking about myself.",
    relief= "raised",
    bg= "grey",
    command=add_to_ext(a3_value)
)

Question_19 = tk.Label(                  #Measuring ???Not sure???
    master=question_labels_5,
    text= "Would your firends describe you as dependable?",
    bg= "light grey"
)
q19_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_5,
    text= "It depends on what we're doing, but generally yes.",
    relief= "raised",
    bg= "grey"
)
q19_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_5,
    text= "Yes, I'm reliable and honor my commitments or plans.",
    relief= "raised",
    bg= "grey"
)
q19_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_5,
    text= "Probably not. I tend to be kind of flaky.",
    relief= "raised",
    bg= "grey"
)

Question_20 = tk.Label(                  #Measuring ???Not sure???
    master=question_labels_5,
    text= "How do you feel about repetitive tasks?",
    bg= "light grey"
)
q20_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_5,
    text= "Sometimes I need tasks like that to help me calm down.",
    relief= "raised",
    bg= "grey"
)
q20_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_5,
    text= "I'm comfortable with repetitive tasks; routine is good.",
    relief= "raised",
    bg= "grey"
)
q20_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_5,
    text= "I get bored easily and need variety whenever possible.",
    relief= "raised",
    bg= "grey"
)
Next_p5 = tk.Button(
    master=answers_labels_4,
    text="Next",
    relief="raised",
    command= lambda: (five_to_finish, opn_score, ext_score, agr_score, ctn_score, nrt_score)
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
Question_19.place(x= 0, y= 240)
q19_a1.place(x=0, y=240)
q19_a2.place(x=0, y=270)
q19_a3.place(x=0, y=300)
Question_20.place(x= 0, y= 360)
q20_a1.place(x=0, y=360)
q20_a2.place(x=0, y=390)
q20_a3.place(x=0, y=420)

Next_p5.place(x=0, y=480)

###################################################################################################################

#EVERYTHING TO DO WITH THE RESULTS PAGE



window.mainloop()