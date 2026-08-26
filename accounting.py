types =[] #收入，支出
amounts =[] # 存金额
notes= [] # 类别，备注

print ("======命令行记账 v1========")
print ("命令: add/list/balance/total/exit")

while True:
    cmd = input('> ')

    if cmd=="add":
        t=input('(1收入/2支出)')
        if t!="1" and t!="2":
            print ('输入错误：只能为1或2')
            continue
        money =input('金额：')
        category =input('类别：(如交通/餐饮/工资)：')
        remark =input('备注：')
        if t =='1':
           types.append('收入')
        else :
            types.append('支出')
        amounts.append(float(money))
        notes.append(category +"/"+remark)
        print(f"已记录第{len(amounts)}笔。")

    elif cmd =="balance":
        balance=0
        for i in range(len(amounts)):
            if types[i] == "收入":
                balance +=amounts[i]
            else :
                balance -=amounts[i]
        print (f'当前余额:{balance:.2f}')

    elif cmd=="list":
        for i in range (len(amounts)):
            if types[i]=="收入":
                print(f"+{amounts[i]:.2f}")
            else :
                print(f"-{amounts[i]:.2f}")
        print ( f"共 {len(amounts)} 笔记录")


    elif cmd =="total" :
        total_in=0
        total_out =0
        for i in range(len(amounts)):
            if types=="收入":
                total_in +=amounts[i]
            else :
                total_out +=amounts[i]
        print ( f"总收入: {total_in:.2f} | 总支出: {total_out:.2f}")

    elif cmd == "exit":
        print("再见！")
        break
    else:
        print("未知命令，重新输入。")

