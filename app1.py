# import the flask module 
from flask import Flask, render_template,request
from flask_mysqldb import MySQL,MySQLdb
# from flaskext.mysql import MySQL

app = Flask(__name__)
# app.secret_key = "secret key"


# Add MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'stud_db'

mysql = MySQL(app)
# mysql.init_app(app)

# Mention the default route 
@app.route("/")
def test():
    return render_template('index.html')
 
# Admin Login 
@app.route("/admin",methods=['GET','POST'])
def adminlog():
    if request.method=='GET':
        return render_template('adminlog.html')

    if request.method=='POST':
        user=request.form['user']
        pwd=request.form['pwd']

        if(user=="admin" and pwd=="admin"):
            print("Login Success !!! ")
            return render_template('adminmenu.html')
        else:
            return render_template('adminlog.html')    
        
# Admin Login 
@app.route("/studlogin",methods=['GET','POST'])
def studlog():
    if request.method=='GET':
        return render_template('studlog.html')

    if request.method=='POST':
        user=request.form['user']
        pwd=request.form['pwd']

        print(user , ' : ' , pwd)

        try :

            sqlstr = '''select *from student_master where RegNo=%s and Emailid=%s'''
            print(sqlstr)   
            # mysql = MySQL(app)
            cursor = mysql.connection.cursor()
            cursor.execute(sqlstr,(user,pwd))
            
            cursor.close()
            msg = ""
            if cursor.rowcount == 0 :
                msg = 0 
            else :
                msg = 1  
        
        except Exception as ex:
            print (ex)
        if msg==1:
            return render_template('studmenu.html',studreg=user)
        else:
            return " <h2> Invalid User Id or Password </h2>  "

# View Student Profile
@app.route("/studprofile")
def viewstudprofile():
    if request.method=='GET':
        regno=request.args.get("regno")
        print(regno)
        try :
            query_string = """select * from student_master where RegNo = %s"""

            print(query_string)   
            cursor = mysql.connection.cursor()
            # cursor = mysql.connection.cursor()

            cursor.execute(query_string,(str(regno),))
            subdata = cursor.fetchone()
            # mysql.connection.commit()
            cursor.close()
            
        except Exception as ex:
            print (ex)
        
        return render_template('viewstudprofile.html',studdata=subdata)

# View Student Marks
@app.route("/studmarks")
def viewstudmarks():
    print(' data : ' , request.get_data())
    if request.method=='GET':
        regno=request.args.get("regno")
        sem=request.args.get("sem")
        print(regno,  ' semester : ' , sem )
        try :
            query_string = """select * from marks_master where RegNo = %s and Semester = %s"""

            print(query_string)   
            cursor = mysql.connection.cursor()
            # cursor = mysql.connection.cursor()

            cursor.execute(query_string,(str(regno),str(sem),))
            subdata = cursor.fetchall()
            # mysql.connection.commit()
            cursor.close()
            
        except Exception as ex:
            print (ex)
        
        return render_template('viewstudmarks.html',markdata=subdata)

# Student Registration 
@app.route("/studreg")
def sturegister():
    if request.method=='GET':
        return render_template('studreg.html')

# Subject Entry Form 
@app.route("/subreg")
def subjectregister():
    if request.method=='GET':
        return render_template('subreg.html')

# Subject Mark Insert 
@app.route("/subregsuc",methods=['POST'] )
def subinsertsuc():
    print("Entered Subject Insert Part !!!")
    if request.method=='POST':
        subcode = request.form['subcode']
        subname = request.form['subname']
        credits = request.form['credits']
        semester = request.form['semester']
        semcode = request.form['semcode']

        # print(regno, " " , name1 , " " , fname, " " ,city ," " ,city , " " ,phone ," " ,emailid  )
        
        try :

            sqlstr = '''insert into subject_master(subcode,subname,credits,semester,semcode) values(%s,%s,%s,%s,%s)'''
            print(sqlstr)   
            # mysql = MySQL(app)
            cursor = mysql.connection.cursor()
            cursor.execute(sqlstr,(subcode,subname,credits,semester,semcode))
            mysql.connection.commit()
            subid = cursor.lastrowid
            print(subid)
            cursor.close()
            
        except Exception as ex:
            print (ex)
        return render_template('subregsuc.html',subid=subid)


# Student Mark Entry 
@app.route("/markreg")
def stumarkregister():
    if request.method=='GET':
        try :
            sqlstr = "select * from subject_master"
            print(sqlstr)   
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            # cursor = mysql.connection.cursor()

            cursor.execute(sqlstr)
            subdata = cursor.fetchall()
            mysql.connection.commit()
            cursor.close()
            # print(" Records Count : " , cursor.rowcount)
            # print(subdata)
        except Exception as ex:
            print (ex)
        
        return render_template('markreg.html',subdata=subdata)

