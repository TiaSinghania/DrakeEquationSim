print("The Drake Equation takes in hypothetical values for various parameters and uses them to calculate how many alien civilizations capable of communicating with Earth we should be able to detect. \n Try out values of your own to judge how alone we might truly be in the universe.\n")

loop = True
while loop:
    R_star = input("Rate of star formation (stars/ year): ")
    f_planet = input("Fraction of stars with planets (value between 0 and 1): ")
    n_habitable = input("Number of habitable planets per system (number): ")
    f_life = input("Fraction of habitable planets that developed life (value between 0 and 1): ")
    f_intel = input("Fraction of planets that developed life that developed intelligence (value between 0 and 1): ")
    f_comm = input("Fraction of intelligent civilizations that are capable of communicating with us (value between 0 and 1): ")
    L_time = input("How long such a civilization capable of communication remains alive (time in years): ")

    N = R_star * f_planet * n_habitable * f_life * f_intel * f_comm * L_time
    print("With those parameters, there should be " + N + " civilizations capable of communicating with Earth\n")

    loop = 'F' == input("Try more values? (T/F)")

