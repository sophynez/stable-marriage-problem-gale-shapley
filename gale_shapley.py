M = ['John', 'Joe', 'Ali', 'Ben', 'Sam']
W = ['Marie', 'Aya', 'Ellie', 'Lin', 'Eva']

men_preferences = {'Ali': ['Marie', 'Aya', 'Ellie', 'Lin', 'Eva'],
                   'Joe': ['Lin', 'Marie', 'Ellie', 'Aya', 'Eva'],
                   'Sam': ['Marie', 'Eva', 'Lin', 'Ellie', 'Aya'],
                   'Ben': ['Eva', 'Ellie', 'Aya', 'Lin', 'Marie'],
                   'John': ['Marie', 'Aya', 'Lin', 'Ellie', 'Eva']}

women_preferences = {'Marie': ['Ali', 'Joe', 'Sam', 'Ben', 'John'],
                     'Aya': ['Ali', 'Sam', 'Joe', 'John', 'Ben'],
                     'Ellie': ['John', 'Joe', 'Sam', 'Ben', 'Ali'],
                     'Lin': ['Ali', 'Ben', 'John', 'Sam', 'Joe'],
                     'Eva': ['Ben', 'John', 'Sam', 'Ali', 'Joe']}

matched = []
partners = []


def get_current_match(person, partner_list):
    for i in partner_list:
        if i[0] == person:
            return i[1]


def check_preferences(person1, person2, preference_order):
    """
    return true is person1 is more preferable than person2, else return false
    we use indexes to compare, the littlest the index, the more the preference
    """
    p1 = preference_order.index(person1)
    p2 = preference_order.index(person2)

    if p1 < p2:
        return True
    return False


def change_partners(partners_list, person, new_partner):
    """
    this function return the ex partner (the one getting changed), and makes the swap between new-ex partners
    return ex partner
    """
    tmp = [list(x) for x in partners_list]
    for i in tmp:
        if i[0] == person:
            old_partner = i[1]
            i[1] = new_partner
            break
    partners_list = [tuple(x) for x in tmp]
    return partners_list, old_partner


# while there are unmatched men :
while M:
    print("-- The list of single unmatched men", M)
    for man in M:
        # print("-- The list of single unmatched men", M)
        print("Current man : ", man)
        prospect = men_preferences[man][0]  # his first preference
        print("current prospect of the man : ", prospect)
        print("List of matched women :", matched)
        if prospect not in matched:
            print(f'{prospect} not matched yet, match her with {man}')
            # if the woman has not been matched, then we should pair them up
            # if she has been matched, check if this man is more preferable to her than her current match
            # Here she is not matched already, so match them up
            matched.append(prospect)
            partners.append((prospect, man))
            # also remove the woman from the preferences of the man, he cannot propose to her again, either because she's already matched with someone else, or she already rejected him
            men_preferences[man].remove(prospect)
            # since the man has found a match, remove him from the list of man because we iterate as long as the list if not empty; there are still men who did not find a match
            M.remove(man)
            print(" - Lists updated")
            print(M)
            print(matched)
            print(partners)
            break
        else:  # here the woman has already been matched
            # check if the current man is more preferable to the woman than her current match
            # if the current man is more preferable, change her match, and return the man to the list of men (not matched again)
            print(f'{prospect} is already matched :(, see if she would jest her current match')
            prospects_match = get_current_match(prospect, partners)
            print(f'current match of {prospect} is {prospects_match}')
            print(f'would {prospect} jest {prospects_match} for {man} ? : {check_preferences(man, prospects_match, women_preferences[prospect])}')
            # now it's man VS prospects_match
            if check_preferences(man, prospects_match, women_preferences[prospect]):
                # here the man is more preferable to the woman than her current_match
                # match her with the man, put back the ex match in the list of man, and remove the man from the list (life's unfair, but well oh well)
                partners, ex_partner = change_partners(partners, prospect, man)
                M.append(ex_partner)
                M.remove(man)
                print(" - Lists updated")
                print(M)
                print(matched)
                print(partners)
            else:
                # here the man is not preferable to the woman, so we remove the woman from the man's list, and continue on
                print(f'{prospect} did not jest {prospects_match} for {man}, {man} will have to move on to the next one in his preference list')
                men_preferences[man].remove(prospect)
                sorry_dude = M.pop(0)
                M.append(sorry_dude)
                print(" - Lists updated")
                print(M)
                print(matched)
                print(partners)
                break

# [('Marie', 'Ali'), ('Lin', 'Sam'), ('Eva', 'Ben'), ('Aya', 'John'), ('Ellie', 'Joe')]
