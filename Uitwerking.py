def read_tsv(bestandsnaam):
    """

    :param bestandsnaam:
    :return:
    """
    genfamilies = []
    with open(bestandsnaam, encoding="UTF8") as inFile:
        next(inFile)
        for line in inFile:
            line = line.split("\t")
            print("*************************************")
            print("Naam:", line[2])
            if "p" in line[6]:
                chr = line[6].split("p")[0]
            elif "q" in line[6]:
                chr = line[6].split("q")[0]
            print("Chromosoom:", chr)
            print("Familie:", line[12])
            genfamilies.append(line[12])
    return genfamilies


def genfamilies_uniek(genfamilies):
    unieke_genfamilies = []
    for g in genfamilies:
        if g not in unieke_genfamilies:
            unieke_genfamilies.append(g)
    print("Unieke genfamilies:", ", ".join(unieke_genfamilies))
    return unieke_genfamilies


def genfamilies_counter(genfamilies, unieke_genfamilies):
    counter = 0
    for ug in unieke_genfamilies:
        for g in genfamilies:
            if ug == g:
                counter += 1

        print(ug, "komt zo vaak voor:", counter)



def main():
    bestandsnaam = "RNA_long_non-coding.tsv"
    genfamilies = read_tsv(bestandsnaam)
    print("*************************************")
    print("*************************************")
    unieke_genfamilies = genfamilies_uniek(genfamilies)
    print("*************************************")
    print("*************************************")
    genfamilies_counter(genfamilies, unieke_genfamilies)
    print("*************************************")


main()