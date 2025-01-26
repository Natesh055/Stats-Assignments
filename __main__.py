import numpy as np
import pandas as pd
import argparse

def step1(dec_matrix):
    sqrtSum = np.sqrt(np.sum(np.square(dec_matrix), axis=0))
    dec_matrix = dec_matrix / sqrtSum
    return dec_matrix

def step2(dec_matrix, weights):
    return dec_matrix * weights

def step3a(dec_matrix, impact):
    col = len(dec_matrix[0])
    minValues = np.min(dec_matrix, axis=0)
    maxValues = np.max(dec_matrix, axis=0)

    idealSol = np.zeros(col)
    for i in range(0, col):
        if impact[i] == 1:
            idealSol[i] = maxValues[i]
        else:
            idealSol[i] = minValues[i]
    return idealSol

def step3b(dec_matrix, impact):
    col = len(dec_matrix[0])
    minValues = np.min(dec_matrix, axis=0)
    maxValues = np.max(dec_matrix, axis=0)

    negIdealSol = np.zeros(col)
    for i in range(0, col):
        if impact[i] == 1:
            negIdealSol[i] = minValues[i]
        else:
            negIdealSol[i] = maxValues[i]
    return negIdealSol

def step4a(idealSol, dec_matrix):
    return np.sqrt(np.sum(np.square(dec_matrix - idealSol), axis=1))

def step4b(negIdealSol, dec_matrix):
    return np.sqrt(np.sum(np.square(dec_matrix - negIdealSol), axis=1))

def step5(idealSol, negIdealSol):
    return negIdealSol / (idealSol + negIdealSol)

def topsisCalc(dec_matrix, weights, impacts):
    dec_matrix = step1(dec_matrix)
    dec_matrix = step2(dec_matrix, weights)
    idealSol = step3a(dec_matrix, impacts)
    negIdealSol = step3b(dec_matrix, impacts)
    eucIdeal = step4a(idealSol, dec_matrix)
    eucNonIdeal = step4b(negIdealSol, dec_matrix)
    relClos = step5(eucIdeal, eucNonIdeal)
    print("BEST DECISION: ", np.max(relClos), "\n")
    print("WORST DECISION: ", np.min(relClos), "\n")

def main(args):
    # Read decision matrix from Excel file
    df = pd.read_excel(args["InputDataFile"])
    dec_matrix = df.iloc[:, 1:].to_numpy()  # Assuming the first column is 'Fund Name' and rest are numeric
    
    # Parse the weights and impacts as numpy arrays
    weights = np.array([float(w) for w in args["Weights"][0].split(',')])
    impacts = np.array([int(i) for i in args["Impacts"][0].split(',')])

    topsisCalc(dec_matrix, weights, impacts)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("InputDataFile", help="Enter the name of Excel file with .xlsx extension", type=str)
    parser.add_argument("Weights", nargs=1, help="Enter the weight vector comma separated", type=str)
    parser.add_argument("Impacts", nargs=1, help="Enter the impact vector comma separated", type=str)
    args = parser.parse_args()
    
    main(vars(args))
