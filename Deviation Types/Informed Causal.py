import Deviation
class InformedCausalDeviation(Deviation):
    def __init__(self, targetInfoSet, devationAction, deviationTargetAction):
         self.targetInfoSet = targetInfoSet
         self.devationAction = devationAction
         self.devationAction = deviationTargetAction
    def deviate(self,infoSet, infoSetNode, strategy):
        for 

def returnTimeSelctionFunctions(info_state,info_state_node,deviationSet ):
    return [(lambda t : 1)]
#Returns all deviations relizable to infomation state
def returnDeviations(info_state,info_state_node):
    deviationSet = []
    for target_action in info_state_node.legal_actions:
        for deviation_action_index in range(info_state_node.legal_actions):
                deviation = (lambda strategy: (
                    for i in info_state_node.legal_actions:
                        if target_action == i:
                            strategy[deviation_action_index] += strategy[i]
                            strategy[i] = 0))
                deviationSet.append(InformedCausalDeviation(target_action))
    return deviationSet