# Check if the student exists  
def checkstudent(regno):
    try :
        sqlstr = "select * from student_master where regno=%s"
        print(sqlstr)   
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor = mysql.connection.cursor()

        cursor.execute(sqlstr,(regno,))
        subdata = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        print("STUDENT AVAIL", cursor.rowcount )
        if cursor.rowcount == 0 :
            return 0
        else :
            return 1 
    
    except Exception as ex:
        print (ex)

# Check whether the subject code grade is already present for the regno and return
def checkifpresent(regno="",subcode=""):
    print(regno , " : : ",subcode )
    try :
        # sqlstr=""
        # sqlstr = "select * from marks_master where RegNo = '" + str(regno) + "' and Subcode = '" + str(subcode) + "'"
        query_string = """select * from marks_master where RegNo = %s and Subcode = %s"""

        print(query_string)   
        cursor = mysql.connection.cursor()
        # cursor = mysql.connection.cursor()

        cursor.execute(query_string,(str(regno),str(subcode),))
        subdata = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        
        if cursor.rowcount == 0 :
            return 0
        else :
            return 1 
    
    except Exception as ex:
        print (ex)
    


# Get credit by passing subject code         
def getcredit(subcode):
    try :
        sqlstr = "select * from subject_master where subcode  like '" + subcode + "'"
        print(sqlstr)   
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor = mysql.connection.cursor()

        cursor.execute(sqlstr)
        subdata = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        print(subdata)
        if cursor.rowcount == 0 :
            return 0
        else :
            return subdata
    
    except Exception as ex:
        print (ex)


# GPA calculation for each semester         
def calcgpa(regno,semester):
    try :
        sqlstr = "select * from marks_master where regno  = %s and semester = %s " 
        print(sqlstr)   
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor = mysql.connection.cursor()

        cursor.execute(sqlstr,(regno,semester,))
        subdata = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        print(subdata)
        if cursor.rowcount == 0 :
            return 0
        else :
            # Iterate and calculate the GPA 
            credit_sum = 0 
            mul_gpa = 0
            for data in subdata:
                print ( data['Credit'] , " : " , data['Grade'], " : ", data['GradePoint'])
                if data['Grade'] != "RA":
                    mul_gpa += ( int(data['Credit']) * int(data['GradePoint']) )
                    credit_sum += int(data['Credit'])
            
            print(credit_sum)
            print(mul_gpa)
            gpa = round(mul_gpa/credit_sum,2)
            result = {"semester":semester,"gpa":gpa, "credit_sum": credit_sum } 
            return result
    
    except Exception as ex:
        print (ex)


# Student View GPA
@app.route("/studcalcugpa",methods=['GET','POST'])
def viewstudgpa():
    if request.method=='GET':
        regno = request.args.get('regno')
        print(regno)
        semester=1
        totres=[]
        for i in range(1,9):
            semester = i
            res = calcgpa(regno,semester)
            if res :
                totres.append(res)
        print(totres)
        # Calculate CGPA
        semgpa=0
        sumofcredit=0
        for d in totres:
            print (d['credit_sum'])
            semgpa += d['gpa'] * d['credit_sum']
            sumofcredit += d['credit_sum']
        cgpa = round(semgpa/sumofcredit , 2)
        
        cgpares={"cgpa",cgpa}
        totres.append(cgpares)
        print("CGPA",cgpa)
        print(totres)
        return render_template('viewstudgpa.html',res=totres,cgpa=cgpa,regno=regno)

# View GPA
@app.route("/calcugpa",methods=['GET','POST'])
def viewgpa():
    if request.method=='GET':
        return render_template('viewgpa.html',res=0)
    if request.method=='POST':
        regno = request.form['regno']
        print(regno)
        semester=1
        totres=[]
        for i in range(1,9):
            semester = i
            res = calcgpa(regno,semester)
            if res :
                totres.append(res)
        print(totres)
        # Calculate CGPA
        semgpa=0
        sumofcredit=0
        for d in totres:
            print (d['credit_sum'])
            semgpa += d['gpa'] * d['credit_sum']
            sumofcredit += d['credit_sum']
        cgpa = round(semgpa/sumofcredit , 2)
        
        cgpares={"cgpa",cgpa}
        totres.append(cgpares)
        print("CGPA",cgpa)
        print(totres)
        return render_template('viewallgpa.html',res=totres,cgpa=cgpa)
 

