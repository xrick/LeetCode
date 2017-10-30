"""
717. 1-bit and 2-bit Characters My SubmissionsBack to Contest

We have two special characters. The first character can be represented by one bit 0. 
The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must 
be a one-bit character or not. The given string will always end with a zero.
"""

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if(len(bits) <= 2):
            if(bits[0] == 1):
                return False
            else:
                return True
        if(bits[0] == 0):
            return self.isOneBitCharacter(bits[1:])
        else:
            return self.isOneBitCharacter(bits[2:])