from flask import Flask , render_template ,request
import pickle
app  = Flask(__name__)
model = pickle.load(open('decisiontreeclassifier.pkl','rb'))
@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/login', methods = ["POST"])
def login():
    ap= request.form["ap"]
    if(ap== "good"):
        ap1,ap2,ap3 = 1,0,0
    if(ap== "moderate"):
        ap1,ap2,ap3 = 0,1,0
    if(ap== "poor"):
        ap1,ap2,ap3 = 0,0,1
    ag = request.form["ag"]
    bp = request.form["bp"]
    sg = request.form["sg"]
    al = request.form["al"]
    su = request.form["su"]
    rbc = request.form["rbc"]
    pc = request.form["pc"]
    pcc = request.form["pcc"]
    b = request.form["b"]
    bgr = request.form["bgr"]
    bu = request.form["bu"]
    sc = request.form["sc"]
    so = request.form["so"]
    po = request.form["po"]
    he = request.form["he"]
    pcv = request.form["pcv"]
    wbcc = request.form["wbcc"]
    rbcc = request.form["rbcc"]
    hy = request.form["hy"]
    pe = request.form["pe"]
    an = request.form["an"]
    total = [[ap1,ap2,ap3,int(ag),int(bp),float(sg),int(al),int(su),int(rbc),int(pc),int(pcc),int(b),int(bgr),int(bu),float(sc),int(so),float(po),float(he),int(pcv),int(wbcc),float(rbcc),int(hy),int(pe),int(an)]]
    q = model.predict(total)
    print(q)
    if(q[0]==0):
        mesg="negative"
    if(q[0]==1):
        mesg="positive"
    return render_template('index.html',label="The result is:"+str(mesg))
if __name__=='__main__':
    app.run(debug = True)