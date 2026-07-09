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
