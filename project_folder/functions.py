import pandas as pd
import numpy as np
import joblib
import  io
import yfinance as yf
import matplotlib.pyplot as plt
import os
import seaborn as sns
import re
import io

# def menu_setting():
#     print(
#     """
#     =================MENU================
#     --------- 1 company profile ---------
#     --------- 2 financial numbers -------
#     --------- 3 financial report --------
#     --------- 4 visualization -----------
#     --------- 5 prediction --------------
#     --------- 6 exit --------------------
#     =====================================

#     Please select the info you need
#     Key in the number in menu
#     """
#     )


# def get_users_command():
#     while True:
#         menu_setting()
#         command_raw = input("please type in number of function:")
#         try:
#             command_raw = int(command_raw)
#             if command_raw in [1,2,3,4,5,6]:
#                 return command_raw
#             else:
#                 1/0
#         except:
#             print("please type in correct number")



# def get_company_selection():
#     # get user's command, input company; deal with upper,lower and 
#     # problem, need to make the df_1 a default data 
#     ticker_list = ['AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ADBE', 'ADI', 'ADM',
#        'ADS', 'ADSK', 'AEE', 'AEP', 'AFL', 'AIG', 'AIV', 'AIZ', 'AJG',
#        'AKAM', 'ALB', 'ALK', 'ALL', 'ALLE', 'ALXN', 'AMAT', 'AME', 'AMG',
#        'AMGN', 'AMP', 'AMT', 'AMZN', 'AN', 'ANTM', 'AON', 'APA', 'APC',
#        'APD', 'APH', 'ARNC', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP',
#        'AYI', 'AZO', 'BA', 'BAC', 'BAX', 'BBBY', 'BBT', 'BBY', 'BCR',
#        'BDX', 'BHI', 'BIIB', 'BK', 'BLL', 'BMY', 'BSX', 'BWA', 'BXP', 'C',
#        'CAG', 'CAH', 'CAT', 'CB', 'CBG', 'CCI', 'CCL', 'CELG', 'CERN',
#        'CF', 'CFG', 'CHD', 'CHK', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL',
#        'CLX', 'CMA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF',
#        'COG', 'COL', 'COO', 'COST', 'COTY', 'CPB', 'CRM', 'CSCO', 'CSRA',
#        'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVS', 'CVX', 'CXO', 'D',
#        'DAL', 'DD', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS',
#        'DISCA', 'DISCK', 'DLPH', 'DLR', 'DLTR', 'DNB', 'DOV', 'DPS',
#        'DRI', 'DUK', 'DVA', 'DVN', 'EA', 'EBAY', 'ECL', 'ED', 'EFX',
#        'EIX', 'EL', 'EMN', 'EMR', 'EOG', 'EQIX', 'EQR', 'EQT', 'ES',
#        'ESS', 'ETFC', 'ETN', 'ETR', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR',
#        'F', 'FAST', 'FB', 'FBHS', 'FCX', 'FDX', 'FE', 'FFIV', 'FIS',
#        'FISV', 'FL', 'FLIR', 'FLR', 'FLS', 'FMC', 'FRT', 'FSLR', 'FTR',
#        'GD', 'GGP', 'GILD', 'GIS', 'GLW', 'GM', 'GPC', 'GPN', 'GPS',
#        'GRMN', 'GT', 'GWW', 'HAL', 'HAR', 'HAS', 'HBAN', 'HBI', 'HCA',
#        'HCN', 'HCP', 'HD', 'HES', 'HIG', 'HOG', 'HOLX', 'HON', 'HP',
#        'HPE', 'HPQ', 'HRB', 'HRL', 'HRS', 'HSIC', 'HST', 'HSY', 'HUM',
#        'IBM', 'IDXX', 'IFF', 'ILMN', 'INTC', 'INTU', 'IP', 'IPG', 'IRM',
#        'ISRG', 'ITW', 'IVZ', 'JBHT', 'JEC', 'JNPR', 'JPM', 'JWN', 'K',
#        'KEY', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KORS', 'KR',
#        'KSS', 'KSU', 'LB', 'LEG', 'LEN', 'LH', 'LKQ', 'LLL', 'LLTC',
#        'LLY', 'LMT', 'LNT', 'LOW', 'LRCX', 'LUK', 'LUV', 'LVLT', 'LYB',
#        'M', 'MA', 'MAA', 'MAC', 'MAR', 'MAS', 'MAT', 'MCD', 'MCHP', 'MCK',
#        'MCO', 'MDLZ', 'MET', 'MHK', 'MJN', 'MKC', 'MLM', 'MMC', 'MMM',
#        'MNST', 'MO', 'MON', 'MOS', 'MPC', 'MRK', 'MRO', 'MSFT', 'MTB',
#        'MTD', 'MU', 'MUR', 'MYL', 'NAVI', 'NBL', 'NDAQ', 'NEE', 'NEM',
#        'NFLX', 'NFX', 'NKE', 'NLSN', 'NOV', 'NSC', 'NTAP', 'NTRS', 'NUE',
#        'NVDA', 'NWL', 'NWS', 'NWSA', 'O', 'OKE', 'OMC', 'ORLY', 'OXY',
#        'PAYX', 'PBCT', 'PBI', 'PCAR', 'PCG', 'PCLN', 'PDCO', 'PEG', 'PEP',
#        'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKI', 'PM', 'PNC', 'PNR',
#        'PNW', 'PPG', 'PPL', 'PRU', 'PSX', 'PVH', 'PWR', 'PX', 'PYPL',
#        'QCOM', 'QRVO', 'R', 'RCL', 'REGN', 'RHI', 'RHT', 'RL', 'ROK',
#        'ROP', 'ROST', 'RRC', 'RSG', 'SBUX', 'SCG', 'SCHW', 'SE', 'SEE',
#        'SHW', 'SIG', 'SJM', 'SLG', 'SNA', 'SNI', 'SO', 'SPG', 'SPGI',
#        'SPLS', 'SRCL', 'SRE', 'STI', 'STT', 'STX', 'STZ', 'SWK', 'SWKS',
#        'SWN', 'SYF', 'SYK', 'SYMC', 'SYY', 'T', 'TAP', 'TDC', 'TDG',
#        'TEL', 'TGNA', 'TGT', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TRV',
#        'TSCO', 'TSN', 'TSO', 'TSS', 'TXN', 'TXT', 'UA', 'UAA', 'UAL',
#        'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URBN', 'USB',
#        'UTX', 'V', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSK',
#        'VRSN', 'VRTX', 'VTR', 'VZ', 'WAT', 'WDC', 'WEC', 'WFC', 'WFM',
#        'WHR', 'WLTW', 'WM', 'WMB', 'WMT', 'WRK', 'WU', 'WY', 'WYN',
#        'WYNN', 'XEC', 'XEL', 'XL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL',
#        'YHOO', 'YUM', 'ZBH', 'ZION', 'ZTS']
#     ticker_list = [x.lower() for x in ticker_list]
#     while True:
#         print("============================================================")
#         print("type in ticker to select company, if you want quit, type in 0")
#         print("============================================================")
#         company_label = input("please input the company you want to search:")
#         company_label = company_label.strip().lower()
#         if company_label in ticker_list:
#             return company_label.upper()
#         elif company_label == "0":
#             print("see you~")
#             break
#         elif len([s for s in ticker_list if re.search(company_label, s, re.IGNORECASE)]) > 0:
#             result = [s for s in ticker_list if re.search(company_label, s, re.IGNORECASE)]
#             for n,i in enumerate(result):
#                 print(n,"--",i)
#             print("============= You mean the companies above? ================")
#             print("============ Please key in the correct command =============")
#         else:
#             print("============ Please key in the correct command =============")


