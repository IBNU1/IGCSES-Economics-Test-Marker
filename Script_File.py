""" This is a script devloped in order to aid students in calculating their
projected grade based on a mocks for the final igcses exam after weighing the grade
"""
import sys
grade_list_score = {"A*":124,"A":95,"B":84,"C":65,"D":54,"E":40,"F":35,"G":28}
grade_lists = ["A*","A","B","C","D","E","F","G"]
mcq_weight = 1.5
sq_weight = 1.16666
def econ_weighing(mcq_score,sq_score) :
    mcq_adjusted_score = mcq_score * mcq_weight
    sq_adjusted_score = sq_score * sq_weight
    return mcq_adjusted_score + sq_adjusted_score

print(20 * "*")
print("""This is a computer script made by an IGCSE Economics student designed
to be used by students to make calcuating their final grade from mock tests
easier by automaticaly weighing the grades and compareing it to the threshold
table""")
print("Direct all feedback to my Github-Account https://github.com/IBNU1")
print("""PS: This program only works if the MCQ paper was out of 30 and
the Structured questions were out of 90""")
print(20 * "*")
print("What was your score for the MCQ(Multiple-Choice) section of the test ?")
mcq = float(input("> "))
print("What was your score for the structured questions section of the test ?")
sq = float(input("> "))
final_score = econ_weighing(mcq,sq)
print("Your final adjusted score is " + str(round(final_score,0)))
for grade in grade_lists :
    if final_score > grade_list_score[grade] :
        print("Your Grade for the mocks test is " + grade)
        sys.exit(0)
print("You failed the test, my conolences")
