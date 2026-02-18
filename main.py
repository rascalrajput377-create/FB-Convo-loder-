import os
import requests
import time

# GitHub Secrets se details lena
TOKEN = os.getenv('FB_TOKEN')
COOKIE = os.getenv('FB_COOKIE')

def send_message(post_id, message):
    # Facebook Graph API endpoint
    url = f"https://graph.facebook.com{post_id}/comments"
    payload = {'message': message, 'access_token': TOKEN}
    headers = {'Cookie': COOKIE}
    
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            print(f"Success! Message sent to {post_id}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Failed: {e}")

# Example use (Aap isse loop mein bhi chala sakte hain)
if __name__ == "__main__":
    target_post = "YOUR_POST_ID_HERE" # Isse change karein
    msg = "Hello from Auto Bot!"
    send_message(target_post, msg)
