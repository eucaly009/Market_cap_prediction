from flask import Flask, render_template, request, redirect, url_for
from functions import *
from openai import OpenAI





app = Flask(__name__)

@app.route('/')
def choose_language():
    return render_template('language_yjl.html')

@app.route('/zh',methods=["POST","GET"]) #简体中文
def zh_index():
# '''
#     client = OpenAI()



#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": "tell me a joke"
#             }
#         ]
#     )

# '''



    generated_text = "暂停使用gpt"


    return render_template('ch_index.html',text=generated_text)



@app.route('/en',methods=["POST","GET"]) #简体中文
def en_index():
# '''
#     client = OpenAI()



#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": "tell me a joke"
#             }
#         ]
#     )

# '''



    generated_text = "暂停使用gpt"


    return render_template('en_index.html',text=generated_text)




@app.route('/zh/company', methods=['POST'])
def company():
    try:


        company_name = request.form['company_name']
        function_num = int(request.form['function_num'])
        
        # 根据不同的功能号调用相应函数并返回结果
        if function_num == 1:
            result_data = company_profile(company_name)
            result_type = 'simple'  # 简单字典
            
        elif function_num == 2:
            result_data = get_financial_numbers(company_name)
            result_type = 'nested'  # 嵌套字典
            
        elif function_num == 3:
            statement_choice = int(request.form['statement_choice'])
            result_data = get_financial_statements(company_name, statement_choice)
            result_type = 'html_table'  # HTML 表格

        else:
            return "无效的功能编号"
        
        return render_template('result.html', company=company_name, result_data=result_data, result_type=result_type)

    except Exception as e:
        return render_template('error.html', error_message=str(e))


@app.route('/zh/financial_statements', methods=['GET', 'POST'])
def financial_statements():
    if request.method == 'POST':
        company_name = request.form['company_name']
        choice = int(request.form['statement_choice'])

        # 调用 get_financial_statements 函数获取相应的财务报表
        result_data = get_financial_statements(company_name, choice)

        # 将 HTML 表格数据传递给模板
        return render_template('result.html', company=company_name, result_data=result_data)

    return render_template('financial_statements.html')





if __name__ == '__main__':
    app.run(debug=True)
