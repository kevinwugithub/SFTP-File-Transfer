# SFTP-File-Transfer
本 Python 工具使用 paramiko 函式庫建立 SSH 連線，並透過 SFTP 進行安全的檔案傳輸。

## 函式說明
create_ssh_client(hostname, username, password)
此函式會建立並回傳一個已連線至指定主機的 SSH client。參數如下：

- hostname：遠端主機的主機名稱或 IP 位址。
- username：用於驗證的使用者名稱。
- password：用於驗證的密碼。

sftp_to_remote(ssh, local_path, remote_path)

此函式會將本地系統的檔案上傳至遠端系統。參數如下：

- ssh：一個已啟用的 SSH client 實例。
- local_path：本地系統上的檔案路徑。
- remote_path：檔案在遠端系統上儲存的位置。

此函式會回傳一個包含 status 鍵的字典。若檔案傳輸成功，status 為 "success"。若發生錯誤，status 為 "error"，並會有 message 鍵說明錯誤原因。

sftp_from_remote(ssh, local_path, remote_path)

此函式會將遠端系統的檔案下載到本地系統。參數如下：

- ssh：一個已啟用的 SSH client 實例。
- local_path：檔案在本地系統儲存的位置。
- remote_path：遠端系統上的檔案路徑。

此函式會回傳一個包含 status 鍵的字典。若檔案傳輸成功，status 為 "success"。若發生錯誤，status 為 "error"，並會有 message 鍵說明錯誤原因。


## 相依套件
本腳本需安裝 paramiko 函式庫。你可以使用 pip 安裝：

```sh
pip install -r requirements.txt
```

## 使用方式
你可以在自己的 Python 腳本中使用這些函式來進行安全的 SSH 檔案傳輸。以下為範例：

```sh
ssh_session = create_ssh_client(hostname="192.168.178.153", username="root", password="password")
scp_from_remote(ssh_session, local_path="interfaces.xml", remote_path="/root/interfaces.xml")
```