# Student Mark Insert 
@app.route("/markinsertsuc",methods=['POST'] )
def markregistersuc():
    print("Entered Mark Insert Part !!!")
    if request.method=='POST':
        regno = request.form['regno']
        subcode = request.form['subcode']
        grade = request.form['grade']


        # Check if student is available or not 
        stud_avail = checkstudent(regno)
        print("CHECKSTUDENT" ,stud_avail)
        if stud_avail == 0 :
            return "<h1> No Such Student </h1>"
        else :
            # return "<h1> Student Available </h1>"
            # print(regno, " " , name1 , " " , fname, " " ,city ," " ,city , " " ,phone ," " ,emailid  )

            #Get Grade  
            if grade.startswith("A"):
                grades="A"
                points=9
                result="Pass"
            if grade.startswith("E"):
                grades="EX"
                points=10
                result="Pass"
            if grade.startswith("B"):
                grades="B"
                points=8
                result="Pass"
            if grade.startswith("C"):
                grades="C"
                points=7
                result="Pass"
            if grade.startswith("D"):
                grades="D"
                points=6
                result="Pass"
            if grade.startswith("R"):
                grades="RA"
                points=0
                result="Fail"
            
            #Get Credit
            subdata = getcredit(subcode)
            print(subdata)
            subdata= list(subdata)
            print(subdata)
            subname = subdata[0]['subname']
            print(subname)
            credit  = subdata[0]['credits'] 
            semester = subdata[0]['semester']
            semcode = subdata[0]['semcode']
            print(credit)
            print(semester)
            print(semcode)
            print(grade)
            print(points)
            # return "1" 
            # Check if the record is already present for the regno and subcode 
            alreadyavail = checkifpresent(regno,subcode)
            print("Already Avail :" ,alreadyavail)
        try :
            if alreadyavail == 0 :
                sqlstr = '''insert into marks_master(RegNo,Semester,Subcode,SubName,Credit,Grade,GradePoint,Result) values(%s,%s,%s,%s,%s,%s,%s,%s)'''
                cursor = mysql.connection.cursor()
                cursor.execute(sqlstr,(regno,semester,subcode,subname,credit,grade,points,result))
            if alreadyavail == 1 :
                sqlstr = """update marks_master set Grade= %s,Credit=%s,GradePoint=%s,Result=%s where Regno= %s and Subcode = %s """
                cursor = mysql.connection.cursor()
                cursor.execute(sqlstr,(grade,credit,points,result,regno,subcode))
            print(sqlstr)   
            # mysql = MySQL(app)
            
            mysql.connection.commit()
            studid = cursor.lastrowid
            print(studid)
            cursor.close()
            
        except Exception as ex:
            print (ex)
        return render_template('markregsuc.html',markid=studid)

     
# Student Registration Insert 
@app.route("/studregsuc",methods=['POST'] )
def sturegistersuc():
    print("Entered Insert Part !!!")
    if request.method=='POST':
        regno = request.form['regno']
        name1= request.form['name1']
        course= request.form['course']
        fname= request.form['fname']
        city = request.form['city']
        phone = request.form['phone']
        emailid = request.form['emailid']

        print(regno, " " , name1 , " " , fname, " " ,city ," " ,city , " " ,phone ," " ,emailid  )
        
        try :

            sqlstr = '''insert into student_master(RegNo,StudentName,Course,FatherName,City,Phone,EmailId) values(%s,%s,%s,%s,%s,%s,%s)'''
            print(sqlstr)   
            # mysql = MySQL(app)
            cursor = mysql.connection.cursor()
            cursor.execute(sqlstr,(regno,name1,course,fname,city,phone,emailid))
            mysql.connection.commit()
            studid = cursor.lastrowid
            print(studid)
            cursor.close()
            
        except Exception as ex:
            print (ex)
        return render_template('studregsuc.html',studid=studid)

# View All Subjects  
@app.route("/viewallsubs")
def viewallsubs():

    try :

        sqlstr = "select * from subject_master"
        print(sqlstr)   
        cursor = mysql.connection.cursor()
        # cursor = mysql.connection.cursor()tu

        cursor.execute(sqlstr)
        studdata = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        print(" Records Count : " , cursor.rowcount)
        print(studdata)
    except Exception as ex:
        print (ex)

    return render_template('viewallsubs.html',mydata=studdata)

# View All Students  
@app.route("/viewallstuds")
def viewallstuds():
    try :
        sqlstr = "select * from student_master"
        print(sqlstr)   
        cursor = mysql.connection.cursor()
        # cursor = mysql.connection.cursor()

        cursor.execute(sqlstr)
        studdata = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        print(" Records Count : " , cursor.rowcount)
        print(studdata)
    except Exception as ex:
        print (ex)

    return render_template('viewallstuds.html',mydata=studdata)
  
@app.route("/home")
def myhome():
    return render_template('homepage.html')

@app.route("/products")
def prod():
    return "<h2> ALL PRODUCTS </h2>"

@app.route("/contact")
def contact():
    return "<h2> CONTACTS </h2>"

@app.route("/listall")
def listall():
    return "<h2> LIST ALL PRODS </h2>"


if __name__ == "__main__":
    app.run(debug=True)    