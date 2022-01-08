import sys
sys.path.append("f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src")

from gros.gesture.Gesture import Gesture
from gros.gesture.GestureSet import GestureSet
from gros.gesture.GestureSequence import GestureSequence
from gros.action.Action import Action
from gros.action.ActionSet import ActionSet
from gros.initialize.Initialize import Initialize
from gros.initialize.SequenceActionPair import SequenceActionPair

class InitializeModeDoc(Initialize):
    def __init__(self) -> None:
        super().__init__()
        self.action_activation_list = ["showDesktop", "switch", "printscreen", "minimize", "save"]
        self.gesture_activation_list = ["palm", "fist", "double_point", "side_palm", "horiz_palm", "thumb_up"]
        self.partial_action_activation(self.action_activation_list)
        self.partial_gesture_activation(self.gesture_activation_list)
    
    def pairing(self):
        gesPool = []
        gesPool.append(GestureSequence("side_grip", [Gesture("side_palm"), Gesture("side_fist")])) # showDesktop
        gesPool.append(GestureSequence("swip", [Gesture("side_palm"), Gesture("horiz_palm")])) # switch
        gesPool.append(GestureSequence("grip", [Gesture("palm"), Gesture("fist")])) # printscreen
        gesPool.append(GestureSequence("hook", [Gesture("double_point"), Gesture("fist")])) # minimize
        gesPool.append(GestureSequence("thumb", [Gesture("thumb_up")])) # save
        pool = []
        for i in range(len(gesPool)):
            pool.append(SequenceActionPair(gesPool[i], Action(self.action_activation_list[i], activate=True)))
        return pool