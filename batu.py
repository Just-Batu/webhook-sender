import requests
def send_discord_webhook(webhook_url, message, num_messages):
    data = {
        "content": message
    }
    
    for _ in range(num_messages):
        response = requests.post(webhook_url, json=data)
        
        if response.status_code == 204:
            print("☆☆☆ Made By Just-Batu --- Discord: medusamarka ★★★")
            print("Mesaj gönderildi.")
        else:
            print("Hata oluştu. Mesaj gönderilemedi.")

if __name__ == "__main__":
    webhook_url = input("Webhook URL'sini girin: ")
    message = input("Göndermek istediğiniz mesajı girin: ")
    num_messages = int(input("Kaç kez mesaj göndermek istiyorsunuz: "))

    send_discord_webhook(webhook_url, message, num_messages)
