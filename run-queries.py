import os
import subprocess
import csv

QUERY_FOLDER = "queries"
SOLVER_PATH = "cvc5"

for query_file in os.listdir(QUERY_FOLDER):     #loops through all query files in the "queries" folder
    print(query_file)
    query_path = os.path.join(QUERY_FOLDER, query_file) #gets the full path of the current smt file
    result = subprocess.run([SOLVER_PATH, "--tlimit=60000", query_path], text=True, capture_output=False) #This runs the solver on the current file
    print(result)


    #need code to write the result to a list or directly to a csv

