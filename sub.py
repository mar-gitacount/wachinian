import subprocess
from datetime import datetime

# 任意の値をnumに代入
num = 80
today_date_file = datetime.now().strftime("%Y%m%d") + "error.txt"


def save_logs_to_file(logs, file_path):
    # ここでアイテム一覧の配列を作ってしまう。
    # ここでの配列は二つで一つの二次元配列になる。

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(str(logs) + "\n")


# numが整数であるか確認
if isinstance(num, int):
    # 1からnumまでの範囲でループ
    for i in range(1, num + 1):
        # subprocessモジュールを使用して別のPythonスクリプトを呼び出す
        # 引数としてiの値を渡す
        process = subprocess.run(["python", "webdriverparts.py", str(i)])
        # 子プロセスの終了コードを確認
        if process.returncode == 0:
            print(f"子プロセス {i} は正常に終了しました。")
            success_process = f"子プロセス {i} は正常に終了しました。"
            save_logs_to_file(success_process, today_date_file)
        else:
            print(
                f"子プロセス {i} はエラー終了しました。終了コード: {process.returncode}"
            )
            error_process = (
                f"子プロセス {i} はエラー終了しました。終了コード: {process.returncode}"
            )
            save_logs_to_file(error_process, today_date_file)
            # process = subprocess.run(["python", "webdriver2.py", str(i)])
else:
    print("Error: num should be an integer.")
