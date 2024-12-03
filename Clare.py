import tkinter as tk

window = tk.Tk()
window.title("Window")

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
    command= lambda: add_to_opn(a2_value)
)
q1_a2 = tk.Button(                      #Assigning a positive value of 0 to this answer
    master=answers_labels_1,
    text= "Change makes me nervous if I haven't planned for it.",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_opn(a1_value)
)

q1_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "It makes me uncomfortable. I like things to remain the same.",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_opn(a3_value)
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
    command=lambda: add_to_agr(a1_value)
)

q2_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_1,
    text= "Planning stress me out, but being surprised stresses me out more.",
    relief= "raised",
    bg= "grey",
    command=add_to_agr(a2_value)
)
q2_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "I need things structured and organized so I enjoy planning ahead.",
    relief= "raised",
    bg= "grey",
    command=add_to_agr(a3_value)
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
    command=add_to_nrt(a1_value)
)
q3_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_1,
    text= "I cherish the chance to exercise my empathy muscles.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a2_value)
)
q3_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "Socializing can be draining.",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a3_value)
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
    command=add_to_ctn(a1_value)
)
q4_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_1,
    text= "I may find it hard to stop what I'm doing",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a2_value)
)
q4_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "I'd stay out of their business, it's not my problem.",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a3_value)

)
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
Question_5 = tk.Label(                  
    master=question_labels_2,
    text= "How often do you experience intense emotional changes",                
    bg= "light grey"
)
q5_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_2,
    text= "My mood stays pretty consistent",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a1_value)
)
q5_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_2,
    text= "I have emotional ups and downs all the time",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a2_value)
)
###q5_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
   ## master=answers_labels_4,
    ####command=add_to_ctn(a3_value)


Question_6 = tk.Label(                  #Measuring Agreableness
    master=question_labels_2,
    text= "A friend asks you to try something new with them. How do you respond?",
    bg= "light grey")

q6_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_2,
    text= "I'd do everything I could do to help",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a1_value)
)
q6_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_2,
    text= "I may find it hard to stop what I'm doing",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a2_value)
)
q6_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text= "I'd stay out of their business, it's not my problem.",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a3_value)
)