def company_profile(company_ticker_name):
    import textwrap
    import yfinance as yf
    
    try:
        company_ob = yf.Ticker(company_ticker_name)
        profile_info = company_ob.info
        wrap_width = 85
        business_summary = "\n".join(textwrap.wrap(profile_info.get("longBusinessSummary", "N/A"), wrap_width))
        
        # 返回字典格式的公司数据
        company_data = {
            "Short Name": profile_info.get("shortName", "N/A"),
            "Long Name": profile_info.get("longName", "N/A"),
            "Country": profile_info.get("country", "N/A"),
            "Website": profile_info.get("website", "N/A"),
            "Industry": profile_info.get("industry", "N/A"),
            "Sector": profile_info.get("sector", "N/A"),
            "Business Summary": business_summary,
            "Full-time Employees": profile_info.get("fullTimeEmployees", "N/A"),
            "Market Cap": profile_info.get("marketCap", "N/A"),
            "Volume": profile_info.get("volume", "N/A"),
            "Previous Close": profile_info.get("previousClose", "N/A"),
            "Current Price": profile_info.get("currentPrice", "N/A"),
            "Open": profile_info.get("open", "N/A"),
            "Day Low": profile_info.get("dayLow", "N/A"),
            "Day High": profile_info.get("dayHigh", "N/A"),
        }
        return company_data
    except Exception as e:
        # 遇到错误时返回一个带错误信息的字典
        return {"Error": f"无法获取公司数据：{str(e)}"}



def get_financial_numbers(company_ticker_name):
    import yfinance as yf

    company_ob = yf.Ticker(company_ticker_name)
    profile_info = company_ob.info

    # 生成第一个表格数据
    table_data1 = [
        ["Short Name", profile_info.get("shortName", "N/A")],
        ["Long Name", profile_info.get("longName", "N/A")],
        ["Market Cap", profile_info.get("marketCap", "N/A")],
        ["Enterprise Value", profile_info.get("enterpriseValue", "N/A")],
        ["Trailing PE", profile_info.get("trailingPE", "N/A")],
        ["Forward PE", profile_info.get("forwardPE", "N/A")],
        ["PEG Ratio", profile_info.get("pegRatio", "N/A")],
        ["Price to Sales Trailing 12 Months", profile_info.get("priceToSalesTrailing12Months", "N/A")],
        ["Price to Book", profile_info.get("priceToBook", "N/A")]
    ]

    # 生成第二个表格数据
    table_data2 = [
        ["Short Name", profile_info.get("shortName", "N/A")],
        ["Long Name", profile_info.get("longName", "N/A")],
        ["Profit Margins", profile_info.get("profitMargins", "N/A")],
        ["Return on Assets", profile_info.get("returnOnAssets", "N/A")],
        ["Return on Equity", profile_info.get("returnOnEquity", "N/A")], 
        ["Total Revenue", profile_info.get("totalRevenue", "N/A")],
        ["Net Income to Common", profile_info.get("netIncomeToCommon", "N/A")],
        ["Trailing EPS", profile_info.get("trailingEps", "N/A")],
        ["Forward EPS", profile_info.get("forwardEps", "N/A")],
        ["Total Debt/Equity", profile_info.get("debtToEquity", "N/A")],
        ["Free Cash Flow", profile_info.get("freeCashflow", "N/A")]
    ]

    # 返回包含两个表格数据的字典
    return {
        "Valuation Measures": table_data1,
        "Financial Highlights": table_data2
    }


"""
market cap
enterprise value
trailing PE
forward PE
PEG ratio
price/Sales
price/book
enterprise value/revenue
enterprise value/EBITDA
"""

"""
profit margin
return on assets
return on equity
revenue
net income avi to common
diluted EPS
total cash
total debt/equity
levered free cash flow
"""

def get_financial_statements(company_name, choice):
    company = yf.Ticker(company_name)

    # 根据选择返回不同的财务报表
    if choice == 1:
        statement = company.balance_sheet
    elif choice == 2:
        statement = company.financials
    elif choice == 3:
        statement = company.cashflow
    else:
        return None  # 错误选择

    # 将 DataFrame 转换为 HTML
    if statement is not None:
        return statement.to_html(classes='table table-bordered')
    else:
        return "<p>该公司没有可用的财务报表数据。</p>"











