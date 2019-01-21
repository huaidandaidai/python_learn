"""
    作者：lsh
    版本：v5.0
    日期：2019-01-11
    功能：判断密码强度
        2.0新增功能;循环跳出
        3.0新增功能：将密码强度和密码保存到文件中
        4.0新增功能：读取文件中的密码
        5.0新增功能：定义一个password工具类
"""


class PasswordTool:
    """
        密码工具类
    """
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def process_password(self):
        # 规则1：密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print("密码长度要求至少8位！")

        # 规则2：包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print("密码要求包含数字！")

        # 规则3：包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print("密码要求包含字母！")

    def check_number_exist(self):
        """
            判断字符串中是否含有数字
        """
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        """
            判断字符串中是否含有字母
        """
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter


def main():
    """
        主函数
    """
    try_time = 5

    while try_time > 0:
        password = input("请输入密码：")
        # 实例化对象
        password_tool = PasswordTool(password)
        password_tool.process_password()

        f = open('password_3.0.txt', 'a')
        f.write('密码:{},强度：{}\n'.format(password, password_tool.strength_level))
        f.close()

        if password_tool.strength_level == 3:
            print("恭喜！密码合格！")
            break
        else:
            print("密码不合格！")
            try_time -= 1

    if try_time == 0:
        print("尝试次数过多，密码设置失败！")


if __name__ == '__main__':
    main()