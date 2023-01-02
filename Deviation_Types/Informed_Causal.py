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
    #a^(target!) t
    deviationTargetAction = attr.ib()
    #si or a^(action)
    devationAction = attr.ib()

    timeSelectionFunctions = attr.ib()
    
    def __init__(self, target):
        self.targetInfoset = target
    
    #If a pure strategy, a pure strategy will be returned (aka function works for both actions and strategies as input)
    def deviate(self,infoset,strategy):
        return "yet to be implemented"

class informedCausalDeviation(deviation):
    def __init__(self, targetInfoSet, devationAction, deviationTargetAction):
         self.targetInfoSet = targetInfoSet
         self.devationAction = devationAction
         self.devationAction = deviationTargetAction
         self.timeSelectionFunctions = [(lambda t : 1)]
    def deviate(self, infoSetNode, strategy):
        if infoSetNode == self.targetInfoSet:
            for i in infoSetNode.legal_actions:
                if self.target_action == i:
                    strategy[self.deviation_action] += strategy[i]
                    strategy[i] = 0

#Returns all deviations NOW relizable on an infomation state
def returnInformedCausalDeviation(info_state,info_state_node):
    deviationSet = []
    for target_action in info_state_node.legal_actions:
        for deviation_action in info_state_node.legal_actions:
                deviationSet.append(informedCausalDeviation(info_state_node, deviation_action,target_action))
    return deviationSet
