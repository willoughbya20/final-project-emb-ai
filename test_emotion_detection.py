from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        res1 = emotion_detector("I am glad this happened")
        self.assertEqual(res1['dominant_emotion'], 'joy')

        res2 = emotion_detector("I am really mad about this")
        self.assertEqual(res2['dominant_emotion'], 'anger')

        res3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(res3['dominant_emotion'], 'disgust')

        res4 = emotion_detector("I am so sad about this")
        self.assertEqual(res4['dominant_emotion'], 'sadness')

        res5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res5['dominant_emotion'], 'fear')

unittest.main()
