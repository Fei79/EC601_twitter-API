import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"The path of json file"
from google.cloud import language

print("Please enter a sentence or paragraph: ", end=" ")
content=input()

client=language.LanguageServiceClient()
type_=language.Document.Type.PLAIN_TEXT
encoding_type=language.EncodingType.UTF32
document = {"content":content,"type_":type_}
response = client.analyze_sentiment(request={"document":document, "encoding_type":encoding_type})
sentiment = response.document_sentiment

def content_status():
    if sentiment.score <= -0.25:
        status = 'Negative'
    elif sentiment.score <= 0.25:
        status = 'Neutral'
    else:
        status = 'Positive'
    return status

print("Sentiment score is: ", end= " ")
print(sentiment.score)
print("Sentiment magnitude is: ", end=" ")
print(sentiment.magnitude)
print("Sentiment status is: ", end=" ")
print(content_status())
