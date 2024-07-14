import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager


def plot(values1, values2, labels1, labels2, left_text, right_text, file_name):
    # 下载并加载 Noto Sans CJK JP 字体
    font_path = "NotoSansJP-Regular.ttf"
    font_manager.fontManager.addfont(font_path)
    plt.rcParams["font.family"] = "Noto Sans JP"

    # 示例数据
    groups = ["遠藤", "清宮", "井上", "阪口", "賀喜"]
    # values1 = [10, 20, 30, 40, 500]
    # values2 = [15, 25, 35, 45, 55]
    # labels1 = ["ラベル1", "ラベル2", "ラベル3", "ラベル4", "ラベル5"]
    # labels2 = ["sdf", "ラベル2", "ラベル3", "ラベル4", "ラベル5"]
    # left_text = "柱状図のddd例"
    # right_text = "柱状図dsdfの例"
    colors1 = ["#fe01a4", "#ff9100", "#fe0500", "#8e00ff", "#ff9100"]
    colors2 = ["#ffffff", "#ff9100", "#ffffff", "#e4fa00", "#02ff00"]
    edgecolor = "black"  # 描边颜色

    # 设置字体和画幅大小
    plt.rcParams.update({"font.size": 14, "font.family": "Noto Sans JP"})
    fig, ax = plt.subplots(figsize=(19.20, 10.80))  # 设置画幅大小为1920x1080像素

    # 设置柱状图
    x = np.arange(len(groups))  # x轴位置
    width = 0.35  # 柱的宽度
    ax.set_ylim(0, 100)

    # 添加柱状图
    rects1 = ax.bar(
        x - width / 2, values1, width, label="列1", color=colors1, edgecolor=edgecolor
    )
    rects2 = ax.bar(
        x + width / 2, values2, width, label="列2", color=colors2, edgecolor=edgecolor
    )

    # 添加标记
    def add_labels(rects, labels):
        for rect, label in zip(rects, labels):
            height = rect.get_height()
            ax.annotate(
                f"{label}",
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha="center",
                va="bottom",
            )

    add_labels(rects1, labels1)
    add_labels(rects2, labels2)

    # 添加标题
    plt.title(right_text, loc="right")
    plt.title(left_text, loc="left")

    # 添加标签和图例
    # ax.set_xlabel("グループ")
    ax.set_ylabel("分")
    ax.set_title("阪口と清宮、最後の握手会")
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    ax.legend()

    fig.tight_layout()

    # 保存图表为PNG文件
    plt.savefig(f"{file_name}.png", format="png")
    plt.close()


import os
import json
import math


def main():

    for hour in range(9, 10):
        for minute in range(50, 60):
            for second in range(0, 60):
                code = [
                    "ZZFA000072300",
                    "ZZFA000072306",
                    "ZZFA000072316",
                    "ZZFA000072295",
                    "ZZFA000072301",
                ]
                # print(hour,minute,second)
                file_name = f"0714-{hour-1:02d}{minute:02d}{second:02d}.json"
                # print(file_name)
                if os.path.exists(file_name):
                    print(file_name)
                    with open(file_name) as dict:
                        data = json.load(dict)
                        data = data["timezones"][0]["members"]

                        waitCount = list(
                            map(lambda x: math.ceil(data[x]["totalCount"]), code)
                        )
                        waitMinute = list(
                            map(lambda x: math.ceil(data[x]["totalWait"] / 60), code)
                        )
                        values1 = waitMinute
                        values2 = [0, 0, 0, 0, 0]
                        labels1 = list(
                            map(
                                lambda x, y: f"{x}人、{y}分",
                                waitCount,
                                waitMinute,
                            )
                        )
                        labels2 = ["", "", "", "", ""]
                        left_text = file_name
                        right_text = "一部前"

                        plot(
                            values1,
                            values2,
                            labels1,
                            labels2,
                            left_text,
                            right_text,
                            file_name,
                        )
                        break # 1 graph every min


main()
