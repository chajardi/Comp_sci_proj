import tkinter as tk

window = tk.Tk()
window.title("Window")

##################################################################################

#MISC THINGS NEEDED BEFOREHAND

a1_value = 0

a2_value = 1

a3_value = -1


global total_ext_int_score
total_ext_int_score = 0

def add_to_total(value):
    total_ext_int_score = total_ext_int_score+value

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
    text= "How do you typically react to change?",
    bg= "light grey"
)
q1_a1 = tk.Button(                      #Assigning a neutral value of 1 to this answer
    master= answers_labels_1,
    text= "I embrace it. New experiences are exciting!",
    relief= "raised",
    bg= "grey",
    command= lambda: add_to_total(a2_value)
)
q1_a2 = tk.Button(                      #Assigning a positive value of 0 to this answer
    master=answers_labels_1,
    text= "Change makes me nervous if I haven't planned for it.",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_total(a1_value)
)

q1_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "It makes me uncomfortable. I like things to remain the same.",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_total(a3_value)
)



Question_2 = tk.Label(               #Measuring Agreableness
    master=question_labels_1,
    text= "How do you feel about planning ahead?",
    bg= "light grey"
)
q2_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_1,
    text= "I prefer to be spontaneous",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_total(a1_value)
)

q2_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_1,
    text= "Planning stress me out, but being surprised stresses me out more.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a2_value)
)
q2_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "I need things structured and organized so I enjoy planning ahead.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a3_value)
)

Question_3 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_1,
    text= "Do you enjoy socializing?",
    bg= "light grey"
)
q3_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_1,
    text= "Being around others makes me feel energized.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a1_value)
)
q3_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_1,
    text= "I cherish the chance to exercise my empathy muscles.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a2_value)
)
q3_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "Socializing can be draining.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a3_value)
)

Question_4 = tk.Label(                  #Measuring Consientiousness
    master=question_labels_1,
    text= "If you see someone in trouble, what would you do?",
    bg= "light grey"
)
q4_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_1,
    text= "I'd do everything I could do to help",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a1_value)
)
q4_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_1,
    text= "I may find it hard to stop what I'm doing",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a2_value)
)
q4_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "I'd stay out of their business, it's not my problem.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a3_value)
)
Question_5 = tk.Label(                  
    master=question_labels_1,
    text= "How often do you experience intense emotional changes",                
    bg= "light grey"
)
q5_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_1,
    text= "My mood stays pretty consistent",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a1_value)
)
q5_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_1,
    text= "I have emotional ups and downs all the time",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a2_value)
)
q5_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
   master=answers_labels_1,
   command=add_to_total(a3_value)
)

Question_6 = tk.Label(                  #Measuring Agreableness
    master=question_labels_1,
    text= "A friend asks you to try something new with them. How do you respond?",
    bg= "light grey")

q6_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_1,
    text= "I'd do everything I could do to help",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a1_value)
)
q6_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_1,
    text= "I may find it hard to stop what I'm doing",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a2_value)
)
q6_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "I'd stay out of their business, it's not my problem.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a3_value)
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
    text= "How are you with deadlines?",
    bg= "light grey"
)
q7_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master= answers_labels_2,
    text= "I get things done to make sure I never let anyone down.",
    relief= "raised",
    bg= "grey",
    command= lambda: add_to_total(a1_value)
)
q7_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_2,
    text= "I structure my time well so that I never miss a deadline.",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_total(a2_value)
)
q7_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text= "I usually procrastinate and get things done at the last minute or a bit late.",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_total(a3_value)
)

Question_8 = tk.Label(                  #Measuring Extraversion
    master=question_labels_2,
    text= "You are at a party. What are you likely doing?",
    bg= "light grey"
)
q8_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_2,
    text= "Having a good time, but letting others steal the spotlight.",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_total(a1_value)
)
q8_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_2,
    text= "Organizing a game for everyone to play.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a2_value)
)
q8_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text= "I'm hanging at the back of the room trying to observe without being noticed.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a3_value)
)

Question_9 = tk.Label(                  #Measuring openness
    master=question_labels_2,
    text= "Which type of game would you prefer to play?",
    bg= "light grey"
)
q9_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_2,
    text= "One where I work with a team to solve a problem together.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a1_value)
)
q9_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_2,
    text= "One that I've never played before.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a2_value)
)
q9_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text= "One that i already know all the rules for.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a3_value)
)

Question_10 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_2,
    text= "How do you respond to stressful situations?",
    bg= "light grey"
)
q10_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_2,
    text= "By enlisting the help of others to get through it.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a1_value)
)
q10_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_2,
    text= "By feeling anxious until it passes.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a2_value)
)
q10_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text= "I keep calm and take things as they come.",
    relief= "raised",
    bg= "grey",
    command=add_to_total(a3_value)
)

Question_11 = tk.Label(                  #Measuring Openness
    master=question_labels_2,
    text= "How creative are you?",
    bg= "light grey"
)
q11_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_2,
    text= "I am creative in some aspects, but less creative in others.",
    relief= "raised",
    bg= "grey"
)
q11_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_2,
    text= "I have a great imagination, and I love exploring creative ideas.",
    relief= "raised",
    bg= "grey"
)
q11_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text= "I tend to be more grounded in reality.",
    relief= "raised",
    bg= "grey"
)

