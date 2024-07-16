import os
import json
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager


def plot(
    values1,
    values2,
    labels1,
    labels2,
    label_one,
    label_two,
    left_text,
    right_text,
    file_name,
):
    # 加载 Noto Sans CJK JP 字体
    font_path = "NotoSansJP-Regular.ttf"
    font_manager.fontManager.addfont(font_path)
    plt.rcParams["font.family"] = "Noto Sans JP"

    # 示例数据
    groups = [
        "賀喜",
        "阪口",
        "井上",
        "清宮",
        "遠藤",
    ]
    colors1 = ["#ff9100", "#ff9100", "#fe0500", "#8e00ff", "#fe01a4"]
    colors2 = ["#02ff00", "#ff9100", "#ffffff", "#e4fa00", "#ffffff"]
    edgecolor = "black"  # 描边颜色

    # 设置字体和画幅大小
    plt.rcParams.update({"font.size": 20, "font.family": "Noto Sans JP"})
    fig, ax = plt.subplots(figsize=(19.20, 10.80))  # 设置画幅大小为1920x1080像素

    # 设置柱状图
    x = np.arange(len(groups))  # x轴位置
    width = 0.35  # 柱的宽度
    ax.set_ylim(0, 100)

    # 添加柱状图
    rects1 = ax.bar(
        x - width / 2,
        values1,
        width,
        label=label_one,
        color=colors1,
        edgecolor=edgecolor,
    )
    rects2 = ax.bar(
        x + width / 2,
        values2,
        width,
        label=label_two,
        color=colors2,
        edgecolor=edgecolor,
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
    ax.set_ylabel("分")
    ax.set_title("阪口と清宮、最後の握手会の待ち時間")
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    # 移除默认图例
    # ax.legend()

    # 添加自定义文字图例
    plt.text(0.95, 0.9, f"左    {label_one}", ha='right', va='center', transform=ax.transAxes, fontsize=14, color='black', bbox=dict(facecolor='none', edgecolor='none'))
    plt.text(0.95, 0.85, f"右    {label_two}", ha='right', va='center', transform=ax.transAxes, fontsize=14, color='black', bbox=dict(facecolor='none', edgecolor='none'))

    fig.tight_layout()


    # 保存图表为PNG文件
    plt.savefig(f"{file_name}.png", format="png")
    plt.close()


def gen_plot(
    hour_s,
    hour_e,
    min_s,
    min_e,
    code_left,
    code_right,
    data_left_index,
    data_right_index,
    right_text,
    label_left,
    label_right,
):
    for hour in range(hour_s, hour_e):
        for minute in range(min_s, min_e):
            for second in range(0, 60):
                # CST JST
                file_name = f"0714-{hour-1:02d}{minute:02d}{second:02d}.json"
                time_text = f"0714-{hour:02d}{minute:02d}"

                if os.path.exists(file_name):
                    print(file_name)
                    with open(file_name) as dict_file:
                        data = json.load(dict_file)
                        data_left = data["timezones"][data_left_index]["members"]
                        data_right = data["timezones"][data_right_index]["members"]

                        waitCount_left = list(
                            map(
                                lambda x: math.ceil(data_left[x]["totalCount"]),
                                code_left,
                            )
                        )
                        waitMinute_left = list(
                            map(
                                lambda x: math.ceil(data_left[x]["totalWait"] / 60),
                                code_left,
                            )
                        )
                        waitCount_right = list(
                            map(
                                lambda x: math.ceil(data_right[x]["totalCount"]),
                                code_right,
                            )
                        )
                        waitMinute_right = list(
                            map(
                                lambda x: math.ceil(data_right[x]["totalWait"] / 60),
                                code_right,
                            )
                        )

                        values1 = waitMinute_left
                        values2 = waitMinute_right
                        labels1 = list(
                            map(
                                lambda x, y: f"{x}人、{y}分",
                                waitCount_left,
                                waitMinute_left,
                            )
                        )
                        labels2 = list(
                            map(
                                lambda x, y: f"{x}人、{y}分",
                                waitCount_right,
                                waitMinute_right,
                            )
                        )
                        left_text = time_text

                        plot(
                            values1,
                            values2,
                            labels1,
                            labels2,
                            label_left,
                            label_right,
                            time_text,
                            right_text,
                            time_text,
                        )
                        break  # 1 graph every min


def main():
    code1 = [
        "ZZFA000072301",
        "ZZFA000072295",
        "ZZFA000072316",
        "ZZFA000072306",
        "ZZFA000072300",
    ]
    code2 = [
        "ZZFA000072330",
        "ZZFA000072324",
        "ZZFA000072345",
        "ZZFA000072335",
        "ZZFA000072329",
    ]
    code3 = [
        "ZZFA000072359",
        "ZZFA000072353",
        "ZZFA000072374",
        "ZZFA000072364",
        "ZZFA000072358",
    ]
    code4 = [
        "ZZFA000072388",
        "ZZFA000072382",
        "ZZFA000072403",
        "ZZFA000072393",
        "ZZFA000072387",
    ]
    code5 = [
        "ZZFA000072417",
        "ZZFA000072411",
        "ZZFA000072432",
        "ZZFA000072422",
        "ZZFA000072416",
    ]

    gen_plot(9, 10, 50, 60, code1, code2, 0, 1, "第1部前", "第1部", "第2部")

    gen_plot(10, 11, 0, 60, code1, code2, 0, 1, "第1部", "第1部", "第2部")
    gen_plot(11, 12, 0, 31, code1, code2, 0, 1, "第1部", "第1部", "第2部")

    gen_plot(11, 12, 31, 60, code1, code2, 0, 1, "第2部前", "第1部", "第2部")

    gen_plot(12, 13, 0, 60, code1, code2, 0, 1, "第2部", "第1部", "第2部")
    gen_plot(13, 14, 0, 31, code1, code2, 0, 1, "第2部", "第1部", "第2部")

    gen_plot(13, 14, 31, 60, code3, code2, 2, 1, "第3部前", "第3部", "第2部")
    gen_plot(14, 15, 0, 31, code3, code2, 2, 1, "第3部前", "第3部", "第2部")

    gen_plot(14, 15, 30, 60, code3, code2, 2, 1, "第3部", "第3部", "第2部")
    gen_plot(15, 16, 0, 60, code3, code2, 2, 1, "第3部", "第3部", "第2部")

    gen_plot(16, 17, 0, 31, code3, code4, 2, 3, "第4部前", "第3部", "第4部")

    gen_plot(16, 17, 30, 60, code3, code4, 2, 3, "第4部", "第3部", "第4部")
    gen_plot(17, 18, 0, 60, code3, code4, 2, 3, "第4部", "第3部", "第4部")

    gen_plot(18, 19, 0, 31, code5, code4, 4, 3, "第5部前", "第5部", "第4部")

    gen_plot(18, 19, 30, 60, code5, code4, 4, 3, "第5部", "第5部", "第4部")
    gen_plot(19, 20, 0, 60, code5, code4, 4, 3, "第5部", "第5部", "第4部")
    gen_plot(20, 21, 0, 60, code5, code4, 4, 3, "第5部", "第5部", "第4部")
    gen_plot(21, 22, 0, 60, code5, code4, 4, 3, "第5部", "第5部", "第4部")


if __name__ == "__main__":
    main()