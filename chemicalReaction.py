# -*- coding: utf-8 -*-

#
# 화학 세부특기사항용 프로그램
# 주제 : 반응 속도를 구하는 프로그램
#
# 필요한 요소:
# 1. 엔탈피 표
# 2. 화학 원소 정보 - 이름, 분자량, 밀도(금속: 고체, 비금속/비활성:기체)
#    참고. 탄소 동소체 같은 경우에는 1.8 ~ 2.1의 중간값으로 적어놓았음.
#    참고2. 기체의 밀도 단위는 g/L, 고체의 밀도 단위는 g/cm^3.
#    참고3. 인(P) 같은 경우에는 백린 기준.
#    참고4. 황(S) 같은 경우에는 감마 기준.
# 3. 1, 2차 반응, 그리고 반응 차수
# 4. 반응속도 상수
#

from utility import *

class chemicalCalculator:

    def calculate_Molarity(mol, volume):
        assert(isinstance(mol, float) and isinstance(volume, float))
        assert(volume > 0)

        # Note: unit is 'M'
        return round(mol/volume, 2)

    # Easy version - only accepts up to 2 chemicals
    # chemMolarityData stands for 'Initial substance's concentration'
    # reactionVelocityData stands for 'Initial reaction velocity'

    degree = []

    def calculate_ReactionDegree(chemMolarityData, reactionVelocityData):

        try:
            assert(isinstance(chemMolarityData, dict))
            assert(isinstance(reactionVelocityData, dict))

            # Checks condition if provided data does meet with it

            # if len(chemMolarityData) - 1 != len(chemMolarityData):
            #    return False
            if len(reactionVelocityData) != len(chemMolarityData):
                return False
            if utility.is_uniqueElement(chemMolarityData) == True:
                return False

            for idx in range(1, len(reactionVelocityData)):
                if utility.isSuitable(chemMolarityData[idx], chemMolarityData[idx+1]) == -1:
                    return False

            comparableIndex = ()
            for idx in range(1, len(reactionVelocityData)):
                # print("INDEX " + str(idx))
                for i in range(1, len(reactionVelocityData)-idx+1):
                    # print("Adjust : " + str(i))
                    if utility.isSuitable(chemMolarityData[idx], chemMolarityData[idx+i]) == True:
                        comparableIndex += (idx, idx+i)

            if len(comparableIndex) == 0:
                return False

            # These expressions can be abbreviated; find ways to make it happen
            degree = [list() for w in range(0, len(chemMolarityData)-1)]
            degreeDiff = [list() for w in range(0, len(chemMolarityData)-1)]

            velocityDiff = []
            for i in range(0, len(comparableIndex), 2):
                for j in range(0, len(chemMolarityData[comparableIndex[i]])):

                    velocityDiff = reactionVelocityData[comparableIndex[i+1]]/reactionVelocityData[comparableIndex[i]]
                    if chemMolarityData[comparableIndex[i+1]][j] / chemMolarityData[comparableIndex[i]][j] != 1:
    
                        degreeDiff[j] = chemMolarityData[comparableIndex[i+1]][j] / chemMolarityData[comparableIndex[i]][j]

                        if velocityDiff == 1:
                            degree[j] = 0
                        else:
                            degree[j] = velocityDiff/degreeDiff[j]

                        # print("Index " + str(j) + " Degree : " + str(degree[j]))

            chemicalCalculator.set_degree(degree)

        except AssertionError:
            return False

    def set_degree(newValue):
        chemicalCalculator.degree = newValue

    def get_degree():
        return chemicalCalculator.degree

    velConst = 0

    def calculate_ReactionVelocityConstant(chemMolarityData, reactionVelocityData):
        
        # degree = calculate_ReactionDegree(chemMolarityData, reactionVelocityData)
        
        # Repeating reaction degree calculation is not a good choice.
        # Try get them from external getter method.

        # Using first data to calculate this constant
        chemicalCalculator.set_reactionVelocityConst(reactionVelocityData[1] / ((chemMolarityData[1][0] ** chemicalCalculator.get_degree()[0]) * (chemMolarityData[1][1] ** chemicalCalculator.get_degree()[1])))

    def set_reactionVelocityConst(newValue):
        chemicalCalculator.velConst = newValue

    def get_reactionVelocityConst():
        return chemicalCalculator.velConst

    # This parameter, chemMolarityData is different, comparing with above ones
    # This follows this format:
    # {1 : (A's molarity), 2: (B's molarity)}

    def calculate_ReactionVelocity(chemMolarityData):

        assert(isinstance(chemMolarityData, dict))

        print(chemicalCalculator.get_degree())
        print(chemicalCalculator.get_reactionVelocityConst())
        return chemicalCalculator.get_reactionVelocityConst() * (chemMolarityData[1] ** chemicalCalculator.get_degree()[0]) * (chemMolarityData[2] ** chemicalCalculator.get_degree()[1])