Question_12 = tk.Label(                  #Measuring Conscientiousness
    master=question_labels_2,
    text= "How would you describe your attention to detail?",
    bg= "light grey"
)
q12_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_2,
    text= "Details are very important; I aim for precision in all things. ",
    relief= "raised",
    bg= "grey"
)
q12_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_2,
    text= "I worry that I'm always missing something important.",
    relief= "raised",
    bg= "grey"
)
q12_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text= "I prefer to focus more on the bigger picture.",
    relief= "raised",
    bg= "grey"
)

question_labels_2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
answers_labels_2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

Question_7.place(x= 0, y= 240)
q7_a1.place(x=00, y=240)
q7_a2.place(x=00, y=270)
q7_a3.place(x=00, y=300)

Question_8.place(x= 0, y= 360)
q8_a1.place(x=00, y=360)
q8_a2.place(x=00, y=390)
q8_a3.place(x=00, y=420)

Question_9.place(x= 0, y= 0)
q9_a1.place(x=00, y=0)
q9_a2.place(x=00, y=30)
q9_a3.place(x=00, y=60)

Question_10.place(x= 0, y= 120)
q10_a1.place(x=00, y=120)
q10_a2.place(x=00, y=150)
q10_a3.place(x=00, y=180)

Question_11.place(x= 0, y= 240)
q11_a1.place(x=00, y=240)
q11_a2.place(x=00, y=270)
q11_a3.place(x=00, y=300)

Question_12.place(x= 0, y= 360)
q12_a1.place(x=00, y=360)
q12_a2.place(x=00, y=390)
q12_a3.place(x=00, y=420)

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
    page_3.destroy()
    page_4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


Next_p3 = tk.Button(
    master=answers_labels_3,
    text="Next",
    command=three_to_four
)

Question_13 = tk.Label(                  #Measuring Openness
    master=question_labels_3,
    text= "How do you react when meeting new people?",
    bg= "light grey"
)
q13_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master= answers_labels_3,
    text= "I don't find myself excited, but I am not scared to.",
    relief= "raised",
    bg= "grey",
    command= lambda: add_to_opn(a1_value)
)
q13_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_3,
    text= "I love to meet new people, and strike up conversation with them.",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_opn(a2_value)
)

q13_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_3,
    text= "I get nervous and tend to avoid meeting new people.",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_opn(a3_value)
)



Question_14 = tk.Label(                  #Measuring Agreableness
    master=question_labels_3,
    text= "How do you typically treat others?",
    bg= "light grey"
)
q14_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_3,
    text= "I don't think I am particularly kind, but I don't think I am mean.",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_agr(a1_value)
)

q14_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_3,
    text= "I try to always treat others with kindness and respect.",
    relief= "raised",
    bg= "grey",
    command=add_to_agr(a2_value)
)
q14_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_3,
    text= "I am typically not sensitive of other peoples feelings.",
    relief= "raised",
    bg= "grey",
    command=add_to_agr(a3_value)
)

Question_15 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_3,
    text= "How Often do you feel sad or depressed?",
    bg= "light grey"
)
q15_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_3,
    text= "I only find myself feeling sad or depressed when a situation warrants it.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a1_value)
)
q15_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_3,
    text= "I dont find myself feeling sad or depressed.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a2_value)
)
q15_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_3,
    text= "I frequently feel sad or depressed.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a3_value)
)

Question_16 = tk.Label(                  #Measuring Consientiousness
    master=question_labels_3,
    text= "What's your process when making decisions?",
    bg= "light grey"
)
q16_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_3,
    text= "Sometimes I plan things out, but I also trust my gut.",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a1_value)
)
q16_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_3,
    text= "I think about the consequences of one decision over another and choose the best one.",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a2_value)
)
q16_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_3,
    text= "I just trust my gut and go with what I feel..",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a3_value)
)

Question_17 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_3,
    text= "Do you get stressed easily?",
    bg= "light grey"
)
q17_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_3,
    text= "Yes, but sometimes I am better at managing it than other times.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a1_value)
)
q17_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_3,
    text= "No, but even when I do feel stressed, I bounce back quickly.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a2_value)
)
q17_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_3,
    text= "Yes, and once I'm stressed, it's hard for me to calm down.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a3_value)
)

Question_18 = tk.Label(                  #Measuring Extraversion
    master=question_labels_3,
    text= "How do you feel about small talk?",
    bg= "light grey"
)
q18_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_3,
    text= "It depends on how I am feeling, but occasionally I engage in small talk.",
    relief= "raised",
    bg= "grey",
    command=add_to_ext(a1_value)
)
q18_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_3,
    text= "I consider myself a small talk expert.",
    relief= "raised",
    bg= "grey",
    command=add_to_ext(a2_value)
)
q18_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_3,
    text= "Small talk makes me anxious, and I tend to avoid talking about myself.",
    relief= "raised",
    bg= "grey",
    command=add_to_ext(a3_value)
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

Question_17.place(x= 0, y= 0)
q17_a1.place(x=0, y=0)
q17_a2.place(x=0, y=30)
q17_a3.place(x=0, y=60)

Question_18.place(x= 0, y= 120)
q18_a1.place(x=0, y=120)
q18_a2.place(x=0, y=150)
q18_a3.place(x=0, y=180)

Next_p3.place(x=0, y= 480)

#################################################################################################################

#EVERYTHING TO DO WITH THE RESULTS PAGE

page_4 = tk.Frame(
    master=window, 
    width=750, 
    height=475, 
    bg="light grey"
)




window.mainloop()