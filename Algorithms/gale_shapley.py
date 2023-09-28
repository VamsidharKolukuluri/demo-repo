import pandas as pd

# The women that men prefer
preferred_rankings_men = {
    'Ash': ['Kia', 'Luz', 'Flo', 'Jae'],
    'Bob': ['Jae', 'Flo', 'Luz', 'Kia'],
    'Del': ['Kia', 'Luz', 'Jae', 'Flo'],
    'Eli': ['Luz', 'Kia', 'Jae', 'Flo']
}

# The men that women prefer
preferred_rankings_women = {
    'Flo': ['Bob', 'Ash', 'Eli', 'Del'],
    'Jae': ['Ash', 'Eli', 'Bob', 'Del'],
    'Kia': ['Eli', 'Del', 'Ash', 'Bob'],
    'Luz': ['Del', 'Ash', 'Eli', 'Bob'],
}

# The women that men prefer
preferred_rankings_men_ = {
    'Xavier': ['Amy', 'Bertha', 'Clare'],
    'Yancey': ['Bertha', 'Amy', 'Clare'],
    'Zeus': ['Amy', 'Bertha', 'Clare']
}

# The men that women prefer
preferred_rankings_women_ = {
    'Amy': ['Yancey', 'Xavier', 'Zeus'],
    'Bertha': ['Xavier', 'Yancey', 'Zeus'],
    'Clare': ['Xavier', 'Yancey', 'Zeus']
}

# Keeps track of the people that may end up together
tentative_engagements = []

# Men who still need to propose and get accepted
free_men = []

count = 0

def init_free_men():
    for man in preferred_rankings_men:
        free_men.append(man)


def stable_matching():
    while (len(free_men) > 0):
        for man in sorted(free_men):
            begin_matching(man)


def begin_matching(man):

    # print('Dealing with %s' % (man))

    for woman in list(preferred_rankings_men[man]):
        #preferred_rankings_men[man].remove(woman)
        taken_match = [
            couple for couple in tentative_engagements if woman in couple]

        preferred_rankings_men[man].remove(woman)

        if (len(taken_match) == 0):
            print('%s proposes to %s.'%(man, woman))
            tentative_engagements.append([man, woman])
            free_men.remove(man)
            print('%s pairs with %s because she is free.' %(woman, man))

            # Remove woman from preference list once proposed.
            break

        elif (len(taken_match) > 0):
            # print('%s is taken already .. ' % (woman))
            print('%s proposes to %s.'%(man, woman))
            current_guy = preferred_rankings_women[woman].index(
                taken_match[0][0])
            potential_guy = preferred_rankings_women[woman].index(man)

            # Remove woman from preference list once proposed.
            #preferred_rankings_men[man].remove(woman)

            if (current_guy < potential_guy):
                print('%s rejects %s because she likes her current match, %s, more.' % (woman, man, taken_match[0][0]))
                print('%s remains free.'%(man))
            else:
                print('%s dumps %s and pairs with %s.' % (woman, taken_match[0][0], man))
                print('%s becomes free.' % (taken_match[0][0]))

                # The new guy is engaged
                free_men.remove(man)

                # The old guy is now single
                free_men.append(taken_match[0][0])

                # Update the guy
                taken_match[0][0] = man
                break


def main():
    init_free_men()
    stable_matching()

    df = pd.DataFrame(tentative_engagements)
    print('\nNow everyone has a match. Here are the matches:')
    df.columns = ['MEN', 'WOMEN']
    print(df)


if __name__ == "__main__":
    main()