def plot_data_web(company_name, choice):
    # 下载公司财务数据
    company = yf.Ticker(company_name)
    income_statement = company.financials

    if choice == 1:
        # 获取 Operating Income 和 Net Income
        try:
            operating_income = income_statement.loc['Operating Income']
            net_income = income_statement.loc['Net Income']
        except KeyError:
            print("Operating Income or Net Income not found in the financials.")
            return None

        # 转换为 DataFrame
        pd_operating_income = pd.DataFrame({"Operating Income": operating_income[::-1]})
        pd_net_income = pd.DataFrame({"Net Income": net_income[::-1]})

        # 计算同比增长率
        operating_income_yoy = pd_operating_income.pct_change() * 100
        net_income_yoy = pd_net_income.pct_change() * 100

        # 合并数据
        operating_combined = pd.concat([pd_operating_income, operating_income_yoy.add_suffix('_YoY')], axis=1)
        net_combined = pd.concat([pd_net_income, net_income_yoy.add_suffix('_YoY')], axis=1)

        # 转换索引为日期格式
        operating_combined.index = pd.to_datetime(operating_combined.index)
        net_combined.index = pd.to_datetime(net_combined.index)

        # 图表 1: Operating Income 和同比增长率
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        ax1.bar(operating_combined.index, operating_combined['Operating Income'], color='b', width=50)
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Operating Income (USD)', color='b')
        ax1.tick_params(axis='y', labelcolor='b')
        ax1.set_title('Operating Income and YoY Growth')

        ax2 = ax1.twinx()
        ax2.plot(operating_combined.index, operating_combined['Operating Income_YoY'], color='g', marker='o', label='Operating Income YoY')
        ax2.set_ylabel('YoY Growth (%)', color='g')
        ax2.tick_params(axis='y', labelcolor='g')
        ax2.legend(loc='upper left')

        # 图表 2: Net Income 和同比增长率
        fig2, ax3 = plt.subplots(figsize=(10, 6))
        ax3.bar(net_combined.index, net_combined['Net Income'], color='r', width=50)
        ax3.set_xlabel('Year')
        ax3.set_ylabel('Net Income (USD)', color='r')
        ax3.tick_params(axis='y', labelcolor='r')
        ax3.set_title('Net Income and YoY Growth')

        ax4 = ax3.twinx()
        ax4.plot(net_combined.index, net_combined['Net Income_YoY'], color='purple', marker='o', label='Net Income YoY')
        ax4.set_ylabel('YoY Growth (%)', color='purple')
        ax4.tick_params(axis='y', labelcolor='purple')
        ax4.legend(loc='upper left')
        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()  # 关闭图形
        buffer.seek(0)  # 将指针移动到图像数据的开头
        return buffer

    elif choice == 2:
        # 获取毛利率、净利率和费用率数据
        try:
            gross_profit = income_statement.loc['Gross Profit']
            net_income = income_statement.loc['Net Income']
            revenue = income_statement.loc['Total Revenue']
            selling_expense = income_statement.loc['Selling General And Administration']
            interest_expense = income_statement.loc['Interest Expense']
            total_expense = income_statement.loc['Total Expenses']
        except KeyError:
            print("Required financial data not found in the financials.")
            return None

        # 计算毛利率和净利率
        gross_profit_margin = (gross_profit / revenue) * 100
        net_profit_margin = (net_income / revenue) * 100

        # 计算费用率
        selling_expense_ratio = (selling_expense / revenue) * 100
        interest_expense_ratio = (interest_expense / revenue) * 100
        total_expense_ratio = (total_expense / revenue) * 100

        # 转换为 DataFrame
        profit_ratios = pd.DataFrame({
            'Gross Profit Margin': gross_profit_margin[::-1],
            'Net Profit Margin': net_profit_margin[::-1]
        })
        expense_ratios = pd.DataFrame({
            'Selling Expense Ratio': selling_expense_ratio[::-1],
            'Interest Expense Ratio': interest_expense_ratio[::-1],
            'Total Expense Ratio': total_expense_ratio[::-1]
        })

        # 图表 1: 毛利率和净利率
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        ax1.bar(profit_ratios.index, profit_ratios['Gross Profit Margin'], color='b', width=50)
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Gross Profit Margin (%)', color='b')
        ax1.tick_params(axis='y', labelcolor='b')
        ax1.set_title('Gross Profit Margin and Net Profit Margin')

        ax2 = ax1.twinx()
        ax2.plot(profit_ratios.index, profit_ratios['Net Profit Margin'], color='g', marker='o', label='Net Profit Margin')
        ax2.set_ylabel('Net Profit Margin (%)', color='g')
        ax2.tick_params(axis='y', labelcolor='g')
        ax2.legend(loc='upper left')

        # 图表 2: 费用率
        fig2, ax3 = plt.subplots(figsize=(10, 6))
        ax3.bar(expense_ratios.index, expense_ratios['Selling Expense Ratio'], color='r', width=50, label='Selling Expense Ratio')
        ax3.bar(expense_ratios.index, expense_ratios['Interest Expense Ratio'], color='y', width=30, label='Interest Expense Ratio')
        ax3.bar(expense_ratios.index, expense_ratios['Total Expense Ratio'], color='purple', width=10, label='Total Expense Ratio')
        ax3.set_xlabel('Year')
        ax3.set_ylabel('Expense Ratios (%)')
        ax3.set_title('Expense Ratios')
        ax3.legend()
        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()  # 关闭图形
        buffer.seek(0)  # 将指针移动到图像数据的开头
        return buffer

    else:
        print("Invalid choice. Please choose 1 or 2.")
        return None

    # 展示图表
    plt.tight_layout()
    plt.show()



