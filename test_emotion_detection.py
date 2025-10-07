from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):
        expected_joy = emotion_detector("I am glad this happened")
        expected_anger = emotion_detector("I am really mad about this")
        expected_disgust = emotion_detector("I feel disgusted just hearing about this")
        expected_sadness = emotion_detector("I am so sad about this")
        expected_fear = emotion_detector("I am really afraid that this will happen")

        self.assertEqual(expected_joy["dominant_emotion"], "joy")
        self.assertEqual(expected_anger["dominant_emotion"], "anger")
        self.assertEqual(expected_disgust["dominant_emotion"], "disgust")
        self.assertEqual(expected_sadness["dominant_emotion"], "sadness")
        self.assertEqual(expected_fear["dominant_emotion"], "fear")

unittest.main()