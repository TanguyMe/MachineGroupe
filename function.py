import random as rd
import logging as lg

participants=[]

def add_participants(x):
    return participants.append(x)


def question_participant():
    print("Another one more participant?")
    return input()


def add_more_participants():
    """Function that asks if he want to add one more participant"""
    try:
        while question_participant() == 'yes':
            print("Who are the participants?")
            new_participant = input()
            add_participants(new_participant)
            print(participants)
    except :
        lg.warning("Impossible to add more participants")


def person_number(participants):
    """Function that asks a number and return this number checking if it is a valid person number"""
    print("Entrez le nombre de personnes par groupe :")
    num_to_select_input = input()  # Demande un chiffre
    try:
        while not num_to_select_input.isdigit() or int(num_to_select_input) > len(participants) // 2 or int(
                num_to_select_input) <= 1:  # Vérifie que l'utilisateur a bien rentré un chiffre valide
            if not num_to_select_input.isdigit():  # Cas où l'entrée n'est pas un chiffre
                print("Entrez le nombre de personnes par groupe EN CHIFFRE :")
                num_to_select_input = input()  # Demande un nouveau chiffre
            elif int(num_to_select_input) > len(
                    participants) // 2:  # Cas où le chiffre est trop grand (génèrerait qu'un seul groupe)
                print("Nombre invalide : Trop grand")
                print("Entrez le nombre de personnes par groupe :")
                num_to_select_input = input()  # Demande un nouveau chiffre
            elif int(num_to_select_input) <= 0:  # Cas où le nombre est négatif ou égal à 1
                print("Nombre invalide : Trop petit")
                print("Entrez le nombre de personnes par groupe :")
                num_to_select_input = input()  # Demande un nouveau chiffre
            else:
                break
        return (int(num_to_select_input))  # Renvoie le nombre entré
    except :
        lg.error("Impossible to return a number of participants by group")


def p_aleatoire(participants):
    """Function that return a list group randomly made with list participants"""
    num_to_select = person_number(participants)
    num_of_group = len(participants) // num_to_select
    group = []
    try:
        for i in range(num_of_group):  # On itere autant de fois qu'on veut de groupes
            if len(participants) >= num_to_select:  # Permet de vérifier qu'il y a assez de personnes pour un groupe complet
                group.append(rd.sample(participants,
                                       num_to_select))  # On ajoute un groupe de personnes tirées aléatoirement à une liste
                for j in range(
                        num_to_select):  # On itere autant de fois qu'il y a de personnes qui viennent d'être assignées à un groupe
                    participants.remove(group[i][j])  # On enleve les personnes qu'on vient de grouper de la liste de départ
            else:
                break  # Arrête d'essayer de créer des groupes si il ne reste plus assez de personnes

        for k in range(len(participants)):  # On regarde s'il reste des personnes dans le groupe participants
            group[k % len(group)].append(participants[
                                             k])  # On les répartit 1 par 1 dans les groupes déjà existants (k%len pour par exemple groupes de 4 avec 11 personnes : on veut que répartir dans les 2 groupes déjà existants)
        print(group)
        return group
    except :
        lg.error("Impossible to create the groups randomly")


def add_competence():
    """Function that asks if we want to add skill as a parameter or not"""
    skill = input()
    if skill == 'yes':
        return question_niveau()
    else:
        return p_aleatoire(participants)


def a_competence(participants):
    """Function that asks the user to write the mark of each participant and add it in a dico"""
    dico = {}
    try:
        for participant in participants:
            print("Quelle est la note de {}(1 à 5)".format(participant))
            dico[participant] = input()
        return dico
    except :
        lg.error('Impossible to add the mark')


def question_niveau():
    """Function that ask if we want to share the group by equal or not level"""
    print("Do you want to share by equal levels?")
    resp = input()
    if resp == 'yes':
        return p_meme_niveau(participants)
    else:
        return p_aleatoire(participants)


def p_meme_niveau(participants):
    """Function that return a list of group made with an equal level from list participants"""
    num_to_select = person_number(participants)
    num_of_group = len(participants) // num_to_select
    group_p = []
    try :
        p_2 = sorted(a_competence(participants).items(),
                 key=lambda t: t[1])  # Trie la liste des apprenants en fonction des notes
        for i in range(num_of_group):  # On itere autant de fois qu'on veut de groupes
            if len(p_2) - len(
                    group_p) * num_to_select >= num_to_select:  # Permet de vérifier qu'il y a assez de personnes pour un groupe complet
                group_p.append([])
                for j in range(
                        num_to_select):  # On itere autant de fois qu'il y a de personnes qui viennent d'être assignées à un groupe
                    group_p[i].append(p_2[i * num_to_select + j][0])
            else:
                break  # Arrête d'essayer de créer des groupes si il ne reste plus assez de personnes

        for k in range(len(participants) - len(
                group_p) * num_to_select):  # On regarde s'il reste des personnes dans le groupe participants
            group_p[-1 - k % len(group_p)].append(p_2[-1 - k][
                                                      0])  # On les répartit 1 par 1 dans les groupes déjà existants en commençant par les plus proches en niveau (k%len pour par exemple groupes de 4 avec 11 personnes : on veut que répartir dans les 2 groupes déjà existants)
        return group_p
    except :
        lg.error("Impossible to create the groups by level ")
