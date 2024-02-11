import requests

def check_bropoll_api_status():
    try:
        response = requests.get("https://ljns.fr:8512/api-spring/api/ping")
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print("Une erreur s'est produite :", e)
        return False

def check_blog_esport_api_status():
    try:
        response = requests.get("https://ljns.fr:8562/api/health")
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print("Une erreur s'est produite :", e)
        return False