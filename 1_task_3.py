def review_summary(review):
    if len(review) <= 30:
        return review
    
    else:
        end_review = review[:30].rfind(' ')
        if end_review != -1:
            return review[:end_review] + "..."
        
        else:
            return review[:30] + "..."

review = "Not a big fan of Taco Bell's Tacos, but Doritos for a taco shell? Insane"
summary = review_summary(review)
print(summary)