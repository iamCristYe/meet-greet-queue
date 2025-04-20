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
    groups_N6 = [
        "海邉朱莉",  # P1 ZZFA000097459 P2 ZZFA000097464
        "川端晃菜",
        "瀬戸口心月",
        "長嶋凛桜",
        "矢田萌華",
        "愛宕心響  ",  # P4 ZZFA000097469 P5 ZZFA000097475
        "大越ひなの",
        "小津玲奈",
        "鈴木佑捺",
        "増田三莉音",
        "森平麗心",
    ]

    groups_N = [
        "五百城茉央",
        "池田瑛紗",
        "一ノ瀬美空",
        "井上和",
        "岡本姫奈",
        "小川彩",
        "奥田いろは",
        "川﨑桜",
        "菅原咲月",
        "冨里奈央",
        "中西アルノ",
    ]
    groups_H = [
        "石塚瑶季",
        "小西夏菜実",
        "清水理央",
        "正源司陽子",
        "竹内希来里",
        "平尾帆夏",
        "平岡海月",
        "藤嶌果歩",
        "宮地すみれ",
        "山下葉留花",
        "渡辺莉奈",
    ]
    groups_S = [
        "石森璃花",
        "遠藤理子",
        "小田倉麗奈",
        "小島凪紗",
        "谷口愛季",
        "中嶋優月",
        "的野美青",
        "向井純葉",
        "村井優",
        "村山美羽",
        "山下瞳月",
    ]
    # color = "#5BBEE4"  # H
    color = "#812990"  # N
    # color = "#f19db5"  # S
    colors1 = [
        color,
        color,
        color,
        color,
        color,
        color,
        color,
        color,
        color,
        color,
    ]
    colors2 = [
        color,
        color,
        color,
        color,
        color,
        color,
        color,
        color,
        color,
        color,
    ]
    edgecolor = color  # 描边颜色

    # 设置字体和画幅大小
    plt.rcParams.update({"font.size": 20, "font.family": "Noto Sans JP"})
    fig, ax = plt.subplots(figsize=(19.20, 10.80))  # 设置画幅大小为1920x1080像素

    groups = groups_N6

    # 设置柱状图
    x = np.arange(len(groups))  # x轴位置
    width = 0.35  # 柱的宽度
    ax.set_ylim(0, 60)

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
    # ax.set_title("10月27日、櫻坂46三期生のミーグリの待ち時間")
    ax.set_title("乃木坂46、6期生の初めてのミーグリの待ち時間")
    # ax.set_title("10月27日、日向坂46四期生のミーグリの待ち時間")
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    # 移除默认图例
    # ax.legend()

    # 添加自定义文字图例
    plt.text(
        0.95,
        0.9,
        f"左    {label_one}",
        ha="right",
        va="center",
        transform=ax.transAxes,
        fontsize=14,
        color="black",
        bbox=dict(facecolor="none", edgecolor="none"),
    )
    plt.text(
        0.95,
        0.85,
        f"右    {label_two}",
        ha="right",
        va="center",
        transform=ax.transAxes,
        fontsize=14,
        color="black",
        bbox=dict(facecolor="none", edgecolor="none"),
    )

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
                file_name = (
                    f"20250420/e25693_0420-{hour:02d}{minute:02d}{second:02d}.json"
                )
                time_text = f"20250420/20250420-{hour:02d}{minute:02d}"

                if os.path.exists(file_name):
                    print(file_name)
                    with open(file_name) as dict_file:
                        data = json.load(dict_file)
                        data_left = data["timezones"][data_left_index]["members"]
                        data_right = data["timezones"][data_right_index]["members"]

                        # 小田倉麗奈

                        data_left["ZZFA000086313"] = {"totalCount": 0, "totalWait": 0}
                        data_left["ZZFA000086340"] = {"totalCount": 0, "totalWait": 0}
                        data_left["ZZFA000086367"] = {"totalCount": 0, "totalWait": 0}
                        data_left["ZZFA000086394"] = {"totalCount": 0, "totalWait": 0}
                        data_left["ZZFA000086421"] = {"totalCount": 0, "totalWait": 0}
                        data_left["ZZFA000086448"] = {"totalCount": 0, "totalWait": 0}

                        data_right["ZZFA000086313"] = {"totalCount": 0, "totalWait": 0}
                        data_right["ZZFA000086340"] = {"totalCount": 0, "totalWait": 0}
                        data_right["ZZFA000086367"] = {"totalCount": 0, "totalWait": 0}
                        data_right["ZZFA000086394"] = {"totalCount": 0, "totalWait": 0}
                        data_right["ZZFA000086421"] = {"totalCount": 0, "totalWait": 0}
                        data_right["ZZFA000086448"] = {"totalCount": 0, "totalWait": 0}

                        waitCount_left = list(
                            map(
                                lambda x: math.ceil(
                                    data_left[x]["totalCount"] if x in data_left else 0
                                ),
                                code_left,
                            )
                        )
                        waitMinute_left = list(
                            map(
                                lambda x: math.ceil(
                                    data_left[x]["totalWait"] / 60
                                    if x in data_left
                                    else 0
                                ),
                                code_left,
                            )
                        )
                        waitCount_right = list(
                            map(
                                lambda x: math.ceil(
                                    data_right[x]["totalCount"] if x in data_right else 0
                                ),
                                code_right,
                            )
                        )
                        waitMinute_right = list(
                            map(
                                lambda x: math.ceil(
                                    data_right[x]["totalWait"] / 60
                                    if x in data_right
                                    else 0
                                ),
                                code_right,
                            )
                        )

                        values1 = waitMinute_left
                        values2 = waitMinute_right
                        labels1 = list(
                            map(
                                lambda x, y: "" if x == 0 else f"{x}人、{y}分",
                                waitCount_left,
                                waitMinute_left,
                            )
                        )
                        labels2 = list(
                            map(
                                lambda x, y: "" if x == 0 else f"{x}人、{y}分",
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
    prefix = "ZZFA0000"
    code1 = []
    code2 = []
    code3 = []
    code4 = []
    code5 = []
    code6 = []
    # start = 97469 - 6
    # period = 6
    # for i in range(0, 11):
    #     code1.append(f"{prefix}{start+period*0+i:04}")
    #     code2.append(f"{prefix}{start+period*1+i:04}")
    #     code3.append(f"{prefix}{start+period*2+i:04}")
    #     code4.append(f"{prefix}{start+period*3+i:04}")
    #     code5.append(f"{prefix}{start+period*4+i:04}")
    #     code6.append(f"{prefix}{start+period*5+i:04}")

    # print(code1)
    # print(code2)
    # print(code3)
    # print(code4)
    # print(code5)
    # print(code6)

    code1 = [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ]

    code2 = [
        "ZZFA000097459",
        "ZZFA000097460",
        "ZZFA000097461",
        "ZZFA000097462",
        "ZZFA000097463",
        "",
        "",
        "",
        "",
        "",
        "",
    ]
    code3 = [
        "ZZFA000097464",
        "ZZFA000097465",
        "ZZFA000097466",
        "ZZFA000097467",
        "ZZFA000097468",
        "",
        "",
        "",
        "",
        "",
        "",
    ]
    code4 = [
        "",
        "",
        "",
        "",
        "",
        "ZZFA000097469",
        "ZZFA000097470",
        "ZZFA000097471",
        "ZZFA000097472",
        "ZZFA000097473",
        "ZZFA000097474",
    ]
    code5 = [
        "",
        "",
        "",
        "",
        "",
        "ZZFA000097475",
        "ZZFA000097476",
        "ZZFA000097477",
        "ZZFA000097478",
        "ZZFA000097479",
        "ZZFA000097480",
    ]
    if True:  # "N"
        gen_plot(9, 10, 45, 60, code1, code2, 0, 1, "第1部前", "第1部", "第2部")

        gen_plot(10, 11, 0, 60, code1, code2, 0, 1, "第1部", "第1部", "第2部")
        gen_plot(11, 12, 0, 31, code1, code2, 0, 1, "第1部", "第1部", "第2部")

        gen_plot(11, 12, 30, 60, code1, code2, 0, 1, "第2部前", "第1部", "第2部")

        gen_plot(12, 13, 0, 60, code1, code2, 0, 1, "第2部", "第1部", "第2部")
        gen_plot(13, 14, 0, 31, code1, code2, 0, 1, "第2部", "第1部", "第2部")

        gen_plot(13, 14, 30, 60, code3, code2, 2, 1, "第3部前", "第3部", "第2部")
        gen_plot(14, 15, 0, 30, code3, code2, 2, 1, "第3部前", "第3部", "第2部")

        gen_plot(14, 15, 30, 60, code3, code2, 2, 1, "第3部", "第3部", "第2部")
        gen_plot(15, 16, 0, 60, code3, code2, 2, 1, "第3部", "第3部", "第2部")

        gen_plot(16, 17, 0, 30, code3, code4, 2, 3, "第4部前", "第3部", "第4部")

        gen_plot(16, 17, 30, 60, code3, code4, 2, 3, "第4部", "第3部", "第4部")
        gen_plot(17, 18, 0, 60, code3, code4, 2, 3, "第4部", "第3部", "第4部")

        gen_plot(18, 19, 0, 30, code5, code4, 4, 3, "第5部前", "第5部", "第4部")

        gen_plot(18, 19, 30, 60, code5, code4, 4, 3, "第5部", "第5部", "第4部")
        gen_plot(19, 20, 0, 60, code5, code4, 4, 3, "第5部", "第5部", "第4部")
        gen_plot(20, 21, 0, 60, code5, code4, 4, 3, "第5部", "第5部", "第4部")
        gen_plot(21, 22, 0, 60, code5, code4, 4, 3, "第5部", "第5部", "第4部")

    if False:  # "H"
        gen_plot(10, 11, 45, 60, code1, code2, 0, 1, "第1部前", "第1部", "第2部")

        gen_plot(11, 12, 0, 60, code1, code2, 0, 1, "第1部", "第1部", "第2部")

        gen_plot(12, 13, 0, 30, code1, code2, 0, 1, "第2部前", "第1部", "第2部")

        gen_plot(12, 13, 30, 60, code1, code2, 0, 1, "第2部", "第1部", "第2部")
        gen_plot(13, 14, 0, 31, code1, code2, 0, 1, "第2部", "第1部", "第2部")

        gen_plot(13, 14, 31, 60, code3, code2, 2, 1, "第3部前", "第3部", "第2部")

        gen_plot(14, 15, 0, 60, code3, code2, 2, 1, "第3部", "第3部", "第2部")

        gen_plot(15, 16, 0, 60, code3, code4, 2, 3, "第4部前", "第3部", "第4部")

        gen_plot(16, 17, 0, 60, code3, code4, 2, 3, "第4部", "第3部", "第4部")

        gen_plot(17, 18, 0, 30, code5, code4, 4, 3, "第5部前", "第5部", "第4部")

        gen_plot(17, 18, 30, 60, code5, code4, 4, 3, "第5部", "第5部", "第4部")
        gen_plot(18, 19, 0, 31, code5, code4, 4, 3, "第5部", "第5部", "第4部")

        gen_plot(18, 19, 31, 60, code5, code6, 4, 5, "第6部前", "第5部", "第6部")

        gen_plot(19, 20, 0, 60, code5, code6, 4, 5, "第6部", "第5部", "第6部")
        gen_plot(20, 21, 0, 60, code5, code6, 4, 5, "第6部", "第5部", "第6部")

    if False:  # S
        gen_plot(10, 11, 45, 60, code1, code2, 0, 1, "第1部前", "第1部", "第2部")

        gen_plot(11, 12, 0, 60, code1, code2, 0, 1, "第1部", "第1部", "第2部")

        gen_plot(12, 13, 0, 30, code1, code2, 0, 1, "第2部前", "第1部", "第2部")

        gen_plot(12, 13, 30, 60, code1, code2, 0, 1, "第2部", "第1部", "第2部")
        gen_plot(13, 14, 0, 31, code1, code2, 0, 1, "第2部", "第1部", "第2部")

        gen_plot(13, 14, 31, 60, code3, code2, 2, 1, "第3部前", "第3部", "第2部")
        gen_plot(14, 15, 0, 30, code3, code2, 2, 1, "第3部前", "第3部", "第2部")

        gen_plot(14, 15, 30, 0, code3, code2, 2, 1, "第3部", "第3部", "第2部")
        gen_plot(15, 16, 0, 30, code3, code2, 2, 1, "第3部", "第3部", "第2部")

        gen_plot(15, 16, 30, 60, code3, code4, 2, 3, "第4部前", "第3部", "第4部")

        gen_plot(16, 17, 0, 60, code3, code4, 2, 3, "第4部", "第3部", "第4部")

        gen_plot(17, 18, 0, 30, code5, code4, 4, 3, "第5部前", "第5部", "第4部")

        gen_plot(17, 18, 30, 60, code5, code4, 4, 3, "第5部", "第5部", "第4部")
        gen_plot(18, 19, 0, 31, code5, code4, 4, 3, "第5部", "第5部", "第4部")

        gen_plot(18, 19, 31, 60, code5, code6, 4, 5, "第6部前", "第5部", "第6部")

        gen_plot(19, 20, 0, 60, code5, code6, 4, 5, "第6部", "第5部", "第6部")
        gen_plot(20, 21, 0, 60, code5, code6, 4, 5, "第6部", "第5部", "第6部")


if __name__ == "__main__":
    main()
