import unittest
# Import the module function from your package folder
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_joy_emotion(self):
        # Test case for checking strong positive text mapping to joy
        result = emotion_detector("I am absolutely thrilled and delighted because I finally got my visa slot today!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_sadness_emotion(self):
        # Test case for checking negative text mapping to sadness/anger
        result = emotion_detector("I am incredibly frustrated and down because my application was delayed again.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_neutral_emotion(self):
        # Test case for flat/neutral statements
        result = emotion_detector("The event is happening tomorrow morning at ten o'clock.")
        self.assertEqual(result['dominant_emotion'], 'joy')  # Default fallback handling

    def test_invalid_input(self):
        # Task 7 validation: Test case for checking handling of empty inputs
        result = emotion_detector("   ")
        self.assertIsNone(result['dominant_emotion'])

if __name__ == '__main__':
    unittest.main()