def plot_data_web_sns(company_name, choice):
    # 设置全局样式
    sns.set_theme(style="whitegrid")
    company = yf.Ticker(company_name)
    income_statement = company.financials

    if choice == 1:
        try:
            # 提取 Operating Income 和 Net Income
            operating_income = income_statement.loc['Operating Income']
            net_income = income_statement.loc['Net Income']
        except KeyError:
            print("Operating Income or Net Income not found in the financials.")
            return None

        # 转换为 DataFrame
        pd_operating_income = pd.DataFrame({"Operating Income": operating_income[::-1]})
        pd_net_income = pd.DataFrame({"Net Income": net_income[::-1]})

        # 计算同比增长率
        operating_income_yoy = pd_operating_income.pct_change() * 100
        net_income_yoy = pd_net_income.pct_change() * 100

        # 合并数据
        operating_combined = pd.concat([pd_operating_income, operating_income_yoy.add_suffix('_YoY')], axis=1)
        net_combined = pd.concat([pd_net_income, net_income_yoy.add_suffix('_YoY')], axis=1)

        # 创建合并图表
        fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

        # 子图 1: Operating Income 和同比增长率
        sns.barplot(x=operating_combined.index.strftime('%Y'),
                    y="Operating Income",
                    data=operating_combined.reset_index(),
                    ax=axs[0], color="skyblue", label="Operating Income")
        sns.lineplot(x=operating_combined.index.strftime('%Y'),
                     y="Operating Income_YoY",
                     data=operating_combined.reset_index(),
                     ax=axs[0].twinx(), color="green", marker="o", label="YoY Growth")
        axs[0].set_title("Operating Income and YoY Growth", fontsize=16)
        axs[0].set_ylabel("Operating Income (USD)", fontsize=12)
        axs[0].legend(loc="upper left")

        # 子图 2: Net Income 和同比增长率
        sns.barplot(x=net_combined.index.strftime('%Y'),
                    y="Net Income",
                    data=net_combined.reset_index(),
                    ax=axs[1], color="lightcoral", label="Net Income")
        sns.lineplot(x=net_combined.index.strftime('%Y'),
                     y="Net Income_YoY",
                     data=net_combined.reset_index(),
                     ax=axs[1].twinx(), color="purple", marker="o", label="YoY Growth")
        axs[1].set_title("Net Income and YoY Growth", fontsize=16)
        axs[1].set_xlabel("Year", fontsize=12)
        axs[1].set_ylabel("Net Income (USD)", fontsize=12)
        axs[1].legend(loc="upper left")

        plt.tight_layout()

        # 将图保存到 buffer 中
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png", dpi=100)
        plt.close(fig)  # 关闭图形，释放内存
        buffer.seek(0)
        return buffer

    elif choice == 2:
        try:
            # 提取数据
            gross_profit = income_statement.loc['Gross Profit']
            net_income = income_statement.loc['Net Income']
            revenue = income_statement.loc['Total Revenue']
            selling_expense = income_statement.loc['Selling General And Administration']
            interest_expense = income_statement.loc['Interest Expense']
            total_expense = income_statement.loc['Total Expenses']
        except KeyError:
            print("Required financial data not found in the financials.")
            return None

        # 计算毛利率和净利率
        gross_profit_margin = (gross_profit / revenue) * 100
        net_profit_margin = (net_income / revenue) * 100

        # 计算费用率
        selling_expense_ratio = (selling_expense / revenue) * 100
        interest_expense_ratio = (interest_expense / revenue) * 100
        total_expense_ratio = (total_expense / revenue) * 100

        # 转换为 DataFrame
        ratios = pd.DataFrame({
            'Gross Profit Margin': gross_profit_margin[::-1],
            'Net Profit Margin': net_profit_margin[::-1],
            'Selling Expense Ratio': selling_expense_ratio[::-1],
            'Interest Expense Ratio': interest_expense_ratio[::-1],
            'Total Expense Ratio': total_expense_ratio[::-1],
        })

        # 创建合并图表
        fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

        # 子图 1: 毛利率和净利率
        sns.barplot(x=ratios.index.strftime('%Y'),
                    y="Gross Profit Margin",
                    data=ratios.reset_index(),
                    ax=axs[0], color="blue", label="Gross Profit Margin")
        sns.lineplot(x=ratios.index.strftime('%Y'),
                     y="Net Profit Margin",
                     data=ratios.reset_index(),
                     ax=axs[0].twinx(), color="green", marker="o", label="Net Profit Margin")
        axs[0].set_title("Profit Margins Over Years", fontsize=16)
        axs[0].set_ylabel("Profit Margins (%)", fontsize=12)
        axs[0].legend(loc="upper left")

        # 子图 2: 各费用率
        sns.barplot(x=ratios.index.strftime('%Y'),
                    y="Selling Expense Ratio",
                    data=ratios.reset_index(),
                    ax=axs[1], color="lightcoral", label="Selling Expense Ratio")
        sns.lineplot(x=ratios.index.strftime('%Y'),
                     y="Total Expense Ratio",
                     data=ratios.reset_index(),
                     ax=axs[1].twinx(), color="purple", marker="o", label="Total Expense Ratio")
        axs[1].set_title("Expense Ratios Over Years", fontsize=16)
        axs[1].set_xlabel("Year", fontsize=12)
        axs[1].set_ylabel("Expense Ratios (%)", fontsize=12)
        axs[1].legend(loc="upper left")

        plt.tight_layout()

        # 将图保存到 buffer 中
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png", dpi=100)
        plt.close(fig)  # 关闭图形，释放内存
        buffer.seek(0)
        return buffer

    else:
        print("Invalid choice. Please choose 1 or 2.")
        return None





def plot_income_data_web(company_name):
    # 下载公司信息
    company = yf.Ticker(company_name)

    # 获取利润表
    income_statement = company.financials

    # 获取 Operating Income 和 Net Income
    try:
        operating_income = income_statement.loc['Operating Income']
        net_income = income_statement.loc['Net Income']
    except KeyError:
        return None  # 如果数据不完整，返回 None

    # 转换为 DataFrame 以便计算同比增长率
    pd_operating_income = pd.DataFrame({"Operating Income": operating_income}).iloc[::-1]
    pd_net_income = pd.DataFrame({"Net Income": net_income}).iloc[::-1]

    # 计算同比增长率
    operating_income_yoy = pd_operating_income.pct_change() * 100
    net_income_yoy = pd_net_income.pct_change() * 100

    # 合并数据
    net_combined = pd.concat([pd_net_income, net_income_yoy.add_suffix('_YoY')], axis=1)
    operating_combined = pd.concat([pd_operating_income, operating_income_yoy.add_suffix('_YoY')], axis=1)

    net_combined.index = pd.to_datetime(net_combined.index)
    operating_combined.index = pd.to_datetime(operating_combined.index)

    # 创建图表
    fig, axes = plt.subplots(2, 1, figsize=(10, 12))

    # 图表 1：Operating Income 和同比增长率
    ax1 = axes[0]
    ax1.bar(operating_combined.index, operating_combined['Operating Income'], color='b', width=50)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Operating Income (USD)', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.set_title('Operating Income and YoY Growth')
    ax2 = ax1.twinx()
    ax2.plot(operating_combined.index, operating_combined['Operating Income_YoY'], color='g', marker='o',
             label='Operating Income YoY')
    ax2.set_ylabel('YoY Growth (%)', color='g')
    ax2.tick_params(axis='y', labelcolor='g')
    ax2.legend(loc='upper left')

    # 图表 2：Net Income 和同比增长率
    ax3 = axes[1]
    ax3.bar(net_combined.index, net_combined['Net Income'], color='r', width=50)
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Net Income (USD)', color='r')
    ax3.tick_params(axis='y', labelcolor='r')
    ax3.set_title('Net Income and YoY Growth')
    ax4 = ax3.twinx()
    ax4.plot(net_combined.index, net_combined['Net Income_YoY'], color='purple', marker='o', label='Net Income YoY')
    ax4.set_ylabel('YoY Growth (%)', color='purple')
    ax4.tick_params(axis='y', labelcolor='purple')
    ax4.legend(loc='upper left')

    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()  # 关闭图形
    buffer.seek(0)  # 将指针移动到图像数据的开头
    return buffer




