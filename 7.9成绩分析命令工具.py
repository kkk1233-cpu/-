import numpy as np

# 存学生名字和对应分数
names = []
scores = []

def print_menu():
    print("----------------------------------------")
    print("            成绩分析系统")
    print("----------------------------------------")
    print("1. 输入成绩数据")
    print("2. 查看成绩统计")
    print("3. 查看成绩排名")
    print("4. 查看成绩分布")
    print("5. 查询学生成绩")
    print("6. 退出系统")
    print("----------------------------------------")

def add_data():
    # 清空上次录入的数据
    names.clear()
    scores.clear()
    try:
        student_num = int(input("请输入学生人数："))
    except:
        print("人数必须填数字，本次录入取消")
        return
    for n in range(student_num):
        st_name = input(f"请输入第{n+1}个学生姓名：")
        while True:
            try:
                st_score = int(input("请输入成绩："))
                if 0 <= st_score <= 100:
                    break
                print("分数只能0-100之间，重新输入")
            except:
                print("成绩要输入整数，重新填")
        names.append(st_name)
        scores.append(st_score)
    print("所有学生成绩录入完成\n")

def calc_stat():
    if len(scores) == 0:
        print("还没有录入任何成绩，先去录入数据！\n")
        return
    score_arr = np.array(scores)
    avg = np.mean(score_arr)
    max_s = np.max(score_arr)
    min_s = np.min(score_arr)
    var_s = np.var(score_arr)
    std_s = np.std(score_arr)
    print("\n====成绩统计信息====")
    print(f"平均分：{avg:.2f}")
    print(f"最高分：{max_s}")
    print(f"最低分：{min_s}")
    print(f"方差：{var_s:.2f}")
    print(f"标准差：{std_s:.2f}\n")

def rank_sort():
    if not scores:
        print("暂无成绩数据，请先录入\n")
        return
    arr = np.array(scores)
    student_info = list(zip(names, scores))
    student_info.sort(key=lambda x:x[1], reverse=True)
    print("\n====成绩排名（高分在前）====")
    for pos in range(len(student_info)):
        print(f"第{pos+1}名  {student_info[pos][0]}  {student_info[pos][1]}分")
    print()

def level_count():
    if len(scores) == 0:
        print("暂无成绩数据，请先录入\n")
        return
    arr = np.array(scores)
    exc = np.sum(arr >= 90)
    good = np.sum((arr >= 80) & (arr < 90))
    mid = np.sum((arr >= 60) & (arr < 80))
    bad = np.sum(arr < 60)
    total = len(arr)
    print("\n====成绩等级分布====")
    print(f"优秀(90~100)：{exc}人，占比{exc/total*100:.1f}%")
    print(f"良好(80~89)：{good}人，占比{good/total*100:.1f}%")
    print(f"及格(60~79)：{mid}人，占比{mid/total*100:.1f}%")
    print(f"不及格(0~59)：{bad}人，占比{bad/total*100:.1f}%\n")
