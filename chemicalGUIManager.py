
class chemicalInputInterpreter:

    def getReactant(reaction):
        
        temp = reaction.split("->")

        chars = ['+','', '']
        try:
            for ch in chars:
                if temp[0].count(ch) != 0:
                    temp[0].remove(ch)
        except IndexError:
            return False

        return temp

    def getProduct(reaction):

        temp = reaction.split("->")

        chars = ['+','', '']
        try:
            for ch in chars:
                if temp[1].count(ch) != 0:
                    temp[1].remove(ch)
        except IndexError:
            return False

        return temp

    def getReactantAmount(reaction):

        return len(chemicalInputInterpreter.getReactant(reaction))

    def getAllElementAmount(reaction):

        return len(chemicalInputInterpreter.toElement(reaction))

    def getProductAmount(reaction):

        return chemicalInputInterpreter.getAllElementAmount(reaction) - chemicalInputInterpreter.getReactantAmount(reaction)

    def toElement(reaction):

        assert(isinstance(reaction, str))
        temp = reaction.split("->")
        temp = [w.split(' ') for w in temp]

        chars = ['+','', '']

        try:
            for ch in chars:
                for i in range(0, 2):
                    if temp[i].count(ch) != 0:
                        temp[i].remove(ch)
        except IndexError:
            return False
        
        # Finally, add elements into list, using list comprehension
        elementList = [w for i in temp for w in i]

        # .. and vaildates it.
        chemicalInputInterpreter.validateWithDatabase(chemicalInputInterpreter.removeQuotient(elementList))

        return elementList


    # WARNING : These functions(removeQuotient, extractQuotient)
    # returns string type, so explicit type conversion is required
    
    def removeQuotient(elementList):

        assert(isinstance(elementList, list))

        temp = []
        for element in elementList:
            if element[0].isnumeric():
                temp.append(element[1:])
            else:
                temp.append(element)

        return temp
        
    def extractQuotient(elementList):
        
        assert(isinstance(elementList, list))
        
        temp = []
        for element in elementList:
            if element[0].isnumeric():
                temp.append('1')
            else:
                temp.append(element[1])
                
        return temp
    
    def validateWithDatabase(componentList):

        assert(isinstance(componentList, list))
        deletionIndex = []
        for i in range(0, len(componentList)):
            if chemicalDictHandler.findElement(componentList[i]) == False:
                deletionIndex.append(i)

        adjust = 0
        for delIndex in deletionIndex:
            del componentList[delIndex-adjust]
            adjust += 1

        return componentList

class chemicalDictHandler:

    chemDict = {}

    def addElement(newElement):
        assert(isinstance(newElement, list))
        chemicalDictHandler.chemDict[newElement[0]] = newElement[1:6]

    def findElement(key):
        try:
            return chemicalDictHandler.chemDict[key]
        except KeyError:
            print("[DEBUG] Key value not found")
            return False

    def deleteElement(key):
        try:
            del chemicalDictHandler.chemDict[key]
        except KeyError:
            print("[DEBUG] Key value not found, deletion is aborted")
            return False

class chemicalFileReader:

    def read_chem_files():

        chemicalElement = []

        try:
            
            chemData = open("./chemData.txt", 'r')

            while True:
                line = chemData.readline()
                if not line:
                    break
                else:
                    line = line.strip('\n')
                    chemicalElement.append(line.split(";"))
                    print(str(line.split(";")) + " was added")
            
        except FileNotFoundError:
            
            chemData.write("")

        finally:

            chemData.close()

            for data in chemicalElement:
                chemicalDictHandler.addElement(data)