def plot_income_data(company_name):
    # 下载公司信息
    company = yf.Ticker(company_name)
    
    # 获取利润表
    income_statement = company.financials
    
    # 获取 Operating Income 和 Net Income
    try:
        operating_income = income_statement.loc['Operating Income']
        net_income = income_statement.loc['Net Income']
    except KeyError:
        print("Operating Income or Net Income not found in the financials.")
        return None
    # 转换为 DataFrame 以便计算同比增长率
    pd_operating_income = pd.DataFrame({
        "Operating Income": operating_income
    })
    pd_net_income = pd.DataFrame({
        "Net Income": net_income
    })
    
    pd_net_income=pd_net_income[::-1]
    pd_operating_income=pd_operating_income[::-1]

    print(pd_operating_income)
    
    # 计算同比增长率（使用 pct_change 计算百分比变化）
    operating_income_yoy = pd_operating_income.pct_change() * 100  # 同比增长率（百分比）
    net_income_yoy = pd_net_income.pct_change() * 100  # 同比增长率（百分比）

    # 合并两个 DataFrame
    net_combined = pd.concat([pd_net_income, net_income_yoy.add_suffix('_YoY')], axis=1)
    operating_combined = pd.concat([pd_operating_income, operating_income_yoy.add_suffix('_YoY')], axis=1)

    net_combined.index=pd.to_datetime(net_combined.index)
    operating_combined.index=pd.to_datetime(operating_combined.index)
    
    # 创建图表 1：Operating Income 和同比增长率
    fig1, ax1 = plt.subplots(figsize=(10, 6))

    # 绘制柱状图：Operating Income
    ax1.bar(operating_combined.index, operating_combined['Operating Income'], color='b', width=50)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Operating Income (USD)', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.set_title('Operating Income and YoY Growth')

    # 创建第二个y轴，并绘制折线图：同比增长率
    ax2 = ax1.twinx()
    ax2.plot(operating_combined.index, operating_combined['Operating Income_YoY'], color='g', marker='o', label='Operating Income YoY')
    ax2.set_ylabel('YoY Growth (%)', color='g')
    ax2.tick_params(axis='y', labelcolor='g')

    # 添加图例
    ax2.legend(loc='upper left')

    # 创建图表 2：Net Income 和同比增长率
    fig2, ax3 = plt.subplots(figsize=(10, 6))

    # 绘制柱状图：Net Income
    ax3.bar(net_combined.index, net_combined['Net Income'], color='r', width=50)
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Net Income (USD)', color='r')
    ax3.tick_params(axis='y', labelcolor='r')
    ax3.set_title('Net Income and YoY Growth')

    # 创建第二个y轴，并绘制折线图：同比增长率
    ax4 = ax3.twinx()
    ax4.plot(net_combined.index, net_combined['Net Income_YoY'], color='purple', marker='o', label='Net Income YoY')
    ax4.set_ylabel('YoY Growth (%)', color='purple')
    ax4.tick_params(axis='y', labelcolor='purple')

    # 添加图例
    ax4.legend(loc='upper left')

    # 展示图表
    plt.tight_layout()
    plt.show()



def get_profitability_and_expense_ratios(company_name):
    # 获取公司对象
    company = yf.Ticker(company_name)
    
    # 获取利润表
    income_statement = company.financials
    print(income_statement)
   
    
    # 获取 Gross Profit, Net Income 和 Revenue
    try:
        gross_profit = income_statement.loc['Gross Profit']
        net_income = income_statement.loc['Net Income']
        revenue = income_statement.loc['Total Revenue']
    except KeyError:
        print("Required financial data not found in the financials.")
        return None

    # 获取四个费用类目：销售费用、管理费用、利息费用、研发费用
    try:
        selling_expense = income_statement.loc['Selling General And Administration']
        interest_expense = income_statement.loc['Interest Expense']
        total_expense = income_statement.loc['Total Expenses']
    except KeyError:
        print("Expense categories not found.")
        return None

    # 计算销售毛利率和销售净利率
    gross_profit_margin = (gross_profit / revenue) * 100
    net_profit_margin = (net_income / revenue) * 100

    # 计算四个费用率（费用/收入）
    selling_expense_ratio = (selling_expense / revenue) * 100
    interest_expense_ratio = (interest_expense / revenue) * 100
    total_expense_ratio = (total_expense / revenue) * 100

    # 创建两个 DataFrame，分别存储毛利率、净利率和四个费用率
    profit_ratios = pd.DataFrame({
        'Gross Profit Margin': gross_profit_margin,
        'Net Profit Margin': net_profit_margin
    })
    
    expense_ratios = pd.DataFrame({
        'Selling Expense Ratio': selling_expense_ratio,
        'Interest Expense Ratio': interest_expense_ratio,
        'Total Expense Ratio': total_expense_ratio
    })

    # 反转数据顺序
    profit_ratios = profit_ratios[::-1]
    expense_ratios = expense_ratios[::-1]

    # 生成第一张图：销售毛利率和销售净利率
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.bar(profit_ratios.index, profit_ratios['Gross Profit Margin'], color='b', width=50)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Gross Profit Margin (%)', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.set_title('Gross Profit Margin and Net Profit Margin')

    ax2 = ax1.twinx()
    ax2.plot(profit_ratios.index, profit_ratios['Net Profit Margin'], color='g', marker='o', label='Net Profit Margin')
    ax2.set_ylabel('Net Profit Margin (%)', color='g')
    ax2.tick_params(axis='y', labelcolor='g')

    ax2.legend(loc='upper left')

    # 生成第二张图：四个费用率
    fig2, ax3 = plt.subplots(figsize=(10, 6))
    ax3.bar(expense_ratios.index, expense_ratios['Selling Expense Ratio'], color='r', width=50, label='Selling Expense Ratio')
    ax3.bar(expense_ratios.index, expense_ratios['Interest Expense Ratio'], color='y', width=30, label='Interest Expense Ratio')
    ax3.bar(expense_ratios.index, expense_ratios['Total Expense Ratio'], color='purple', width=10, label='Total Expense Ratio')

    ax3.set_xlabel('Year')
    ax3.set_ylabel('Expense Ratios (%)')
    ax3.set_title('Expense Ratios')

    ax3.legend()

    plt.tight_layout()
    plt.show()


#visualization的功能函数
def part4_mian(company_name):
    choice=int(input("Type 1 for income information\nType 2 for expense information"))
    if choice ==1:
        plot_income_data(company_name)
    elif choice==2:
        get_profitability_and_expense_ratios(company_name)


