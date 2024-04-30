from functionality import xorFunction, hammingDistance

def polynomialDivision(polynomial : list, divisor : list) -> list:
    if len(polynomial) >= len(divisor):

        # Adjusting Divisor Degree
        adjustedDivisorDegree = []

        for i in range(len(polynomial) - len(divisor)):
            adjustedDivisorDegree.append(0)

        for i in divisor:
            adjustedDivisorDegree.append(i)

        # Division Process
        quotient  = []
        remainder = []

        while(adjustedDivisorDegree.index(1) >= polynomial.index(1)):
            quotient.append(adjustedDivisorDegree.index(1) - polynomial.index(1))
            polynomial = polynomialXOR(polynomial, shiftLeftArrayValue(adjustedDivisorDegree, adjustedDivisorDegree.index(1) - polynomial.index(1)))
            remainder  = polynomial

        if quotient or remainder:
            return [convertQuotient(quotient, len(adjustedDivisorDegree)), remainder]
        else:
            return None

    else:
        return polynomial # return polynomial since the divisor has larger degree

def shiftLeftArrayValue(inputArray, shift):
    outputArray = []

    for i in range(len(inputArray)):
        if i >= shift:
            outputArray.append(inputArray[i])

    if len(outputArray) <= len(inputArray):
        for i in range(len(inputArray) - len(outputArray)):
            outputArray.append(0)

    if outputArray:
        return outputArray
    else:
        return None

def polynomialXOR(inputPolynomialA : list, inputPolynomialB : list) -> list:
    outputPolynomial = []

    if len(inputPolynomialA) == len(inputPolynomialB):
        for i in range(len(inputPolynomialA)):
            if inputPolynomialA[i] == inputPolynomialB[i]:
                outputPolynomial.append(0)
            else:
                outputPolynomial.append(1)

        if outputPolynomial:
            return outputPolynomial
        else:
            return None

    else:
        return None

def convertQuotient(inputQuotient : list, lengthPolynomial : int) -> list:
    outputArray = []

    if inputQuotient:
        for i in range(lengthPolynomial):
            outputArray.append(0)

        for i in inputQuotient:
            outputArray[(len(outputArray)-1)-i] = 1
    else:
        return None

    if outputArray:
        return outputArray
    else:
        return None

def printPolynomial(inputPolynomialArray : list) -> str :
    if inputPolynomialArray:
        outputString = ""

        for i in range(len(inputPolynomialArray)):
            if i == len(inputPolynomialArray)-1:
                if inputPolynomialArray[i]:
                    outputString += "x^" + str((len(inputPolynomialArray)-1)-i)
            else:
                if inputPolynomialArray[i]:
                    outputString += "x^" + str((len(inputPolynomialArray) - 1) - i) + "+"

        if outputString:
            return outputString
        else:
            return None

    else:
        return None

def convertingStringtoPolynomial(inputString : str) -> list:
    outputArray = []

    if inputString:
        for i in inputString:
            outputArray.append(int(i))

        if outputArray:
            return outputArray
        else:
            return None

    else:
        return None

def generatingCodeword(inputMessagePolynomial : list, inputRemainder : list) -> list:
    if inputMessagePolynomial and inputRemainder:
        return polynomialXOR(inputMessagePolynomial, inputRemainder)
    else:
        return None

def addingParityBitstoMessage(inputMessage : str, n : int, k : int) -> str:
    if inputMessage:
        if n > k:
            for i in range(n-k):
                inputMessage += "0"

            return inputMessage
        else:
            return None
    else:
        return None

def generatingGenPoly(inputGenPolyinOctal : str):
    if inputGenPolyinOctal:
        outputString = ""

        for i in inputGenPolyinOctal:
            x = str(bin(int(i)))
            x = x[x.find('b')+1:]

            if len(x) == 3:
                outputString += x
            else:
                for j in range(3-len(x)):
                    outputString += '0'

                for j in x:
                    outputString += j

        if outputString:
            return outputString
        else:
            return None
    else:
        return None

