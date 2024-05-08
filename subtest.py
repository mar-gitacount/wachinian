import subprocess

# 任意の値をnumに代入
num = 10

# numが整数であるか確認
if isinstance(num, int):
    # 1からnumまでの範囲でループ
    process = subprocess.run(["python", "webdriverparts.py", str(num)])
    if process.returncode == 0:
        print(f"子プロセス {num} は正常に終了しました。")
    else:
        print(
            f"子プロセス {num} はエラー終了しました。終了コード: {process.returncode}"
        )
else:
    print("Error: num should be an integer.")
