# AutomatedCats

So,
I automated this using PipeDream some of my own code.

I started off by creating a trigger that automatically runs the code every 5 minutes.
![image](https://user-images.githubusercontent.com/66801986/229467375-c19f38b3-c637-458b-9442-7007527e717c.png)

After that, I created a method that refreshes my token every hour so it doesn't expire (which takes around 2 hours), and you can find it at [get_auth_token.js](https://github.com/5vl/AutomatedCats/blob/main/get_auth_token.js).

Then I used some Python because it was a lot easier to work with for this, it gets the cat image, saves it to a temp file which gets deleted later, uploads the image to Twitter and gets the media id from that, then it creates a new tweet with the image and some text! You can find that code here: [get_cat_and_post.py](https://github.com/5vl/AutomatedCats/blob/main/get_cat_and_post.py).

I also needed consumer keys, so I created a quick [get_consumer_keys.py](https://github.com/5vl/AutomatedCats/blob/main/get_consumer_keys.py) for that. It's not great, but does the job.
After you do that you can paste in the keys in the other python file and it should work!

Happy catting!
