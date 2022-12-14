import collections
import attr


@attr.s
class deviation(object):
    #I^!
    deviationInfoset = attr.ib()
    #I^(target)
    targetInfoset = attr.ib()
    #a^(!)
    targetAction = attr.ib()
    #a^(target!) timport collections
import attr


@attr.s
class deviation(object):
    #I^!
    deviationInfoSet = attr.ib()
    #I^(target)
    targetInfoSet = attr.ib()
    #a^(!)
    targetAction = attr.ib()
    #a^(target!) t
    deviationTargetAction = attr.ib()
    #si or a^(action)
    deviationAction = attr.ib()

    timeSelectionFunctions = attr.ib()
    
    def __init__(self, target):
        super(self).__init()
        self.targetInfoset = target
    
    #If a pure strategy, a pure strategy will be returned (aka function works for both actions and strategies as input)
    def deviate(self,infoset,strategy):
        return "yet to be implemented"

class informedCausalDeviation(deviation):

    def __init__(self, targetInfoSet, devationAction, deviationTargetAction):
         self.targetInfoSet = targetInfoSet
         self.deviationAction = devationAction
         self.deviationTargetAction = deviationTargetAction
         self.timeSelectionFunctions = [(lambda t : 1)]

         self.targetAction = None
         self.deviationInfoSet = None
         self.deviationInfoSet = None
         

    def deviate(self, infoSetNode, strategy):
        #print(infoSetNode)
        deviationStrategy = strategy.copy()
        #print(deviationStrategy)
        if infoSetNode == self.targetInfoSet:
            print(len(infoSetNode.legal_actions))
            for i in infoSetNode.legal_actions:
                if self.deviationTargetAction == i:
                    if not self.deviationAction in infoSetNode.legal_actions:
                        print("errpr")
                    deviationStrategy[self.deviationAction] = deviationStrategy[i] + deviationStrategy[self.deviationAction]
                    deviationStrategy[i] = 0
                else:
                    deviationStrategy[i] = 0
        #print(" TEST " + str(list(deviationStrategy.values())))
        return list(deviationStrategy.values())

#Returns all deviations NOW relizable on an infomation state
def returnInformedCausalDeviation(info_state,info_state_node):
    deviationSet = []
    for target_action in info_state_node.legal_actions:
        for deviation_action in info_state_node.legal_actions:
                deviationSet.append(informedCausalDeviation(info_state_node, deviation_action,target_action))
    return deviationSet

