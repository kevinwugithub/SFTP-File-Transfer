import paramiko  # 匯入 paramiko 套件，用來進行 SSH 和 SFTP 連線
from typing import Dict  # 匯入型別提示

# 建立 SSH 連線客戶端
# 警告：AutoAddPolicy 僅建議用於測試環境，正式環境請妥善管理主機金鑰。
def create_ssh_client(hostname: str, username: str, password: str) -> paramiko.SSHClient:
    ssh = paramiko.SSHClient()  # 建立 SSHClient 物件
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自動接受新的主機金鑰（不建議用於正式環境）
    ssh.connect(hostname, username=username, password=password)  # 連接到遠端主機
    return ssh  # 回傳 SSH 連線物件

# 上傳檔案到遠端伺服器
def sftp_to_remote(ssh: paramiko.SSHClient, local_path: str, remote_path: str) -> Dict[str, str]:
    try:
        # 使用 with 語法自動管理 SFTP 連線資源，確保即使發生例外也能正確關閉
        with ssh.open_sftp() as sftp:
            sftp.put(local_path, remote_path)  # 上傳本機檔案到遠端
        return {"status": "success"}  # 回傳成功訊息
    except FileNotFoundError:
        return {"status": "error", "message": "本地檔案不存在"}  # 本地檔案不存在
    except PermissionError:
        return {"status": "error", "message": "權限不足"}  # 權限不足
    except Exception as e:
        return {"status": "error", "message": str(e)}  # 其他錯誤訊息

# 從遠端伺服器下載檔案到本機
def sftp_from_remote(ssh: paramiko.SSHClient, local_path: str, remote_path: str) -> Dict[str, str]:
    try:
        # 使用 with 語法自動管理 SFTP 連線資源，確保即使發生例外也能正確關閉
        with ssh.open_sftp() as sftp:
            sftp.get(remote_path, local_path)  # 下載遠端檔案到本機
        return {"status": "success"}  # 回傳成功訊息
    except FileNotFoundError:
        return {"status": "error", "message": "遠端檔案不存在"}  # 遠端檔案不存在
    except PermissionError:
        return {"status": "error", "message": "權限不足"}  # 權限不足
    except Exception as e:
        return {"status": "error", "message": str(e)}  # 其他錯誤訊息
