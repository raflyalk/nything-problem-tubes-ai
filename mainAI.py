import geneticalgorithm
import SimulatedAnnealing
import State
import hillClimbing

def input_pawn(fname):
    with open(fname) as f:
        getLine = f.readlines()
    
    pawnInput = []
    for line in getLine :
        dataPawn = line.split(" ")
        if (dataPawn[0] == "WHITE"):
            if (dataPawn[1]=="KNIGHT"):
                pawnInput.append({'pawnType': 'K','pawnCount': int(dataPawn[2])})
            elif (dataPawn[1]=="BISHOP"):
                pawnInput.append({'pawnType': 'B','pawnCount': int(dataPawn[2])})
            elif (dataPawn[1]=="ROOK"):
                pawnInput.append({'pawnType': 'R','pawnCount': int(dataPawn[2])})
            else :
                pawnInput.append({'pawnType': 'Q','pawnCount': int(dataPawn[2])})
        else :
            if (dataPawn[1]=="KNIGHT"):
                pawnInput.append({'pawnType': 'k','pawnCount': int(dataPawn[2])})
            elif (dataPawn[1]=="BISHOP"):
                pawnInput.append({'pawnType': 'b','pawnCount': int(dataPawn[2])})
            elif (dataPawn[1]=="ROOK"):
                pawnInput.append({'pawnType': 'r','pawnCount': int(dataPawn[2])})
            else :
                pawnInput.append({'pawnType': 'q','pawnCount': int(dataPawn[2])})
    return pawnInput

def main() :
    print("\n▀ ▄ ░ ▀ ▄ ░     █▀▀▄ ░ ░ █░░█ ▀▀█▀▀ █░░█ ░▀░ █▀▀▄ █▀▀▀     ░ ▄ ▀ ░ ▄ ▀")
    print("░ ░ █ ░ ░ █     █░░█ ▀ ▀ █▄▄█ ░░█░░ █▀▀█ ▀█▀ █░░█ █░▀█     █ ░ ░ █ ░ ░")
    print("▄ ▀ ░ ▄ ▀ ░     ▀░░▀ ░ ░ ▄▄▄█ ░░▀░░ ▀░░▀ ▀▀▀ ▀░░▀ ▀▀▀▀     ░ ▀ ▄ ░ ▀ ▄\n")
    fname = input("Masukan Nama File Input Bidak Catur : ")
    pawnInput = input_pawn(fname)
    print("Pilih Algoritma local search yang digunakan"),
    print("1. Hill Climbing")
    print("2. Simulated Annealing")
    print("3. Genetic Algorithm\n")
    str = input(">> Pilihan: ")
    while(not(int(str)==1 or int(str)==2 or int(str)==3)):
        print("Masukan Salah !")
        str = input(">> Pilihan: ")
    if (int(str) == 1) :
        print ("\n-- Solusi Hill Climbing --")
        finalState = hillClimbing.main(pawnInput)
    elif (int(str) == 2) :
        print ("\n-- Solusi Simulated Annealing --")
        finalState = SimulatedAnnealing.main(pawnInput)
    else :
        print ("\n-- Solusi Genetic Algorithm --")
        finalState = geneticalgorithm.main(pawnInput)
    print('\n')
    finalState.printChessBoard()
    print(finalState.sameColorCost, finalState.diffColorCost)
if __name__ == '__main__' :
    main()