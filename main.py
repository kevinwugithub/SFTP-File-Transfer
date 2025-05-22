import paramiko  # 匯入 paramiko 套件，用來進行 SSH 和 SFTP 連線

# 建立 SSH 連線客戶端
def create_ssh_client(hostname, username, password):
    ssh = paramiko.SSHClient()  # 建立 SSHClient 物件
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自動接受新的主機金鑰（不建議用於正式環境）
    ssh.connect(hostname, username=username, password=password)  # 連接到遠端主機
    return ssh  # 回傳 SSH 連線物件

# 上傳檔案到遠端伺服器
def sftp_to_remote(ssh, local_path, remote_path):
    try:
        sftp = ssh.open_sftp()  # 開啟 SFTP 連線
        sftp.put(local_path, remote_path)  # 上傳本機檔案到遠端
        sftp.close()  # 關閉 SFTP 連線
        return {"status": "success"}  # 回傳成功訊息
    except Exception as e:
        return {"status": "error", "message": str(e)}  # 回傳錯誤訊息

# 從遠端伺服器下載檔案到本機
def sftp_from_remote(ssh, local_path, remote_path):
    try:
        sftp = ssh.open_sftp()  # 開啟 SFTP 連線
        sftp.get(remote_path, local_path)  # 下載遠端檔案到本機
        sftp.close()  # 關閉 SFTP 連線
        return {"status": "success"}  # 回傳成功訊息
    except Exception as e:
        return {"status": "error", "message": str(e)}  # 回傳錯誤訊息
