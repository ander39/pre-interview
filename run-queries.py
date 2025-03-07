import os
import subprocess

QUERY_FOLDER = "C:/Users/willj/git/pre-interview/queries"
SOLVER_PATH = "C:/Users/willj/git/cvc5-Win64-x86_64-static/bin"

for query_file in os.listdir(QUERY_FOLDER):     #loops through all query files in the "queries" folder
    #print(query_file)
    result = subprocess.run(["executable",query_file], capture_output=True, text=True, check=True)
    print(result)