def calculate_beta_and_financials(ticker_list, start_date, end_date,num,Year):
    global selected_bs,selected_cf
    results = []
    
    for ticker in ticker_list:
        
        stock = yf.download(ticker, start=start_date, end=end_date)
        market = yf.download('^GSPC', start=start_date, end=end_date)

        
        stock['Returns'] = stock['Adj Close'].pct_change().dropna()
        market['Returns'] = market['Adj Close'].pct_change().dropna()

        
        returns_data = pd.DataFrame({
            'Stock Returns': stock['Returns'],
            'Market Returns': market['Returns']
        }).dropna()
        try:
        
            returns_data['Year'] = returns_data.index.year

            beta_by_year = {}

            for year in returns_data['Year'].unique():
                yearly_data = returns_data[returns_data['Year'] == year]
                cov_matrix = np.cov(yearly_data['Stock Returns'], yearly_data['Market Returns'])
                cov_stock_market = cov_matrix[0, 1]
                market_var = cov_matrix[1, 1]
                beta = cov_stock_market / market_var
                beta_by_year[year] = beta
        
            
            stock_info = yf.Ticker(ticker)

            balance_sheet = stock_info.balancesheet
            selected_bs = balance_sheet.loc[['Current Assets', 'Cash And Cash Equivalents', 'Current Liabilities', 'Total Liabilities Net Minority Interest']]

            
            cash_flow = stock_info.cashflow
            selected_cf = cash_flow.loc[['Depreciation And Amortization', 'Capital Expenditure']]
            
            
            income_stmt = stock_info.incomestmt
            selected_is = income_stmt.loc[['Net Income', 'Interest Expense', 'Tax Rate For Calcs']]    

            result = {
                'Ticker': ticker,
                'Year' : year,
                'Beta': beta_by_year[Year],
                'Current Assets': selected_bs.loc['Current Assets'].values[num],
                'Cash And Cash Equivalents': selected_bs.loc['Cash And Cash Equivalents'].values[num],
                'Current Liabilities': selected_bs.loc['Current Liabilities'].values[num],
                'Total Liabilities Net Minority Interest': selected_bs.loc['Total Liabilities Net Minority Interest'].values[num],
                'Depreciation And Amortization': selected_cf.loc['Depreciation And Amortization'].values[num],
                'Capital Expenditure': selected_cf.loc['Capital Expenditure'].values[num],
                'Net Income': selected_is.loc['Net Income'].values[num],
                'Interest Expense': selected_is.loc['Interest Expense'].values[num],
                'Tax Rate For Calcs': selected_is.loc['Tax Rate For Calcs'].values[num]
            }


            results.append(result)
        except:
            pass

    
    results_df = pd.DataFrame(results)
    results_df["Year"] = Year
    return results_df
    # results_df.to_csv(output_csv, index=False)
    # print(f'Results saved to {output_csv}')



def get_profile_number(column_list,company_list):   
    profile_info_dict = {}
    for company in company_list:
        try:
            ticker = yf.Ticker(company)
            ticker_info = ticker.info
            ticker_info_selected = {}
            for key in column_list:
                try:
                    value = ticker_info[key]
                    ticker_info_selected[key] = value
                except:
                    ticker_info_selected[key] = ""
            # ticker_info_selected["company"] = company
            profile_info_dict[company] = ticker_info_selected
        except:
            pass
        # profile_info_df = profile_info_df.append(profile_info_dict)
    profile_info_df = pd.DataFrame(profile_info_dict)
    return profile_info_df


def recommendation_exiting_company(company):
    ticker_list = [company]
    (a,b) = (0,2023)
    start_date = '2020-09-29'
    end_date = '2023-10-01'
    Financial_data=calculate_beta_and_financials(ticker_list, start_date, end_date, a,b)
    

    # get macroecomonical data
    df_macro = pd.read_excel("./economic_indicators_last_4_years.xlsx",sheet_name = "Sheet1")
    df_macro = df_macro.rename(columns={"Unnamed: 0":"date"})
    df_macro.drop(["Reserve Ratio"],axis=1,inplace=True)
    df_macro = df_macro.loc[df_macro["date"]!="2024-09-01",:]
    df_macro["date"] = [str(x)[:4] for x in df_macro.date]
    df_macro = df_macro.rename(columns={"date":"Year"})

    # 

    column_list = ["country","industry","sector","fullTimeEmployees",'exchange','quoteType']

    profile_info = get_profile_number(column_list,ticker_list)
    profile_df = profile_info.drop_duplicates().T
    # profile_df = profile_df.rename(columns={"Unnamed: 0":"Ticker"})
    profile_df = profile_df.reset_index()
    profile_df = profile_df.rename(columns={"index":"Ticker"})


    Financial_data['Year'] = Financial_data['Year'].astype(int)
    df_macro["Year"] = df_macro["Year"].astype(int)
    input_data = Financial_data.merge(profile_df).merge(df_macro)

    input_data.drop(["sector","exchange","quoteType"],axis=1,inplace=True)
    input_data = input_data.reset_index()
    
    with open("./X_variable_list.txt",'r') as f:
        contents = f.read()

    contents = eval(contents)

    result_industry = [s for s in contents if s.startswith("industry_")]
    industry_dummy = pd.DataFrame(np.zeros((1, len(result_industry))))
    industry_dummy.columns = result_industry

    industry_dummy = industry_dummy.reset_index()
    input_data = input_data.merge(industry_dummy)

    result_country = [s for s in contents if s.startswith("country_")]
    country_dummy = pd.DataFrame(np.zeros((1, len(result_country))))
    country_dummy.columns = result_country

    country_dummy = country_dummy.reset_index()
    input_data = input_data.merge(country_dummy)


    # find category and 0 -> 1
    category_industry = "industry_" + input_data.industry.values[0]
    input_data[category_industry] = 1

    country_industry = "country_" + input_data.country.values[0]
    input_data[country_industry] = 1

    input_data.set_index("Ticker")
    input_data = input_data.drop(["index","industry","country","Ticker"],axis=1)
    input_data.Year = input_data.Year-2020
    
    # load data 
    rf_loaded = joblib.load('./random_forest_model_evaluation.joblib')
    
    y_predict = rf_loaded.predict(input_data)
    return y_predict


"""
let user type in the information one by one and then give out a prediction
"""
def check_input_asint(columns):
    while True:
        command = input("Please type in {}:".format(columns))
        if command=='a':
            print("see you next time~")
            break
        else:
            try:
                command = int(command)
                return command
            except:
                print("please type in number:")


