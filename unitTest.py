from chemicalReaction import *

molarityList = {1:[1.0, 1.0], 2:[1.0, 2.0], 3:[2.0, 2.0]}
initialVelocity = {1:0.25, 2:1.0, 3:2.0}
chemicalCalculator.calculate_ReactionDegree(molarityList, initialVelocity)
chemicalCalculator.calculate_ReactionVelocityConstant(molarityList, initialVelocity)
print(chemicalCalculator.calculate_ReactionVelocity({1:5, 2:3}))

molarityList = {1:[0.1, 0.1], 2:[0.1, 0.2], 3:[0.2,0.1]}
initialVelocity = {1:4, 2:4, 3:16}
chemicalCalculator.calculate_ReactionDegree(molarityList, initialVelocity)
chemicalCalculator.calculate_ReactionVelocityConstant(molarityList, initialVelocity)
print(chemicalCalculator.calculate_ReactionVelocity({1:1, 2:3}))