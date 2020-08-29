import unittest
import main


class TestGame(unittest.TestCase):
    #TEST UNIT INPUT IN LOWER CASE RETURN TRUE
    def test_input(self):
        result = main.hang('the sky is blue')
        self.assertTrue(result)
       #TEST UNIT INPUT RETURN FALSE BECAUSE THE WORD IS NOT IN LOWER CASE 
    def test_input2(self):
        main.word = 'press'
        result = main.hang('PRESS')
        self.assertFalse(result)
    # TEST RANDOM WORD FUNCTION IS WORKING PROPERLY OR NOT
    def test_random_word(self):
        result = main.randomWord()
        self.assertTrue(result)
        #TESTING EACH LETTER OF A WORD IS REPLACED WITH "_" CORRECTLY OR NOT
    def test_not_match_word(self):
        result = main.spacedOut('press','')
        self.assertEqual(result,'_ _ _ _ _ ')
        #TESTING IF THERE IS A "S" LETTER IS GUESSED CORRECTLY FROM A USER AND ALL PLACES OF S WILL BE REVEALED
    def test_not_match_word1(self):
        array = ['S']
        result = main.spacedOut('press',array)
        self.assertEqual(result,'_ _ _ S S ')
        #TESTING IF THERE IS A "l" LETTER IS GUESSED CORRECTLY FROM A USER AND ALL PLACES OF "l" WILL NOT BE REVEALED
    def test_not_match_word2(self):
        array = ['1']
        result = main.spacedOut('press',array)
        self.assertEqual(result,'_ _ _ _ _ ')
        #TESTING IF THERE IS A "+" LETTER IS GUESSED CORRECTLY FROM A USER AND ALL PLACES OF "+" WILL NOT BE REVEALED
    def test_not_match_word3(self):
        array = ['+']
        result = main.spacedOut('press',array)
        self.assertEqual(result,'_ _ _ _ _ ')
            #TESTING IF THERE IS A "T" LETTER IS GUESSED CORRECTLY FROM A USER AND ALL PLACES OF "T" WILL BE REVEALED
    def test_not_match_word5(self):
        array = ['T']
        result = main.spacedOut('the sky is blue',array)
        self.assertEqual(result,'T _ _  _ _ _  _ _  _ _ _ _ ')
            #TESTING IF THERE IS A "T" LETTER IS GUESSED CORRECTLY FROM A USER AND ALL PLACES OF T WILL BE REVEALED    
    def test_not_match_word4(self):
        array = ['T']
        result = main.spacedOut('zoologist',array)
        self.assertEqual(result,'_ _ _ _ _ _ _ _ T ')
    #TESTING HANGMAN PICTURE WILL BE DISPLAYED PROPERLY OR NOT
    def test_display(self):
        result = main.hangmanPics
        self.assertTrue(result)
      #TESTING LOSING MESSANGE WILL BE DISPLAYED PROPERLY OR NOT
    def test_end(self):
        answer = main.lostTxt
        self.assertEqual(answer,'You Lost, press any key to play again...')
           #TESTING WINNING MESSANGE WILL BE DISPLAYED PROPERLY OR NOT
    def test_end1(self):
        answer = main.winTxt
        self.assertEqual(answer,'WINNER!, press any key to play again...')


#   #TESTING RESET FUNCTION WILL WORK PROPERLY OR NOT
    def test_reset(self):
        result = main.reset()
        self.assertFalse(result)
if __name__ == '__main__':

    unittest.main()

