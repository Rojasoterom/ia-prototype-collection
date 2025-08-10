# Import unittest and emotion analyzer package
import unittest
from EmotionAnalysis.emotion_detection import emotion_detector

# Create TestEmotionAnalyzer class
class TestEmotionAnalyzer(unittest.TestCase):
    def test_emotion_analyzer(self):
        # Case 1 - Test joy emotion
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        # Case 2 - Test anger emotion
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        # Case 3 - Test disgust emotion
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        
        # Case 4 - Test sadness emotion
        result_2 = emotion_detector('I am so sad about this')
        self.assertEqual(result_2['dominant_emotion'], 'sadness')
        
        # Case 5 - Test fear emotion
        result_3 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_3['dominant_emotion'], 'fear')

unittest.main()
