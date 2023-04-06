#!/usr/bin python3
# Contributors: vipa | Datura Data Group

########################################################

# Testing for User Imports
try:
    import pandas as pd
    import time
    import matplotlib.pyplot as plt
    import sys
    import subprocess
except ImportError:
    print('''[-] Manually installing required modules...\n
    [-] This can also be performed via command 'python3 -m pip install -r requirements' within your terminal!''')
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pandas'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'time'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'matplotlib.pyplot'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'sys'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'subprocess'])
    pass
finally:
    print("[-] Requirements have been installed!")
    pass

# Globals
user_input = input("Filename:\t")
if ".csv" in user_input:
    file = user_input
else:
    file = user_input + ".csv"


# Main Function
def main(file):
    try:
        # Pandas CSV Interpreter  | Display
        print("[-] Analyzing data set...")
        df = pd.read_csv(file)
        df.dropna(inplace=True)
        print(df.to_string())
        df.plot()  # Formatting to process matlib graph
        plt.show()  # Matlib graph


    except SyntaxError as e:
        print("[!] SYNTAX ERROR - EXITING... Read the docs. SMH.")
        time.sleep(3)
        exit()


main(file)
