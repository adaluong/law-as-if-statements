def homicide():
    death = input("is there a death? yes/no: ").lower()
    if death == 'yes':
        act_causing_death()
    elif death == 'no':
        print('not homicide')
    else:
        homicide()

def act_causing_death():
    caused = input("is there an act causing death? yes/no: ")
    if caused == 'yes':
        if voluntary_act():
            return True
        else:
            return False
    elif caused == 'no':
        return False
    else:        
        act_causing_death()

def voluntary_act():
    print("act needs to be voluntary and willed and not an accident")
    print('see Barwick in Ryan')
    

def murder_mens_rea():
    print("intent to kill")
    print("intent for grievous bodily harm")
    print("reckless indifference to human life")
    print("constructive murder - attempting during or after 25 year crime")

    option = input("enter option: ")
    if option in ['d', 'constructive murder']:
        constructive_murder()

def constructive_murder():
    print('during attempt of a 25 year crime')
    print("has its own AR/MR - have to prove that")

# MANSLAUGHTER

def manslaughter():
    # actus reus
    
    unlawful_and_dangerous_act()
    criminal_negligence()

    manslaughter_mens_rea()

def unlawful_and_dangerous_act():
    if (unlawful() and dangerous()):
        return True
    else:
        return False

def unlawful():
    criminal_offence = input("is it a criminal offence (base of AR/MR). yes/no: ")
    if criminal_offence == 'yes':
        return True
    if criminal_offence == 'no':
        return False
    else:
        unlawful()
    
def dangerous():
    dangerous = input("is it a dangerous act according to the judge? yes/no: ").lower()
    appreciable_risk_of_serious_harm = input("would an objective reasonable person in the accused's position appreciate that it's dangerous according to the jury? yes/no: ").lower()
    
    if dangerous not in ['yes','no'] or reasonable_person not in ['yes','no']:
        print('answers need to be yes or no')
        dangerous()

    if dangerous == 'yes' and appreciable_risk_of_serious_harm == 'yes':
        return True
    else:
        return False
    

if __name__ == '__main__':
    homicide()