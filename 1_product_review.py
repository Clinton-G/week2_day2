#   Task 1:




#original_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ['good', 'excellent', 'bad', 'poor', 'average']
review = "this product is really good, im impressed with its quality. "
review2 = "the performance of this product is excellent, highly recommended! "
review3 = "i had a bad experience with this product, it didn't meet my expectations. "
review4 = "poor quality product, wouldn't recommend it to anyone. "
review5 = "the product was average, nothing extraordinary about it. "
all_review = review + review2 + review3 + review4 + review5

goodreview = review.replace('good', 'GOOD')
excelreview = review2.replace('excellent', 'EXCELLENT')
badreview = review3.replace('bad', 'BAD')
poorreview = review4.replace('poor', 'POOR')
avgreview = review5.replace('average', 'AVERAGE')

capital_review = goodreview + excelreview + badreview  + poorreview + avgreview
print(capital_review)


#   Dylan Example:

# def review_highlights(reviews):
#     keywords = ['good', 'excellent', 'bad', 'poor', 'average']
#     for review in reviews:
#         for kw in keywords:
#                 review = review.replace(kw, kw.upper())
#                 review = review.replace(kw.title(), kw.upper())
#         print(review)
# review_highlights(reviews)



#----------------------------------------------------------------------------------------------------
#   Task 2:

poitives_word = "good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"
negative_word = "bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"


print(all_review.count('good'))
#   fails with multiple .count(words)
print(all_review.count('good', 'excellent'))
#   fail
positive_count = all_review.count('good')
print(positive_count)
# #   fails with multiple words


pass


#----------------------------------------------------------------------------------------------------
#   Task 3:

reviews_summary = all_review[0:31]
print(reviews_summary)

