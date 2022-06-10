import time


class setColours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCLYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD  = '\033[1m'
    UNDERLINE = '\033[4m'

time.sleep(0.5)
print(bc.OKGREEN +
    "Test 1 passed" + 
    bc.ENDC)

time.sleep(0.5)
print(bc.OKGREEN +
    "Test 2 passed" + 
    bc.ENDC)

time.sleep(0.5)
print(bc.OKGREEN +
    "Test 3 passed" + 
    bc.ENDC)


