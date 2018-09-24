CORD_C = ["C", "Dm", "Em", "F", "G", "Am"]
CORD_D = ["D", "Em", "F#m", "G", "A", "Bm"]
INPUT = [["G", "C", "Em", "Em"], ["Am", "F", "Dm", "G"], ["Dm", "Dm", "Am", "Am"], ["C", "Em", "G", "F"], ["G", "C", "Am", "Em"], ["Am", "Am", "F", "G"], ["F", "Am", "Dm", "Em"], ["G", "C", "Am", "Am"], ["G", "F", "Em", "F"], ["F", "Em", "Am", "Am"], ["Em", "G", "C", "G"], ["G", "C", "Am", "Am"], ["Dm", "C", "C", "F"], ["Dm", "Am", "F", "C"], ["G", "Dm", "Em", "C"], ["G", "C", "Am", "G"], ["F", "F", "F", "Em"], ["Dm", "Em", "F", "Em"], ["F", "F", "G", "G"], ["Dm", "Em", "Dm", "Dm"], ["Em", "C", "Em", "C"], ["Dm", "F", "F", "Dm"], ["C", "Am", "F", "G"], ["G", "G", "G", "C"], ["Dm", "Em", "G", "F"], ["Dm", "Dm", "Am", "C"], ["G", "C", "G", "Dm"], ["Em", "Dm", "G", "F"], ["Em", "Am", "F", "G"], ["Dm", "F", "Em", "Am"], ["C", "C", "Am", "Em"], ["G", "Am", "Am", "C"], ["Dm", "Dm", "C", "Dm"], ["Dm", "Em", "Dm", "Dm"], ["Em", "Am", "Am", "C"], ["F", "F", "Am", "F"], ["C", "F", "Am", "F"], ["Dm", "C", "G", "F"], ["C", "Em", "Am", "G"], ["G", "Dm", "C", "C"], ["Dm", "C", "Em", "Dm"], ["Am", "G", "C", "Dm"], ["F", "G", "F", "Am"], ["F", "Am", "F", "G"], ["Em", "F", "C", "F"], ["Em", "F", "C", "F"], ["C", "G", "Em", "Em"], ["Em", "G", "C", "Dm"], ["F", "Dm", "Dm", "Em"], ["Am", "F", "C", "G"]]
OUTPUT = ""
for row in range(len(INPUT)):
    for i in range(len(INPUT[row])):
        Position_CORD = CORD_C.index(INPUT[row][i])
        OUTPUT += CORD_D[Position_CORD] + " "
    
    OUTPUT += "\n"

print(OUTPUT)