def mannual_data_keyin():
    global df_raw
    print("You need to provide some key information of this company")
    print("Tips: if you want to quit, please type 'a'")
    print("Please type in numbers following instruction:")
    content_list = ['Beta', 'Current Assets', 'Cash And Cash Equivalents', 'Current Liabilities', 
        'Total Liabilities Net Minority Interest', 'Depreciation And Amortization', 'Capital Expenditure',
        'Net Income', 'Interest Expense', 'Tax Rate For Calcs', 'fullTimeEmployees']
    content_dict={}
    for column in content_list:
        output_unit = check_input_asint(column)
        content_dict[column] = output_unit
    with open("./X_variable_list.txt",'r') as f:
        contents = f.read()
    contents = eval(contents)
    df_raw = pd.DataFrame(np.zeros((1, len(contents))))
    df_raw.columns = contents
    country_info = input("Please type in country:")
    industry_info = input("Please type in industry:")


    category_industry = "industry_" + industry_info
    df_raw[category_industry] = 1

    country_industry = "country_" + country_info
    df_raw[country_industry] = 1
    content_list_no_onehot = ['Beta', 'Current Assets', 'Cash And Cash Equivalents', 'Current Liabilities', 
        'Total Liabilities Net Minority Interest', 'Depreciation And Amortization', 'Capital Expenditure',
        'Net Income', 'Interest Expense', 'Tax Rate For Calcs', 'fullTimeEmployees']
    for i in content_list_no_onehot:
        df_raw[i] = content_dict[i]
    
    macro_dict = {
        "CPI":307.531,
        "PPI":255.192,
        "Unemployment Rate":3.8,
        "Federal Funds Rate":5.33,
        "Inflation Rate":4.116338,
        "Overnight Lending Rate":5.33,
        "10 Year Treasury Rate":4.59
        }
    for j in macro_dict.keys():
        df_raw[j] = macro_dict[j]
    df_raw["Year"] = 0
    # df_raw.drop(["Ticker"],axis=1,inplace=True)
    rf_loaded = joblib.load('./random_forest_model_evaluation.joblib')
    y_predict = rf_loaded.predict(df_raw)

    return y_predict
    


def menu_function5(company):
    while True:
        choice = input("Type 1 for company recommendation evaluation\nType2 to type in data and get a evaluation\nType3 to exit")
        try:
            choice = int(choice)
            if choice == 1:
                evaluation = recommendation_exiting_company(company)
                evaluation = format(float(evaluation[0]), 'f')
                print("Recommended evaluation for {} is {} \nGenerated by AI, DYOR".format(company,evaluation))
                break
            elif choice == 2:
                evaluation = mannual_data_keyin()
                evaluation = format(float(evaluation[0]), 'f')
                print("Recommended evaluation is {} \nGenerated by AI, DYOR".format(evaluation))
                break
            elif choice == 3:
                print("see you the next time~")
                break

        except:
            print("please key in correct command in [1,2,3]")




def ranking(company):
    df = pd.read_csv("../data/new_financial.csv")
    # Check if the company exists in the DataFrame
    if company not in df['Company'].values:
        return f"Company {company} not found."
    
    ticker_data = df[df['Company'] == company].iloc[0]
    
    # Get the sector and industry for the ticker
    sector = ticker_data['sector']
    industry = ticker_data['industry']
    
    # Filter the DataFrame by the same sector and industry
    sector_data = df[df['sector'] == sector]
    industry_data = df[df['industry'] == industry]
    
    # Convert relevant columns to numeric (coerce errors)
    columns_to_check = [
        'marketCap', 'beta', 'trailingPE', 'forwardPE', 'profitMargins',
        'grossMargins', 'operatingMargins', 'debtToEquity', 'currentRatio',
        'quickRatio', 'freeCashflow', 'totalRevenue', 'netIncomeToCommon',
        'trailingEps', 'forwardEps', 'dividendYield', 'returnOnAssets',
        'returnOnEquity', 'enterpriseValue'
    ]
    
    # Convert columns to numeric and coerce errors to NaN
    for column in columns_to_check:

        sector_data.loc[:, column] = pd.to_numeric(sector_data[column], errors='coerce')
        industry_data.loc[:, column] = pd.to_numeric(industry_data[column], errors='coerce')

    # Ranking for each column of interest
    ranking_data = {}
    for column in columns_to_check:
        # Ranking in sector
        sector_rank = (sector_data[column] >= ticker_data[column]).sum()
        sector_total = sector_data[column].count()
        sector_info = f"({sector_rank}/{sector_total})" if sector_rank != 0 else '(NA)'
        
        # Ranking in industry
        industry_rank = (industry_data[column] >= ticker_data[column]).sum()
        industry_total = industry_data[column].count()
        industry_info = f"({industry_rank}/{industry_total})"if industry_rank != 0 else '(NA)'
        
        # Store the results in the dictionary
        ranking_data[column] = (ticker_data[column], sector_info, industry_info)
    
    # Create a ranking DataFrame
    ranking_df = pd.DataFrame.from_dict(ranking_data, orient='index', columns=['Value', 'Rank in Sector', 'Rank in Industry'])
    ranking_df['Sector'] = sector
    ranking_df['Industry'] = industry

    return ranking_df[['Value', 'Sector', 'Rank in Sector', 'Industry', 'Rank in Industry']]



def get_financial_data(ticker):

    import yfinance as yf
    import pandas as pd

    """获取财务数据"""
    stock = yf.Ticker(ticker)
    
    try:
        # 获取财务报表数据
        balance_sheet = stock.balance_sheet
        cash_flow = stock.cashflow
        income_statement = stock.financials

        current_assets = balance_sheet.loc['Total Assets'].values[0]
        current_liabilities = balance_sheet.loc['Total Debt'].values[0]
        cash_and_equivalents = balance_sheet.loc['Cash And Cash Equivalents'].values[0]
        net_income = income_statement.loc['Net Income'].values[0]
        
        # 提取自由现金流 (Free Cash Flow)
        fcf = cash_flow.loc['Free Cash Flow'].values[0] if 'Free Cash Flow' in cash_flow.index else None
        
        return {
            'ticker': ticker,
            'current_assets': current_assets,
            'current_liabilities': current_liabilities,
            'cash_and_equivalents': cash_and_equivalents,
            'net_income': net_income,
            'free_cash_flow': fcf
        }
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def calculate_fcf_valuation(ticker):
    """计算自由现金流估值"""
    financial_data = get_financial_data(ticker)
    
    if financial_data is None:
        return
    
    # 用户输入增长率和折现率
    growth_rate = float(input("请输入预计年增长率（如0.05表示5%）："))
    discount_rate = float(input("请输入贴现率（如0.10表示10%）："))
    years = int(input("请输入预测几年（例如5）："))
    
    # 估算未来的现金流
    fcf = financial_data['free_cash_flow'] if financial_data['free_cash_flow'] is not None else financial_data['net_income']
    
    if fcf is None:
        print("无法计算FCF，金融数据未完整。")
        return

    print(f"当前自由现金流为: {fcf}")
    
    # 计算未来的自由现金流
    future_cash_flows = []
    for year in range(1, years + 1):
        future_cash_flow = fcf * ((1 + growth_rate) ** year)
        future_cash_flows.append(future_cash_flow)
        print(f"预计第{year}年的现金流: {future_cash_flow}")

    # 折现未来现金流
    present_value = sum([cf / ((1 + discount_rate) ** year) for year, cf in enumerate(future_cash_flows, start=1)])
    terminal_value = future_cash_flows[-1] * (1 + growth_rate) / (discount_rate - growth_rate)
    present_terminal_value = terminal_value / ((1 + discount_rate) ** years)
    
    total_valuation = present_value + present_terminal_value
    return total_valuation

    # print(f"{ticker} 的自由现金流估值结果: {total_valuation:.2f}")

