import os
import requests
import time

# GitHub Secrets se details lena
TOKEN = os.getenv('FB_TOKEN')
COOKIE = os.getenv('FB_COOKIE')

def send_comment(post_id, message):
    # Sahi Graph API URL
    url = f"https://graph.facebook.com{post_id}/comments"
    payload = {'message': message, 'access_token': TOKEN}
    headers = {'Cookie': COOKIE}
    
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            print(f"✅ Success! Message sent to {post_id}")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"⚠️ Failed: {e}")

if __name__ == "__main__":
    # Yahan apni Post ID aur Message dalein
    target_post = "100022256290881" 
    messages_list = ["Hello!", "Nice Post!", "Auto Bot Active!", "Cool!"] # Aap list badal sakte hain
    
    print("🚀 Bot starting...")
    
    # Ye loop 5 baar comment karega (Aap ise badal sakte hain)
    for i in range(5):
        msg = messages_list[i % len(messages_list)]
        send_comment(target_post, msg)
        
        # 60 seconds ka wait taaki account safe rahe
        if i < 4: 
            print("⏳ Waiting 60 seconds before next comment...")
            time.sleep(60)

    print("🏁 Task Completed!")
