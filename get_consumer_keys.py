import tweepy

oauth1_user_handler = tweepy.OAuth1UserHandler(
    "API_KEY", "API_SECRET",
    callback="CALLBACK_URL"
)

print(oauth1_user_handler.get_authorization_url(signin_with_twitter=True))

code = input("Enter verifier: ")

access_token, access_token_secret = oauth1_user_handler.get_access_token(code)

print("Consumer key: " + access_token)
print("Consumer secret: " + access_token_secret)
