import time
import winsound

def focus_timer(duration):
    print("专注时间开始！")
    time.sleep(duration * 60)  # 将分钟转换为秒并等待指定的时间

    # 专注时间结束后，播放提示音
    frequency = 2500  # 设置提示音频率（以赫兹为单位）
    duration = 2000  # 设置提示音持续时间（以毫秒为单位）
    winsound.Beep(frequency, duration)

    print("专注时间结束！")

if __name__ == "__main__":
    minutes = int(input("请输入专注时间（分钟）："))
    focus_timer(minutes)
