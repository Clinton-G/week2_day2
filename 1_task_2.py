positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally_words(review):
    positive_tally = 0
    negative_tally = 0
    
    for word in review.split():
        if word.lower() in positive_words:
            positive_tally += 1
        elif word.lower() in negative_words:
            negative_tally += 1
    
    return positive_tally, negative_tally

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

for count, review in enumerate(reviews, start=1):
    positive_count, negative_count = tally_words(review)
    print(f"Review {count}: Positive words: {positive_count}, Negative words: {negative_count}")