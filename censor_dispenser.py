# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("/Users/diallo/Downloads/censor_dispenser/email_one.txt", "r").read()
email_two = open("/Users/diallo/Downloads/censor_dispenser/email_two.txt", "r").read()
email_three = open("/Users/diallo/Downloads/censor_dispenser/email_three.txt", "r").read()
email_four = open("/Users/diallo/Downloads/censor_dispenser/email_four.txt", "r").read()
# with open("/Users/diallo/Downloads/censor_dispenser/email_two.txt", "r")as myfile:
#     email_two = myfile.read()

# word='learning algorithms'
# def censor(word, email_one):
#     if word in email_one:
#         return email_one.replace(word, '')
# print(censor(word, email_one))


proprietary_terms = ["she","personality matrix", "sense of self","share", "self-preservation", "learning algorithm", "her", "herself"]


# def censor_2(proprietary_terms,email_two):
#     for term in range(0, len(proprietary_terms)):
#         length = len(proprietary_terms[term])
#         email_two=email_two.replace(proprietary_terms[term], ''*length)
#     return email_two
#
# print(censor_2(proprietary_terms, email_two))


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_3(proprietary_terms,negative_words, email_three):
    for term in range(0, len(proprietary_terms)):
        length = len(proprietary_terms[term])
        email_two=email_three.replace(proprietary_terms[term], ''*length)
    return email_three

    for word in range(0, len(negative_words)):
        length_words = len(negative_words[word])
        for word_email in range(0, len(email_three[word_email])):
            if negative_words[word] in email_three[word_email] and email_three[word_email]-1 == negative_words[word]:
                email_three = email_three.replace(negative_words[word], '#' * length)
    return email_three


print(censor_3(proprietary_terms, negative_words, email_three))
