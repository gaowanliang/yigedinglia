from flask import Flask, render_template, request
from cyjl import yigedinglia, cyfd
import requests
app = Flask(__name__)


@app.route("/ygdl", methods=['GET'])
def ygdls():
    if request.args.get('search') != None:
        yzm = request.args.get('recaptcha')
        datas = {
            'secret': "****",
            'response': yzm
        }
        k = requests.post(
            "https://recaptcha.net/recaptcha/api/siteverify", data=datas)
        kk = eval(k.text.replace('"', "'").replace(
            'true', "1").replace('false', "2"))
        if kk["success"] == 1:
            p = yigedinglia(request.args.get('search'))
            try:
                p['ls']
            except:
                return render_template("index10.html", ygdlia=p['title'], disa="456")
            else:
                cyy = p['ls']
                pyy = p['tk']
                szz = range(p['num'])
                step = range(p['step'])
                return render_template("index10.html", ygdlia=p['title'], disa="123" if p['step'] != 0 else "456", indexs=szz, cy=cyy, py=pyy, bu=step)

        else:
            return render_template("index10.html", ygdlia="服务器开小差了，请尝试重新查询或更换其他浏览器", disa="456")
    return render_template("index10.html", disa="456")


@app.route("/fudu", methods=['GET'])
def fuducy():
    if request.args.get('search') != None:
        yzm = request.args.get('recaptcha')
        datas = {
            'secret': "****",
            'response': yzm
        }
        k = requests.post(
            "https://recaptcha.net/recaptcha/api/siteverify", data=datas)
        kk = eval(k.text.replace('"', "'").replace(
            'true', "1").replace('false', "2"))
        if kk["success"] == 1:
            p = cyfd(request.args.get('search'))
            # print(p)
            try:
                p['ls']
            except:
                return render_template("index9.html", ygdlia=p['title'], disa="456")
            else:
                cyy = p['ls']
                pyy = p['tk']
                szz = range(p['num'])
                step = range(p['step'])
                #print(p['ls'], p['tk'],)
                return render_template("index9.html", ygdlia=p['title'], disa="123" if p['step'] != 0 else "456", indexs=szz, cy=cyy, py=pyy, bu=step)

        else:
            return render_template("index9.html", ygdlia="服务器开小差了，请尝试重新查询或更换其他浏览器", disa="456")
    return render_template("index9.html", disa="456")


if __name__ == '__main__':
    # 设置debug=True是为了让代码修改实时生效，而不用每次重启加载
    app.run(host='0.0.0.0', port=8000, debug=True)
