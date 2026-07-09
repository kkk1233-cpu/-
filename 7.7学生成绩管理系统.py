student_data = []

def show_menu():
    print("\n========== 学生成绩管理系统 ==========")
    print("1. 新增学生成绩信息")
    print("2. 根据姓名/学号查询学生")
    print("3. 全部学生成绩综合统计")
    print("0. 退出管理系统")
    print("======================================")

while True:
    show_menu()
    select = input("请输入功能编号：")

    if select == "1":
        stu_id = input("请输入学生学号：")
        repeat = False
        for s in student_data:
            if s["stu_id"] == stu_id:
                repeat = True
                break
        if repeat:
            print("该学号已存在，无法重复录入！")
            continue

        name = input("请输入学生姓名：")
        subject_list = input("输入科目名称（空格隔开，如语文 数学 英语）：").split()
        score_list = []
        for sub in subject_list:
            score = float(input(f"请输入{sub}成绩："))
            score_list.append(score)

        student = {
            "name": name,
            "stu_id": stu_id,
            "subjects": subject_list,
            "scores": score_list
        }
        student_data.append(student)
        print(f"{name} 信息录入成功！")

    elif select == "2":
        keyword = input("输入姓名或学号进行查询：")
        has_data = False
        for stu in student_data:
            if keyword in stu["name"] or keyword == stu["stu_id"]:
                print("\n-------- 学生详情 --------")
                print(f"姓名：{stu['name']}  学号：{stu['stu_id']}")
                for sub, sc in zip(stu["subjects"], stu["scores"]):
                    print(f"{sub}：{sc}分")
                avg = sum(stu["scores"]) / len(stu["scores"])
                print(f"平均分：{avg:.2f}")
                print(f"单科最高分：{max(stu['scores'])}")
                print(f"单科最低分：{min(stu['scores'])}")
                has_data = True
        if not has_data:
            print("未匹配到对应学生")

    elif select == "3":
        if len(student_data) == 0:
            print("暂无任何学生数据，请先录入！")
            continue
        all_score = []
        pass_count = 0
        for stu in student_data:
            all_score.extend(stu["scores"])
            for s in stu["scores"]:
                if s >= 60:
                    pass_count += 1
        total_avg = sum(all_score) / len(all_score)
        print("\n-------- 全班成绩统计 --------")
        print(f"所有科目总平均分：{total_avg:.2f}")
        print(f"全体最高单科分：{max(all_score)}")
        print(f"全体最低单科分：{min(all_score)}")
        print(f"及格科目总数（≥60）：{pass_count}")

    elif select == "0":
        print("程序结束，感谢使用！")
        break

    else:
        print("输入错误，请选择0~3之间的数字！")

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
    
    def find_single():
    target = input("请输入要查询的学生姓名：")
    if target in names:
        index = names.index(target)
        mark = scores[index]
        # 手动判定等级
        if mark >= 90:
            lv = "优秀"
        elif mark >= 80:
            lv = "良好"
        elif mark >= 60:
            lv = "及格"
        else:
            lv = "不及格"
        print(f"\n{target} 的成绩：{mark}，等级：{lv}\n")
    else:
        print("系统里没有这个学生\n")

# 主循环运行程序
if __name__ == "__main__":
    while 1:
        print_menu()
        try:
            opt = int(input("请选择："))
        except:
            print("只能输入数字1-6！")
            continue
        if opt == 1:
            add_data()
        elif opt == 2:
            calc_stat()
        elif opt == 3:
            rank_sort()
        elif opt == 4:
            level_count()
        elif opt == 5:
            find_single()
        elif opt == 6:
            print("系统退出，结束运行")
            break
        else:
            print("输入超出1-6范围，请重新选择\n")
