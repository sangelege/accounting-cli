import json
import os 

DATA_FILE = "records.json"

def load_records():
    if not os.path.exists(DATA_FILE):
        return[]
    try:
        with open (DATA_FILE, "r", encoding ="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("[警告] 数据文件损坏，从空记录开始。")
        return[]


def save_records(records):
    with open(DATA_FILE, "w",encoding ="utf-8") as f:
        json.dump(records,f,ensure_ascii=False,indent =2)

def parse_amount(text):
    try :
        amount = float(text)
        if amount>0:
            return amount
        else:
            print ("金额错误")
    except (ValueError):
        print("输入数字错误")
    return None


def add_record(records):
    while True:
        rtype = input("类型（收入/支出）：").strip()
        if rtype=="收入" or rtype=="支出":
            break
        print("类型不存在")

    while True:
        amount =parse_amount(input("输入金额：")) 
        if amount >0:
            break

    note =input("输入备注：")

    records.append({"type": rtype, "amount": amount, "note": note})


def show_records(records):
    if len(records)==0:
        print ("还没有记录，先add一笔")
    else:
        for i in range(len(records)):
            print("序号"   "类型"  "金额"  "备注")
            print(i+1,records[i]["rtype"],records[i]["amount"],records[i]["note"])

def show_summary(records):
    in_sum=0
    out_sum=0

    for i in range(len(records)):
        if records[i].rtype=="收入":
            in_sum+=records[i].amount
        else:
            out_sum+=records[i].amount
    print("总收入：" ,in_sum)
    print("总支出：" ,out_sum)
    print("结余： " ,in_sum-out_sum)


def main():
   
    records = load_records()
    print("=== 记账程序 v2 ===")
    while True:
        print("\n命令: add | list | summary | exit")
        cmd = input("> ").strip().lower()
        if cmd == "add":
            add_record(records)
        elif cmd == "list":
            show_records(records)
        elif cmd == "summary":
            show_summary(records)
        elif cmd == "exit":
            save_records(records)
            print(f"已保存 {len(records)} 条记录，再见。")
            break
        else:
            print("未知命令。")


if __name__ == "__main__":
    main()
