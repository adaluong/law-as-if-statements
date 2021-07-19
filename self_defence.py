"""
a lot of law is lowkey just if statements
proof of concept 
by ada luong, july 2021, 1:27am

criminal law: murder + self defence
use at ur own risk
"""

def main():
    print("HELLO. YOU HAVE BEEN CHARGED WITH MURDER.")
    print("IS THERE A DEFENCE OF SELF-DEFENCE HMMMM")

    if (subjective_belief_test() == False):
        print("RIP you are a MURDERER")
    else:
        purpose = purpose_of_killing()
        verdict = reasonable_conduct(purpose)
    return

def subjective_belief_test():
    subjective_belief = input("Did you actually believe that the conduct was necessary? ").lower()
    if (subjective_belief == 'no'):
        return False
    if (subjective_belief == 'yes'):
        return True
    else:
        print("Sorry, enter 'yes' or 'no'")
        subjective_belief_test()

def purpose_of_killing():
    print("Why did you kill the person? ")
    print("a: to defend yourself or another person")
    print("b: to stop imprisonment")
    print("c: to protect property")
    print("d: to stop trespass")
    return input("option: ").lower()

def reasonable_conduct(purpose_of_killing):
    reasonableness = input("Was the conduct objectively reasonable in the circumstances that the accused was in? ").lower()
    if reasonableness not in ['yes', 'no']:
        print("Enter 'yes' or 'no'")
        reasonable_conduct(purpose_of_killing)

    if reasonableness == 'yes':
        print("YOU HAVE BEEN ACQUITED. FREE TO GO!!! YEET")
    elif purpose_of_killing in ['a','b']:
        print("Alright, you're guilty of MANSLAUGHTER")
    elif purpose_of_killing in ['c', 'd']:
        print("GG you're a murderer")
    else:
        print("IDK you entered something wrong")
    return

if __name__ == '__main__':
    main()