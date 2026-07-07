import math
import time

def calc_add(num1, num2):
    return num1 + num2

def calc_sub(num1, num2):
    return num1 - num2

def calc_mul(num1, num2):
    return num1 * num2

def calc_div(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("除数不能为0")
    return num1 / num2

def calc_mod(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("模数不能为0")
    return num1 % num2

def calc_pow(num1, num2):
    return num1 ** num2

def calc_sqrt(num):
    if num < 0:
        raise ValueError("负数不支持开平方")
    return math.sqrt(num)

def save_calc_log(expression, res):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_text = f"[{now}] {expression} = {res:.2f}"
    with open("calc_record.txt", "a", encoding="utf-8") as f:
        f.write(log_text + "\n")

def read_calc_log():
    try:
        with open("calc_record.txt", "r", encoding="utf-8") as f:
            record_list = f.readlines()
        if not record_list:
            print("暂无任何计算记录")
            return
        print("\n======== 历史计算记录 ========")
        for line in record_list:
            print(line.strip())
    except FileNotFoundError:
        print("日志文件不存在，还没有计算记录")

def print_calc_menu():
    print("\n======== 多功能计算器 ========")
    print("1.加法  2.减法  3.乘法  4.除法")
    print("5.取模  6.幂运算  7.开平方")
    print("8.查看历史记录  0.退出计算器")
    print("==============================")

def calculator_main():
    while True:
        print_calc_menu()
        op_choice = input("请选择运算类型：")
        if op_choice == "0":
            print("计算器已关闭")
            break
        try:
            if op_choice == "8":
                read_calc_log()
                continue
            if op_choice == "7":
                n = float(input("输入待开方数字："))
                result = calc_sqrt(n)
                expr = f"√{n}"
                print(f"计算结果：{result:.2f}")
                save_calc_log(expr, result)
                continue
            a = float(input("输入第一个数字："))
            b = float(input("输入第二个数字："))
            res = 0
            exp = ""
            if op_choice == "1":
                res = calc_add(a, b)
                exp = f"{a} + {b}"
            elif op_choice == "2":
                res = calc_sub(a, b)
                exp = f"{a} - {b}"
            elif op_choice == "3":
                res = calc_mul(a, b)
                exp = f"{a} × {b}"
            elif op_choice == "4":
                res = calc_div(a, b)
                exp = f"{a} ÷ {b}"
            elif op_choice == "5":
                res = calc_mod(a, b)
                exp = f"{a} % {b}"
            elif op_choice == "6":
                res = calc_pow(a, b)
                exp = f"{a} ^ {b}"
            else:
                print("无效选项，请重新输入！")
                continue
            print(f"计算结果：{res:.2f}")
            save_calc_log(exp, res)
        except ValueError:
            print("输入错误！请输入有效数字")
        except ZeroDivisionError as err:
            print("运算失败：", err)
        except Exception as err:
            print("程序异常：", err)

if __name__ == "__main__":
    calculator_main()
