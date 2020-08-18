import sys
if not sys.version_info[0] >= 3:
    print("This script is compatible with python 3.x. Please upgrade your python version and retry")
    sys.exit(0)

#checking whether google translate python library is installed or not
try:
    from googletrans import Translator

except Exception:
    print("This script requires installation of Google translate API. Please install the API using 'pip install googletrans' \n You can check it out by opening this link in your browser \n https://pypi.org/project/googletrans/")
    sys.exit(0)

translator = Translator()

def main():
    
    #File input 
    filename = input("Enter full name of your document (including extension): ")
    print("___________________________________________________________________________________________________")

    # Opening input file
    with open(filename, 'r') as f:
        content = f.read()

    #Using google translate to translate contents repeatedly. The 3 most accurate languages that google can translate (Source:https://www.tomedes.com/business-center/language-Google-Translate-translate#:~:text=The%20best%20was%20Afrikaans%2C%20followed,once%20more%20topping%20the%20table) were chosen
    afrikaans = translator.translate(content, src='en', dest='af')
    german = translator.translate(afrikaans.text, src='af', dest='de')
    spanish = translator.translate(german.text, src='de', dest='es')
    english = translator.translate(spanish.text, src='es', dest='en')

    #Showing input and output on command line
    print(" Original Content: \n{}".format(content))
    print("\n\n New Content: \n{}".format(english.text))

    #Creating a new file that contains output
    new = filename.split(".")
    new_filename = new[0] + "_output.txt"

    # Writing the New Content in Output File
    with open(new_filename, 'w') as a:
        a.write(english.text)
    print("\n Output File: {}".format(new_filename))


if __name__ == "__main__":
    main()

