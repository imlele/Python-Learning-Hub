class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        For every letter in *ransomNote*, check if it is in *magazine*.
        If it is, remove it from *magazine*.
        If it is not, return False.
        If we get to the end of *ransomNote*, return True.
        """
        for c in ransomNote:
            if c not in magazine:
                return False
            i = magazine.find(c)
            magazine = magazine[:i] + magazine[i+1:]

        return True

### OR ###
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Create a dictionary of letter counts for *magazine*.
        Create a dictoinary of letter counts for *ransomNote*.
        check IF every key of *ransomNoteLetterCount* is in *magazineLetterCount*.
              AND IF the value of *ransomNoteLetterCount* is <= the value of *magazineLetterCount*.
        """
        magazineLetterCount = {}
        for c in magazine:
            if c in magazineLetterCount:
                magazineLetterCount[c] += 1
            else:
                magazineLetterCount[c] = 1

        ransomNoteLetterCount = {}
        for c in ransomNote:
            if c in ransomNoteLetterCount:
                ransomNoteLetterCount[c] += 1
            else:
                ransomNoteLetterCount[c] = 1

        for c in ransomNoteLetterCount:
            if c not in magazineLetterCount or ransomNoteLetterCount[c] > magazineLetterCount[c]:
                return False
        
        return True
        

    