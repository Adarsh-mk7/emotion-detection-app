from textblob import TextBlob

def emotion_detector(text_to_analyze):
    # Task 7: Error handling for blank, empty, or whitespace-only inputs
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    # Run local lexicon analysis
    blob = TextBlob(text_to_analyze)
    polarity = blob.sentiment.polarity        # Ranges from -1.0 (Negative) to +1.0 (Positive)
    subjectivity = blob.sentiment.subjectivity  # Ranges from 0.0 (Objective) to 1.0 (Subjective)

    # Convert native polarity/subjectivity patterns dynamically into the project's expected 5 emotions
    if polarity > 0.1:
        joy = round(polarity * subjectivity, 4)
        sadness = 0.0
        anger = 0.0
    elif polarity < -0.1:
        joy = 0.0
        sadness = round(abs(polarity) * subjectivity * 0.7, 4)
        anger = round(abs(polarity) * subjectivity * 0.3, 4)
    else:
        joy = 0.05
        sadness = 0.05
        anger = 0.05

    # Static default metrics for complex edge fields to safely fill the template structure
    fear = round((1.0 - polarity) * 0.1, 4)
    disgust = round(anger * 0.5, 4)

    emotion_list = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }

    # Extract dominant emotion programmatically
    dominant_emotion = max(emotion_list, key=emotion_list.get)
    emotion_list['dominant_emotion'] = dominant_emotion

    return emotion_list