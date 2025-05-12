import pyshorteners

#create a shortener object
s = pyshorteners.Shortener()

# take input(long url)
long_url = input("Enter the long URL: ")
# shorten the url
short_url = s.tinyurl.short(long_url)
# print the short url
print("Short URL:", short_url)

# expanding the short url if required
expanded_url = s.tinyurl.expand(short_url)
# print the expanded url
print("Expanded URL:", expanded_url)