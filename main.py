#! /usr/bin/env python3
# coding: utf-8


import function as f
import logging as lg

def main():
    """Main function that is used as a menu to create the groups"""
    print("Who are the participants?")
    participant1 = input()

    f.add_participants(participant1)

    print(f.participants)

    f.add_more_participants()

    print(f.participants)

    print("Do you want to add a skill?")

    print(f.add_competence())

try :
    if __name__ == "__main__":
        main()
except :
    lg.error("Impossible to run main")

