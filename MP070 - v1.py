def BinaryInput():
    BinaryValue = input('Enter the binary number: ')
    Check = 0
    Status = False
    while Status == False:
        Length = len(BinaryValue)
        try:
            BinaryValue = int(BinaryValue)
            if Length >0 and Length%4 == 0:
                BinaryValue2 = str(BinaryValue)
                Check = 1
                for index in range(Length):
                    if BinaryValue2[index] != '1' and BinaryValue2[index] != '0':
                        
                        Check = 0
            else:
                Check = 2
        except:
            print('Must enter Integers')
            BinaryValue2 = str(BinaryValue)
            if BinaryValue2[0] == '0':
                Check = 1
        if Check == 1:
            Status = True
        else:
            if Check == 2:
                print('Length or binary number must not be 0 and must be divisible by 4')
                BinaryValue = input('Reenter the binary number: ')
            else:
                print('Number can only contain 1s or 0s')
                BinaryValue = input('Reenter the binary number: ')
            
    return BinaryValue


def BinaryToDenary(BinaryValue):
    BinaryValue = str(BinaryValue)
    List = list(BinaryValue)
    List.reverse()
    Length = len(BinaryValue)
    DenaryValue = 0
    for index in range(Length):
        NumberofIndex = List[index]
        Number = int(NumberofIndex)
        Working = Number * (2**(index))
        DenaryValue = DenaryValue + Working
    return DenaryValue


def DenaryInput():
    DenaryValue = input('Enter the Denary number: ')
    Check = False
    Status = False
    while Status == False:
        Length = len(DenaryValue)
        try:
            DenaryValue = int(DenaryValue)
            Check = True
        except:
            print('Must enter Integers')
        if Check == True:
            Status = True
        else:
            print('Number can only contain 1s or 0s')
            DenaryValue = input('Reenter the Denary number: ')
            
    return DenaryValue

def DenaryToBinary(DenaryValue):
    BinaryValue1 = ''
    if DenaryValue == 0:
        BinaryValue = '0'
    else:
        while DenaryValue > 0:
            StringNumber = str(DenaryValue % 2)
            BinaryValue1 = BinaryValue1 + StringNumber
            DenaryValue = DenaryValue // 2
        index = len(BinaryValue1)
        BinaryValue = ''
        while index > 0:
            BinaryValue = BinaryValue + BinaryValue1[index - 1]
            index = index - 1 
    return BinaryValue

def HexInput():
    HexValue = input('Enter the Hexadecimal Value')
    Check = True
    Status = False
    while Status == False:
        Length = len(HexValue)
        for index in range(Length):
                if HexValue[index] != '0' and HexValue[index] != '1' and HexValue[index] != '2' and HexValue[index] != '3' and HexValue[index] != '4' and HexValue[index] != '5' and HexValue[index] != '6' and HexValue[index] != '7' and HexValue[index] != '8' and HexValue[index] != '9' and HexValue[index] != '10' and HexValue[index] != 'A' and HexValue[index] != 'a' and HexValue[index] != 'B' and HexValue[index] != 'b' and HexValue[index] != 'C' and HexValue[index] != 'c' and HexValue[index] != 'D' and HexValue[index] != 'd' and HexValue[index] != 'E' and HexValue[index] != 'e' and HexValue[index] != 'F' and HexValue[index] != 'f':
                    Check = False
        if Check == False:
            HexValue = input('Reenter the Hexadecimal Value')
        else:
            Status = True
    return HexValue

def HexToBinary(HexValue):
    Hex_int = int(HexValue, 16)
    BinaryValue1 = ''
    if Hex_int == 0:
        BinaryValue = '0'
    else:
        while Hex_int > 0:
            StringNumber = str(Hex_int % 2)
            BinaryValue1 = BinaryValue1 + StringNumber
            Hex_int = Hex_int // 2
        index = len(BinaryValue1)
        BinaryValue = ''
        while index > 0:
            BinaryValue = BinaryValue + BinaryValue1[index - 1]
            index = index - 1 
    return BinaryValue
        
def BinaryToHex(BinaryValue):
    BinaryValue = str(BinaryValue)
    hex_digits = '0123456789ABCDEF'
    Hex_chars = ''
    if BinaryValue == '0':
        Hex_chars = '0'
    else:
        for i in range(0, len(BinaryValue), 4):
            hex_digit = 0
            for j in range(4):
                hex_digit += int(BinaryValue[i + j]) * (2 ** (3 - j))
            Hex_chars = Hex_chars + (hex_digits[hex_digit])
    HexValue = Hex_chars
    return HexValue

def HexadecimalToDenary(HexValue):
    DenaryValue = int(HexValue,16)
    return DenaryValue

def DenaryToHexadecimal(DenaryValue):
    hex_digits = '0123456789ABCDEF'
    HexChars = ''
    if DenaryValue == 0:
        HexChars = '0'
        HexValue = HexChars
    else:
        while DenaryValue > 0:
            HexChars = HexChars + hex_digits[DenaryValue%16]
            DenaryValue = DenaryValue // 16
        MyList = list(HexChars)
        MyList.reverse()
        Length = len(HexChars)
        HexValue = ''
        for index in range(Length):
            HexValue = HexValue + MyList[index]
    return HexValue


def Menu():
    Status = True
    while Status == True:
        print('1 - Binary to Denary')
        print('2 - Denary to Binary')
        print('3 - Hexadecimal to Binary')
        print('4 - Binary to Hexadecimal')
        print('5 - Hexadecimal to Denary')
        print('6 - Denary to Hexadecimal')
        print('! - QUIT')
        Option = input('Enter option number: ')
        while Option != '1' and Option != '2' and Option != '3' and Option != '4' and Option != '5' and Option != '6' and Option != '!':
            Option = input('Reenter option number: ')
        if Option == '1':
            BinaryValue = BinaryInput()
            DenaryValue = BinaryToDenary(BinaryValue)
            print('Binary:',BinaryValue,'\nDenary:',DenaryValue)
        else:
            if Option == '2':
                DenaryValue = DenaryInput()
                BinaryValue = DenaryToBinary(DenaryValue)
                print('Denary:',DenaryValue,'\nBinary:',BinaryValue)
            else:
                if Option == '3':
                    HexValue = HexInput()
                    BinaryValue = HexToBinary(HexValue)
                    print('Hexadecimal:',HexValue,'\nBinary:',BinaryValue)
                else:
                    if Option == '4':
                        BinaryValue = BinaryInput()
                        HexValue = BinaryToHex(BinaryValue)
                        print('Binary:',BinaryValue,'\nHexadecimal:',HexValue)
                    else:
                        if Option == '5':
                            HexValue = HexInput()
                            DenaryValue = HexadecimalToDenary(HexValue)
                            print('Hexadecimal:',HexValue,'\nDenary:',DenaryValue)
                        else:
                            if Option == '6':
                                DenaryValue = DenaryInput()
                                HexValue = DenaryToHexadecimal(DenaryValue)
                                print('Denary:',DenaryValue,'\nHexadecimal:',HexValue)
                            else:      
                                if Option == '!':
                                    print('Goodbye...')
                                    Status = False
    return
Menu()
