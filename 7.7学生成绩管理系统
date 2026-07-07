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
