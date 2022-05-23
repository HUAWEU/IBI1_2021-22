<<<<<<< HEAD
def nucleotide_content_calculator(i):
    """
    input: i , a single string
    returns the percentage of nucleotides
    """
    upper = i.upper()
    a = 0
    t = 0
    c = 0
    g = 0
    for m in range(0,len(upper)):
        x = upper[m]
        if x == "A":
            a += 1
        if x == "T":
            t += 1
        if x == "C":
            c += 1
        if x == "G":
            g += 1

    percentagea = "A%" + "=" + str((a/len(upper))*100)
    percentaget = "T%" + "=" + str((t/len(upper))*100)
    percentagec = "C%" + "=" + str((c/len(upper))*100)
    percentageg = "G%" + "=" + str((g/len(upper))*100)
    print(percentagea)
    print(percentaget)
    print(percentagec)
    print(percentageg)


DNA = "ATCGACGTACTGACGTacgt"
=======
def nucleotide_content_calculator(i):
    """
    input: i , a single string
    returns the percentage of nucleotides
    """
    upper = i.upper()
    a = 0
    t = 0
    c = 0
    g = 0
    for m in range(0,len(upper)):
        x = upper[m]
        if x == "A":
            a += 1
        if x == "T":
            t += 1
        if x == "C":
            c += 1
        if x == "G":
            g += 1

    percentagea = "A%" + "=" + str((a/len(upper))*100)
    percentaget = "T%" + "=" + str((t/len(upper))*100)
    percentagec = "C%" + "=" + str((c/len(upper))*100)
    percentageg = "G%" + "=" + str((g/len(upper))*100)
    print(percentagea)
    print(percentaget)
    print(percentagec)
    print(percentageg)


DNA = "ATCGACGTACTGACGTacgt"
>>>>>>> e22e09b592cc8a054107ad38ad83d7f407d9cd31
nucleotide_content_calculator(DNA)