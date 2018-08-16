
class utility:

    def getMax(a, b):
        if a < b:
            return b
        else:
            return a

    def getMin(a, b):
        if a < b:
            return a
        else:
            return b

    def findLeastIndex(dataList):
        assert(len(dataList) > 0)
        least = dataList[0]
        leastidx = 0
        
        for idx in range(0, len(dataList)):
            if dataList[i] < least:
                least = dataList[i]
                leastidx = i
        return leastidx

    def is_uniqueElement(dataDict):

        # Every element contained in dataDict will be appended here
        allElements = []

        # Every chemical experiments order start with index '1', so it  doesn't matter
        for i in range(1, len(dataDict)+1):
            allElements += (dataDict[i])
        # print(allElements)

        uniqueElement = set(allElements)
        # print(uniqueElement)

        for element in uniqueElement:
            if allElements.count(element) > 1:
                # print('This element is not unique')
                return False

        return True

    def isSuitable(list1, list2):

        try:

            # Assuming that both list's length are same
            assert(len(list1) == len(list2))
            for i in range(0, len(list1)):

                '''
                print("At index " + str(i))
                print(list1[i])
                print(list2[i])
                print(list1[i+1])
                print(list2[i+1])
                '''

                if list1[i] == list2[i] and list1[i+1] != list2[i+1]:
                    # print("Those lists have same elements, not duplicated")
                    return True

                elif list1[i] != list2[i] and list1[i+1] == list2[i+1]:
                    # print("Those lists have same elements, not duplicated")
                    return True

                elif list1[i] == list2[i] and list1[i] == list2[i]:
                    # print("Those lists have same elements, DUPLICATED")
                    return False

                else:
                    # print("Those lists HAVE NOT same elements")
                    return False

        except AssertionError:
            return -1
