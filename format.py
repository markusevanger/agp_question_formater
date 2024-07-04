import os


"""

Dette scriptet er laget for å formatere "20 spørsmåls" filer til 2 x 10 spørsmål til bruk i Agderposten. 

Scriptet leser .txt filer fra mappen "unformatted" (eller annet navn gitt under) ⬇️.
Deretter lager den en formatert kopi i mappen kalt "formatted" (kan også bytte navn under) ⬆️

Noen filer slipper iblant gjennom med feil, disse blir som regel markert med "_manual" i filnavnet. 

"""

# ⬇️ This is the directory that output is placed in. 
formatted_folder_name = "formatted"

# ⬆️ This is the directory that the script reads from. 
unformatted_dir_name = "unformatted"


# This is the message generated at the top of all files that are OK
default_watermark = "Denne filen er automatisk formatert. Alltid Dobbeltsjekk. \n \n"

# This message is shown on files that needs to be fixed manually.
manual_watermark = "\n !!! \n Denne filen kunne ikke bli formatert skikkelig. \n Det er sansynligvis for mange svar fordi ett av svarende inneholder ett ',' noe sted. \n \n"




def isNotEmpty(string:str):
    return string.strip() != ""


# Takes an unformatted 20 questions filename and returns two lists of questions and answers.
def extractQnA(filename):

    with open(filename, 'r', encoding='utf-8') as file:
        
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


# Returns a list containing all .txt files that are not processed in the unformatted directory.  
def createFormattingQueue():
    
    allFiles = os.listdir(unformatted_dir_name)
    formattingQueue = []
    for file in allFiles:
        if file.endswith(".txt"):
            firstLine = open(unformatted_dir_name + "/" + file, encoding='utf-8').readline().rstrip()
            if firstLine != default_watermark or manual_watermark:
                formattingQueue.append(file)

    return formattingQueue

# Creates a new .txt file that contains two sets of questions. 
# if isManual is True, extractQnA did not manage to get the correct amount of QnAs. The file is then tagged as needing to be manually looked at. 
#    Formatting manual files are still timesaving, so it is still done, but marked as being wrong. 
def formatFile(file, isManual, questions, answers):
  
        
        if isManual:
            watermark = manual_watermark
            formatType = "manual"
        else:
            watermark = default_watermark
            formatType = "formatted"
        
        f = open(f"{formatted_folder_name}/{file.strip('.txt')}_{formatType}.txt", "w", encoding='utf-8')
        f.write(watermark)

        
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


        if isManual:
            rangeMax = len(answers)
        else: 
            rangeMax = 20

        for i in range(10, rangeMax):
            f.write(f"{i-9}. {answers[i]} \n")
        f.close()

    


def main():

    print("💬 Checking if a formatted directory exists")
    if formatted_folder_name not in os.listdir(): # crete formatted directory if it doesnt exist.
        os.mkdir(formatted_folder_name)
        print("💬 Created new formatted directory with name: " + formatted_folder_name)


    
    
    formattingQueue = createFormattingQueue() # Get all .txt files in unformatted directory.
    print(f"💬 Created queue of files to format ({len(formattingQueue)} files)")



    print(f"💬 Formatting {len(formattingQueue)} files.")

    manualCounter = 0 
    for file in formattingQueue: # 
        questions, answers = extractQnA(unformatted_dir_name + "/" + file)

        needsToBeFixedManually = len(questions) != len(answers)
        if needsToBeFixedManually: 
            manualCounter += 1

        formatFile(
                file=file,
                isManual=needsToBeFixedManually,
                questions=questions,
                answers=answers
                )
    print()
    print(f"✅ Done formatting. Resulting files in /{formatted_folder_name}")
    print(f"✨ Formatted {len(formattingQueue) - manualCounter} correctly.")
    print(f"❌ {manualCounter} files needs to be manually checked.")

main()