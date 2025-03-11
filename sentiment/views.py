from rest_framework.response import Response
from rest_framework.decorators import api_view
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from django.views.decorators.csrf import csrf_exempt

nltk.download('vader_lexicon')

@csrf_exempt
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)['compound']

    if score > 0:
        return "Positive 😊"
    elif score == 0:
        return "Neutral 😐"
    else:
        return "Negative 😢"
    
@api_view(['POST'])
def sentiment_analysis(request):
    text = request.data.get('text', '')
    if not text:
        return Response({'error': 'Please provide text to analyze'}, status=400)

    sentiment = analyze_sentiment(text)
    return Response({'sentiment': sentiment})