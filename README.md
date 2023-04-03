# AutomatedCats

So,
I automated this using PipeDream with a little bit of my own code.

I started off by creating a trigger that automatically runs the code every 5 minutes.
![image](https://user-images.githubusercontent.com/66801986/229467375-c19f38b3-c637-458b-9442-7007527e717c.png)

After that, I used my own piece of code which is in [get_image.js](https://github.com/5vl/AutomatedCats/blob/main/get_image.js)

Then, I used the "upload_media" Twitter workflow on Pipedream with the below info set:
![image](https://user-images.githubusercontent.com/66801986/229467896-c5ad7638-bad8-4a7a-a2f9-a1230b6dfb20.png)

Lastly, I used the "twitter_create_tweet" workflow to actually post the image + a message!
![image](https://user-images.githubusercontent.com/66801986/229468270-1840c330-95fb-4031-8af4-4e9367c1258b.png)
