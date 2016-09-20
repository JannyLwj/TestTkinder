# coding=utf-8
import subprocess

# 帮助信息
HELP = '''\
输入 ?/h/H 打印当前帮助
输入 q/quit/exit 退出日记本
输入 r/read 读取所有日记内容
'''

# 将用户输入数据传进server
def postdata(data):
    # curl localhost:4000/write --silent --data input_md=hello > /dev/null
    command = ['curl','localhost:4000/write', '--silent', '--data','input_md={}'.format(data), '>', '/dev/null']
    subprocess.call('curl localhost:4000/write --silent --data input_md="{}" > /dev/null'.format(data), shell=True)

# 从服务器读取聊天数据数据
def readdiary():
    return subprocess.check_output('curl -s localhost:4000/read_raw', shell=True)

if __name__ == '__main__':
    print(HELP)
    while True:
        data = input("该写点啥呢\n> ")
        if data in ['h', 'H', '?']:
            print(HELP)
        elif data in ['q', 'quit', 'exit']:
            print("bye, 亲~")
            break
        elif data in ['r', 'read']:
            print(readdiary())
        else:
            postdata(data)
