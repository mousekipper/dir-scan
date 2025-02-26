import requests

def directory_scanner(base_url, file_list):

    for file in file_list:
        url = f"{base_url}/{file}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[+] founded file/directory: {url}")

# 실행
target_url = "TARGET_URL"
hidden_files = ["admin", "backup.zip", "config.php", "secret"]
directory_scanner(target_url, hidden_files)
