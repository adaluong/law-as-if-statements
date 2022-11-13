def assault():
    if assault_actus_reus() and assault_mens_rea():
        coincidence()
        print("assault case exists")
    else:
        print("no assault. try stalking/intimidation offence")

def assault_actus_reus():
    print("""
    IDENTIFY THE ACTUS REUS
    """)
    positive_act = input("Is there a voluntary act, not omission (Fagan). yes/no: ").lower()
    if positive_act not in ['yes', 'no']:
        assault_actus_reus()
    elif positive_act == 'no':
        return False

    print("\nBATTERY: unlawful physical contact / application of force to a person + unlawful")
    print("ASSAULT: act creating an apprehension/fear of immediate personal violence")
    act = input("battery or assault? ")

    if act == 'battery':
        print("\nneeds to be WITHOUT CONSENT")
        print("can't consent to actual bodily harm")
        print("recognised category of exceptions: boxing, tatooing, sports...")
        unlawful = input("unlawful? yes/no: ").lower()
        if unlawful == 'yes':
            return True
        elif unlawful == 'no':
            return False
        else: assault_actus_reus()

    elif act == 'assault':
        print("\nhow imminent? (Knight, Zanker)")
        print("no need for reasonable fear (Mostyn)")
        print("consider stalking or intimidation offence too")
        return True

def assault_mens_rea():
    print("""
    IDENTIFY THE MENS REA
    """)
    print("INTENTION to effect unlawful contact or create apprehension of imminent unlawful contact")
    print("RECKLESS (knowledge or forsight of POSSIBILITY) as to whether their actions would effect unlawful contact or create apprehension of imminent unlawful contact (Macpherson)")
    mr = input("intention, reckless (foresight of possibility), or negligence? ")
    if mr == 'intention':
        print("i.e. intention to touch or create fear")
        return True
    elif mr == 'reckless':
        print("case-by-case: murder is 'probability', sexual assault is 'failure to think'")
        return True
    elif mr == 'negligence':    
        print("negligence is insufficient (MacPhereson v Brown)")
        return False
    else:
        assault_mens_rea()

def coincidence():
    print("note: actus reus must coincide with mens rea (Fagan)")

if __name__ == '__main__':
    assault()