def convertingPolynomialtoString(inputPolynomial : list) -> str:
    if inputPolynomial:
        outputString = ""

        for i in inputPolynomial:
            outputString += str(i)

        if outputString:
            return outputString
        else:
            return None

    else:
        return None

def adjustingMessageLength(inputPlainMessage : str, length : int) -> str:
    if inputPlainMessage and length and (length >= len(inputPlainMessage)):
        outputString = ""

        for i in range(length - len(inputPlainMessage)):
            outputString += '0'

        for i in inputPlainMessage:
            outputString += i

        if outputString:
            return outputString
        else:
            return None

    else:
        return None

def calculatingReceivedCodeword(inputReceivedHelperBits : list, inputAuthenticBiometric : list) -> list:
    outputArray = []

    if len(inputReceivedHelperBits) == len(inputAuthenticBiometric):
        for i in range(len(inputReceivedHelperBits)):
            if len(inputReceivedHelperBits[i]) == len(inputAuthenticBiometric[i]):
                outputArray.append(xorFunction(inputReceivedHelperBits[i], inputAuthenticBiometric[i]))
            else:
                break
                return None

        if outputArray:
            return outputArray
        else:
            return None
    else:
        return None

def calculatingKRR(inputReceivedCodeword : list, inputAuthenticCodeword : str) -> list:
    outputArray = []

    if inputReceivedCodeword and inputAuthenticCodeword:
        for i in inputReceivedCodeword:
            if len(i) == len(inputAuthenticCodeword):
                outputArray.append(hammingDistance(i,inputAuthenticCodeword))
            else:
                break
                return None

        if outputArray and (len(outputArray) == len(inputReceivedCodeword)):
            return outputArray
        else:
            return None
    else:
        return None

def generatingKRRFromVarianceDataset(inputReceivedCodewordFromVarianceDataset : list, inputAuthenticCodeword : str) -> list:
    outputArray = []

    if inputReceivedCodewordFromVarianceDataset and inputAuthenticCodeword:
        for datasetReceivedCodeword in inputReceivedCodewordFromVarianceDataset:
            if datasetReceivedCodeword:
                tempArray = []

                for i in datasetReceivedCodeword:
                    if len(i) == len(inputAuthenticCodeword):
                        tempArray.append(hammingDistance(i, inputAuthenticCodeword))
                    else:
                        break
                        return None

                if tempArray:
                    # outputArray.append([
                    #     min(tempArray), max(tempArray)
                    # ])
                    outputArray.append(min(tempArray))
                else:
                    break
                    return None
            else:
                break
                return None

    else:
        return None

    if outputArray:
        return outputArray
    else:
        return None

def testThis():
    n            = 63
    k            = 45
    genPolyOctal = "1701317" # See ECC Book
    plainMessage = "0100000101011000001011100011001000110101" # Message should have the correct length, namely
    # meets the (n ,k) scheme. For example, in this case the message should have 45-bits length to meet (63,45) BCH code

    message = convertingStringtoPolynomial(addingParityBitstoMessage(adjustingMessageLength(plainMessage, k), n, k))
    genPoly = convertingStringtoPolynomial(generatingGenPoly(genPolyOctal))

    # x = polynomialDivision(polynomial, divisor)
    x = polynomialDivision(message, genPoly)
    y = generatingCodeword(message, x[1])
    #
    print("Message   : " + str(convertingStringtoPolynomial(plainMessage)))
    print("GenPoly   : " + str(genPoly))
    print("Quotient  : " + str(x[0]))
    print("Remainder : " + str(x[1]))
    print("Codeword  : " + str(y))

    a = convertingPolynomialtoString(y)
    b = "000000100000101011000001011100011001000110101111011111101101011"

    if a == b:
        print("TRUE")
    else:
        print("FALSE")

# testThis()