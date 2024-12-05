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
    text= "When a stranger talks to me, I consider it an opportunity to make a connection.?",
    bg= "light grey"
)
q1_a1 = tk.Button(                      #Assigning a neutral value of 1 to this answer
    master= answers_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command= lambda: add_to_opn(a2_value)
)
q1_a2 = tk.Button(                      #Assigning a positive value of 0 to this answer
    master=answers_labels_1,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_opn(a1_value)
)

q1_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_opn(a3_value)
)



Question_2 = tk.Label(               
    master=question_labels_1,
    text= " Being out with a big group of friends all night can be exhausting.",
    bg= "light grey"
)
q2_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_1,
    text= "Agree!",
    relief= "raised",
    bg= "grey",
    command=lambda: add_to_agr(a1_value)
)

q2_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_1,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=add_to_agr(a2_value)
)
q2_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=add_to_agr(a3_value)
)

Question_3 = tk.Label(                  #Measuring Neuroticism
    master=question_labels_1,
    text= "I consider myself to be an assertive person.",
    bg= "light grey"
)
q3_a1 = tk.Button(                      #Assigning a neutral value of 0 to this answer
    master=answers_labels_1,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a1_value)
)
q3_a2 = tk.Button(                      #Assigning a positive value of postive 1 to this answer
    master=answers_labels_1,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a2_value)
)
q3_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_1,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=add_to_nrt(a3_value)
)

Question_4 = tk.Label(                  #Measuring Consientiousness
    master=question_labels_1,
    text= "It’s not unusual for me to get lost in thought around other people.",
    bg= "light grey"
)
q4_a1 = tk.Button(                      #Assigning a neutral value of 1 to this answer
    master=answers_labels_1,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a1_value)
)
q4_a2 = tk.Button(                      #Assigning a positive value of postive 0 to this answer
    master=answers_labels_1,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a2_value)
)
q4_a3 = tk.Button(                      #Assigning a negative value of +1 to this answer
    master=answers_labels_1,
    text= "Disagree",
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
    text= "I think that being on a reality show would be a nightmare.",                
    bg= "light grey"
)
q5_a1 = tk.Button(                      #Assigning - 1 to this
    master=answers_labels_2,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a1_value)
)
q5_a2 = tk.Button(                      #Assigning a positive value of postive 0 to this answer
    master=answers_labels_2,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a2_value)
)
q5_a3 = tk.Button(              #Assigning a negative value of +1 to this answer
    master=answers_labels_2,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command= add_to_ctn(a3_value)
)

Question_6 = tk.Label(                  
    master=question_labels_2,
    text= "I don’t mind talking about anything, even if I’m not that knowledgeable about it.",
    bg= "light grey")

q6_a1 = tk.Button(                      #Assigning value 1 to this answer
    master=answers_labels_2,
    text= "Agree",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a1_value)
)
q6_a2 = tk.Button(                      #Assigning a 0 to this answer
    master=answers_labels_2,
    text= "Sometimes",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a2_value)
)
q6_a3 = tk.Button(                      #Assigning a negative value of -1 to this answer
    master=answers_labels_2,
    text= "Disagree",
    relief= "raised",
    bg= "grey",
    command=add_to_ctn(a3_value)
)
