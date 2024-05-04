import random
from typing import List

def setSecretWord(self, themeList:List[str]) -> None:
   self.secretWord = themeList[random.randomint(0, 9)]

def setSecretWordLength(self, secretWord:str) -> None:
   self.secretWordLength = len(secretWord)

def setMaxPoints(self, secretWordLength:int) -> None:
   self.maxPoints = secretWordLength

def matchWordle(self, secretWord:str, guessWord:str) -> List[int]:
   matchResult:List[int] = []
   for i in range(0, len(secretWord)):
      if secretWord[i] == guessWord[i]:
         matchResult.append(guessWord[i])
      else:
         matchResult.append(' ')
   return matchResult

