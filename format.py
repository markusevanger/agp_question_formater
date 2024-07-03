import random
import os




def isNotEmpty(string):
    return string.strip() != ""

def formatFile(filename):

    with open(filename, 'r') as file:
        
        questions = []
        answers = []


        counter = 0
        for line in file:

            if (counter < 20 and isNotEmpty(line)):
                questions.append(line.strip())
                counter += 1
            else:
                if (isNotEmpty(line) and counter > 19):
                    for answer in line.split(","):
                        answers.append(answer.strip())



    
    return (questions, answers)


def createFormattingQueue(watermark):
    
    allFiles = os.listdir()
    formattingQueue = []
    for file in allFiles:
        if file.endswith(".txt"):
            firstLine = open(file).readline().rstrip()
            if firstLine != watermark:
                formattingQueue.append(file)

    return formattingQueue


def main():

    watermark = "This file is formatted using a automated tool. Do not remove the line you are currently reading."
    formatted_folder_name = "formatted"
    

    if formatted_folder_name not in os.listdir():
        os.mkdir(formatted_folder_name)

    
    
    formattingQueue = createFormattingQueue(watermark)
    for file in formattingQueue:
        questions, answers = formatFile(file)
        
        if len(questions) != len(answers):
            print("Questions  and Answer length do not match. ")
            print(f"Amount of Qs: {len(questions)}")
            print(f"Amount of As: {len(answers)}")
            print(f"Stopping on program on file: {file}")
            return

        f = open(f"{formatted_folder_name}/{file.strip('.txt')}_formatted.txt", "w")
        f.write(watermark + "\n \n")

        
        # Questionset 1:
        f.write("Spørsmålssett 1: \n\n")
        for i in range(0, 10):
            f.write(f"{i+1}. {questions[i]} \n")
        f.write("\n")
        for i in range(0, 10):
            f.write(f"{i+1}. {answers[i]} \n")

        f.write("\n\n===================\n\n\n")
        

        # Questionset 2: 
        f.write("Spørsmålssett 2: \n\n")
        for i in range(10, 20):
            f.write(f"{i-9}. {questions[i]} \n")
        f.write("\n")

        for i in range(10, 20):
            f.write(f"{i-9}. {answers[i]} \n")
            



        



    # formater_fil(filename=fil)
    

main()