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

