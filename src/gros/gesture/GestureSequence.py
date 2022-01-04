import sys
sys.path.append("f:/0Desk/IBDP/ComputerScience/IA/code/GROS/src")

from gros.gesture.Gesture import Gesture

class GestureSequence(object):
    def __init__(self, name:str, gestureSequence:list, activate=True, position_restrict=False):
        """Initialize a gesture sequence that listens on the cache memory of gestures

        Args:
            name (str): the name of the gesture sequence
            gestureSequence (list): a list of gesture that forms the gesture sequence
            activate (bool, optional): the activation status. Defaults to True.
            position_restrict (bool, optional): position restrict control. Gestures at different position may be marked as different gestures.
        """
        self._name = name
        self._gestureSequence = gestureSequence
        self._status = activate
        self.position_restrict = position_restrict
        
    def get_name(self):
        # get name of the gesture
        return self._name
    
    def get_activation_status(self):
        # get the name of the activation status
        return self._status
        
    def listen_on_cache(self, cache:list):
        """listen on the cache memory, sequence is detected, then return True

        Args:
            cache (list): a copy of the cache memory

        Returns:
            (bool): indicator of whether if the sequence is detected
        """
        cache_comp = cache[-len(self._gestureSequence):]
        # print(len(self._gestureSequence))
        for i in range(len(cache_comp)):
            if cache_comp[i].get_name() == self._gestureSequence[i].get_name():
                if self.position_restrict:
                    if cache_comp[i].get_position() == self._gestureSequence[i].get_position():
                        pass
                    else:
                        return False
            else:
                return False
        return True

# palm = GestureSequence('palm', [Gesture('palm', True, "right")], position_restrict=True)
# dpalm = Gesture('palm', 'left')
# dfist = Gesture('fist', 'right')
# cache = [dfist, dfist, dpalm]
# print(palm.listen_on_cache(cache))