# 示例用法
# ticker = input("请输入股票代码（如 'AAPL'）：")
# calculate_fcf_valuation(ticker)


#def dcf_model(ticker):
    # 获取财务数据
    stock = yf.Ticker(ticker)
    
    # 获取自由现金流
    cash_flow = stock.cashflow
    if 'Free Cash Flow' in cash_flow.index:
        fcf = cash_flow.loc['Free Cash Flow'][0]
    else:
        fcf = None
    
    # 获取收入（Revenue）
    income_statement = stock.financials
    if 'Total Revenue' in income_statement.index:
        revenue = income_statement.loc['Total Revenue'][0]
    else:
        revenue = None

    # 获取其他重要信息
    info = stock.info
    last_price = info.get('currentPrice', None)

    # 输出财务数据
    print(f"Ticker: {ticker}")
    print(f"Free Cash Flow: {fcf}")
    print(f"Revenue: {revenue}")
    print(f"Current Price: {last_price}")
    
    # 输入用户提供的其他数据
    if fcf is None:
        print("无法获取自由现金流，请手动输入：")
        fcf = float(input("输入未来5年的自由现金流（以第1年为基准）: "))

    growth_rate = float(input("输入预计的年增长率（例如：0.05表示5%）："))
    discount_rate = float(input("输入折现率（例如：0.1表示10%）："))
    terminal_growth_rate = float(input("输入终值增长率（例如：0.02表示2%）："))

    # 计算未来现金流（假设5年）
    cash_flows = [(fcf * ((1 + growth_rate) ** i)) for i in range(1, 6)]
    
    # 计算折现现金流
    discounted_cash_flows = [cf / ((1 + discount_rate) ** i) for i, cf in enumerate(cash_flows, start=1)]
    
    # 计算终值
    terminal_value = cash_flows[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
    discounted_terminal_value = terminal_value / ((1 + discount_rate) ** 5)
    
    # 估值计算
    total_valuation = sum(discounted_cash_flows) + discounted_terminal_value
    
    # 输出估值结果
    print(f"估算的企业总价值: ${total_valuation:,.2f}")
    if last_price is not None:
        # print(f"每股价值预估: ${total_valuation / info.get('sharesOutstanding', 1):,.2f}")
        return round(total_valuation / info.get('sharesOutstanding', 1))
    else:
        return None
        print("当前股价未知，无法计算每股价值。")
def dcf_model(company_name, growth_rate, discount_rate, terminal_growth_rate):
    import yfinance as yf
    print(f"Running DCF Model with {ticker}, {growth_rate}, {discount_rate}, {terminal_growth_rate}")
    # 模型逻辑...

    # 获取财务数据
    stock = yf.Ticker(company_name)
    cash_flow = stock.cashflow
    fcf = cash_flow.loc['Free Cash Flow'][0] if 'Free Cash Flow' in cash_flow.index else 1_000_000

    # 计算未来现金流
    cash_flows = [(fcf * ((1 + growth_rate) ** i)) for i in range(1, 6)]
    discounted_cash_flows = [cf / ((1 + discount_rate) ** i) for i, cf in enumerate(cash_flows, start=1)]
    
    # 计算终值和总估值
    terminal_value = cash_flows[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
    discounted_terminal_value = terminal_value / ((1 + discount_rate) ** 5)
    total_valuation = sum(discounted_cash_flows) + discounted_terminal_value

    return round(total_valuation, 2)




def chat_with_gpt():
    '''
    description: 
        this function call openai api to make users able to interact with chatgpt within this website

    parameters:
        None
    
    output:
        print the response from chat-gpt

    '''
    client = OpenAI(
    api_key="API-KEY",
    )
    conversation = [{"role": "system", "content": "You are a helpful assistant."}]
    while True:
        try:
            user_input = input("you:")
            conversation.append({"role": "user", "content": user_input})
            chat_completion = client.chat.completions.create(
                messages=conversation,
                model="gpt-4o-mini",
                        )
            print("You:", user_input)
            assistant_reply = chat_completion.choices[0].message.content
            conversation.append({"role": "assistant", "content": assistant_reply})
            print("ChatGPT: ", assistant_reply)
            print("\n")
            print("\n")

        except TimeoutError:
            print("error")




def find_data(Ticker):
    """
    这是一个根据用户输入的Ticker，返回该公司对应的数据
    input:
        Ticker(str):公司名称

    output:
        pd.Series:根据Ticker返回对应的行数据
        str:如果Ticker没有找到则返回提示信息

    """
    try:
        df_standardized = pd.read_csv("./data/data_preprocessed.csv", index_col="Ticker")
        result = df_standardized.loc[Ticker]
        result = pd.DataFrame(result).T
        return result
    except KeyError:
        return f"Ticker '{Ticker}' not found in the DataFrame."
    



def regression_prediction(input_data):
    """
    这是一个调用已保存randomforest模型，根据已在数据库中数据（含3年历史市值）来预测精确市值的函数。
    
    Input：已经预处理完毕的Xvariables数据；dataframe格式
    Output：根据提供数据预测的市值结果；array格式
    
    
    """
    try:
        model = joblib.load('random_forest_model_evaluation_t-3_stand.joblib')
        
        if not isinstance(input_data, pd.DataFrame):
            raise ValueError("Please enter the data in pandas DataFrame format.")
        
        prediction = model.predict(input_data)
        return prediction
    except:
        return f"error"




def predict_inlist(Ticker):
    """
    这是一个输入Ticker，如果Ticker在datalist中就返回精确预测值，如果不在datalist中就返回提示信息：Ticker不在datalist中。

    input：
        Ticker(str):公司名称

    output：
        如果在list中，返回根据提供数据预测的市值结果；array格式
        如果不在list中，返回提示信息；str格式
    """
    
    input_data = find_data(Ticker)
    if not isinstance(input_data, pd.DataFrame):
        return f"Ticker '{Ticker}' not found in the list."
    
    else: 
        return regression_prediction(input_data)
    



