import os

H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')

def fb():
	print ("Akan Datang😎")


def ___menu___():
    os.system('clear')
    print ("================menu==================")
    print("01.Alat View Tiktok")
    print("02.Alat Untuk Facebook")
    
    
    ___pilih = input("input:")
    if ___pilih in ['1','01']:
        os.system('python viewbot.py')
    elif ___pilih in ['2','02']:
        fb()
    else:
        exit("%s[%s!%s]%s Wrong Input"%(M,P,M,P))
if __name__ == '__main__':
    ___menu___()