'''roblem Statement 
Movie reviews are stored as follows: 
reviews = [ 
    "excellent movie", 
    "average story", 
    "excellent acting", 
    "poor direction", 
    "excellent visuals", 
    "poor screenplay", 
    "good music", 
    "excellent climax", 
    "average performance", 
    "good cinematography" 
] 
Requirements 
Create the following functions: 
1. count_sentiments(reviews) 
Counts: 
• Excellent  
• Good  
• Average  
• Poor reviews  
2. most_common_word(reviews) 
Returns the most frequently occurring word. 
3. longest_review(reviews) 
Returns the review containing the maximum number of characters. 
4. reviews_with_keyword(reviews, keyword) 
Displays all reviews containing a given keyword. '''


# List of movie reviews
reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]


# Function to count sentiments
def count_sentiments(reviews):

    excellent = 0
    good = 0
    average = 0
    poor = 0

    # Traverse each review
    for review in reviews:

        if "excellent" in review:
            excellent += 1

        elif "good" in review:
            good += 1

        elif "average" in review:
            average += 1

        elif "poor" in review:
            poor += 1

    print("Excellent Reviews:", excellent)
    print("Good Reviews:", good)
    print("Average Reviews:", average)
    print("Poor Reviews:", poor)


def most_common_word(reviews):

    words = []

    for review in reviews:
        words.extend(review.split())

    unique_words = set(words)

    common_word = ""
    max_count = 0

    for word in unique_words:
        count = words.count(word)

        if count > max_count:
            max_count = count
            common_word = word

    return common_word


def longest_review(reviews):

    longest = reviews[0]

    i = 1

    while i < len(reviews):

        if len(reviews[i]) > len(longest):
            longest = reviews[i]

        i += 1

    return longest

# Function to display reviews containing a keyword
def reviews_with_keyword(reviews, keyword):

    for review in reviews:
        if keyword in review:
            print(review)



count_sentiments(reviews)

print("\nMost Common Word:")
print(most_common_word(reviews))

print("\nLongest Review:")
print(longest_review(reviews))

print("\nReviews containing 'excellent':")
reviews_with_keyword(reviews, "excellent")


'''Sample Output 
Excellent Reviews: 4 
Good Reviews: 2 
Average Reviews: 2 
Poor Reviews: 2 
 
Most Common Word: 
excellent 
 
Longest Review: 
good cinematography 
 
Reviews containing 'excellent': 
excellent movie 
excellent acting 
excellent visuals 
excellent climax '''
