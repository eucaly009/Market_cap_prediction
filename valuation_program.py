import pandas as pd
import numpy as np
import joblib
import yfinance as yf
import matplotlib.pyplot as plt
import os
import seaborn as sns


def menu_setting():
    print(
    """
    =================MENU================
    --------- 1 company profile ---------
    --------- 2 financial numbers -------
    --------- 3 financial report --------
    --------- 4 visualization -----------
    --------- 5 prediction --------------
    --------- 6 exit --------------------
    =====================================

    Please select the info you need
    Key in the number in menu
    """
    )

def get_users_command():
    while True:
        menu_setting()
        command_raw = input("please type in number of function:")
        try:
            command_raw = int(command_raw)
            if command_raw in [1,2,3,4,5,6]:
                return command_raw
            else:
                1/0
        except:
            print("please type in correct number")

# get user's command, input company; deal with upper,lower and 
def get_company_selection():
    # problem, need to make the df_1 a default data 
    ticker_list = ['AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ADBE', 'ADI', 'ADM',
       'ADS', 'ADSK', 'AEE', 'AEP', 'AFL', 'AIG', 'AIV', 'AIZ', 'AJG',
       'AKAM', 'ALB', 'ALK', 'ALL', 'ALLE', 'ALXN', 'AMAT', 'AME', 'AMG',
       'AMGN', 'AMP', 'AMT', 'AMZN', 'AN', 'ANTM', 'AON', 'APA', 'APC',
       'APD', 'APH', 'ARNC', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AWK', 'AXP',
       'AYI', 'AZO', 'BA', 'BAC', 'BAX', 'BBBY', 'BBT', 'BBY', 'BCR',
       'BDX', 'BHI', 'BIIB', 'BK', 'BLL', 'BMY', 'BSX', 'BWA', 'BXP', 'C',
       'CAG', 'CAH', 'CAT', 'CB', 'CBG', 'CCI', 'CCL', 'CELG', 'CERN',
       'CF', 'CFG', 'CHD', 'CHK', 'CHRW', 'CHTR', 'CI', 'CINF', 'CL',
       'CLX', 'CMA', 'CME', 'CMG', 'CMI', 'CMS', 'CNC', 'CNP', 'COF',
       'COG', 'COL', 'COO', 'COST', 'COTY', 'CPB', 'CRM', 'CSCO', 'CSRA',
       'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVS', 'CVX', 'CXO', 'D',
       'DAL', 'DD', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS',
       'DISCA', 'DISCK', 'DLPH', 'DLR', 'DLTR', 'DNB', 'DOV', 'DPS',
       'DRI', 'DUK', 'DVA', 'DVN', 'EA', 'EBAY', 'ECL', 'ED', 'EFX',
       'EIX', 'EL', 'EMN', 'EMR', 'EOG', 'EQIX', 'EQR', 'EQT', 'ES',
       'ESS', 'ETFC', 'ETN', 'ETR', 'EW', 'EXC', 'EXPD', 'EXPE', 'EXR',
       'F', 'FAST', 'FB', 'FBHS', 'FCX', 'FDX', 'FE', 'FFIV', 'FIS',
       'FISV', 'FL', 'FLIR', 'FLR', 'FLS', 'FMC', 'FRT', 'FSLR', 'FTR',
       'GD', 'GGP', 'GILD', 'GIS', 'GLW', 'GM', 'GPC', 'GPN', 'GPS',
       'GRMN', 'GT', 'GWW', 'HAL', 'HAR', 'HAS', 'HBAN', 'HBI', 'HCA',
       'HCN', 'HCP', 'HD', 'HES', 'HIG', 'HOG', 'HOLX', 'HON', 'HP',
       'HPE', 'HPQ', 'HRB', 'HRL', 'HRS', 'HSIC', 'HST', 'HSY', 'HUM',
       'IBM', 'IDXX', 'IFF', 'ILMN', 'INTC', 'INTU', 'IP', 'IPG', 'IRM',
       'ISRG', 'ITW', 'IVZ', 'JBHT', 'JEC', 'JNPR', 'JPM', 'JWN', 'K',
       'KEY', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KORS', 'KR',
       'KSS', 'KSU', 'LB', 'LEG', 'LEN', 'LH', 'LKQ', 'LLL', 'LLTC',
       'LLY', 'LMT', 'LNT', 'LOW', 'LRCX', 'LUK', 'LUV', 'LVLT', 'LYB',
       'M', 'MA', 'MAA', 'MAC', 'MAR', 'MAS', 'MAT', 'MCD', 'MCHP', 'MCK',
       'MCO', 'MDLZ', 'MET', 'MHK', 'MJN', 'MKC', 'MLM', 'MMC', 'MMM',
       'MNST', 'MO', 'MON', 'MOS', 'MPC', 'MRK', 'MRO', 'MSFT', 'MTB',
       'MTD', 'MU', 'MUR', 'MYL', 'NAVI', 'NBL', 'NDAQ', 'NEE', 'NEM',
       'NFLX', 'NFX', 'NKE', 'NLSN', 'NOV', 'NSC', 'NTAP', 'NTRS', 'NUE',
       'NVDA', 'NWL', 'NWS', 'NWSA', 'O', 'OKE', 'OMC', 'ORLY', 'OXY',
       'PAYX', 'PBCT', 'PBI', 'PCAR', 'PCG', 'PCLN', 'PDCO', 'PEG', 'PEP',
       'PFE', 'PFG', 'PG', 'PGR', 'PH', 'PHM', 'PKI', 'PM', 'PNC', 'PNR',
       'PNW', 'PPG', 'PPL', 'PRU', 'PSX', 'PVH', 'PWR', 'PX', 'PYPL',
       'QCOM', 'QRVO', 'R', 'RCL', 'REGN', 'RHI', 'RHT', 'RL', 'ROK',
       'ROP', 'ROST', 'RRC', 'RSG', 'SBUX', 'SCG', 'SCHW', 'SE', 'SEE',
       'SHW', 'SIG', 'SJM', 'SLG', 'SNA', 'SNI', 'SO', 'SPG', 'SPGI',
       'SPLS', 'SRCL', 'SRE', 'STI', 'STT', 'STX', 'STZ', 'SWK', 'SWKS',
       'SWN', 'SYF', 'SYK', 'SYMC', 'SYY', 'T', 'TAP', 'TDC', 'TDG',
       'TEL', 'TGNA', 'TGT', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TRV',
       'TSCO', 'TSN', 'TSO', 'TSS', 'TXN', 'TXT', 'UA', 'UAA', 'UAL',
       'UDR', 'UHS', 'ULTA', 'UNH', 'UNM', 'UNP', 'UPS', 'URBN', 'USB',
       'UTX', 'V', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSK',
       'VRSN', 'VRTX', 'VTR', 'VZ', 'WAT', 'WDC', 'WEC', 'WFC', 'WFM',
       'WHR', 'WLTW', 'WM', 'WMB', 'WMT', 'WRK', 'WU', 'WY', 'WYN',
       'WYNN', 'XEC', 'XEL', 'XL', 'XLNX', 'XOM', 'XRAY', 'XRX', 'XYL',
       'YHOO', 'YUM', 'ZBH', 'ZION', 'ZTS']
    ticker_list = [x.lower() for x in ticker_list]
    while True:
        print("============================================================")
        print("type in ticker to select company, if you want quit, type in 0")
        print("============================================================")
        company_label = input("please input the company you want to search:")
        company_label = company_label.strip().lower()
        if company_label in ticker_list:
            return company_label.upper()
        elif company_label == "0":
            print("see you~")
            break
        elif len([s for s in ticker_list if re.search(company_label, s, re.IGNORECASE)]) > 0:
            result = [s for s in ticker_list if re.search(company_label, s, re.IGNORECASE)]
            for n,i in enumerate(result):
                print(n,"--",i)
            print("============= You mean the companies above? ================")
            print("============ Please key in the correct command =============")
        else:
            print("============ Please key in the correct command =============")

def company_profile(company_ticker_name):
    from tabulate import tabulate
    import textwrap
    company_ob = yf.Ticker(company_ticker_name)
    profile_info = company_ob.info
    wrap_width = 85
    business_summary = long_business_summary = "\n".join(textwrap.wrap(profile_info["longBusinessSummary"], wrap_width))
    table_data = [
    ["Short Name", profile_info["shortName"]],
    ["Long Name", profile_info["longName"]],
    ["Country", profile_info["country"]],
    ["Website", profile_info["website"]],
    ["Industry", profile_info["industry"]],
    ["Sector", profile_info["sector"]],
    ["Business Summary", business_summary],
    ["Full-time Employees", profile_info["fullTimeEmployees"]],
    ["Market Cap", profile_info["marketCap"]],
    ["Volume", profile_info["volume"]],
    ["Previous Close", profile_info["previousClose"]],
    ["currentPrice", profile_info["currentPrice"]],
    ["Open", profile_info["open"]],
    ["Day Low", profile_info["dayLow"]],
    ["Day High", profile_info["dayHigh"]]
    # ["Company Officers", profile_info["companyOfficers"]]
]
    print(tabulate(table_data, headers=["Attribute", "Value"], tablefmt="grid"))

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

def get_financial_numbers(company_ticker_name):
    from tabulate import tabulate
    company_ob = yf.Ticker(company_ticker_name)
    profile_info = company_ob.info
    table_data1 = [
    ["Short Name", profile_info["shortName"]],
    ["Long Name", profile_info["longName"]],
    ["Market Cap", profile_info["marketCap"]],
    ["enterprise Value", profile_info["enterpriseValue"]],
    ["trailing PE", profile_info["trailingPE"]],
    ["forward PE", profile_info["forwardPE"]],
    ["peg Ratio", profile_info["pegRatio"]],
    ["price To Sales Trailing12Months", profile_info["priceToSalesTrailing12Months"]],
    ["price To Book", profile_info["priceToBook"]]
    ]
    table_data2 = [
    ["Short Name", profile_info["shortName"]],
    ["Long Name", profile_info["longName"]],
    ["profit Margins", profile_info["profitMargins"]],
    ["return On Assets", profile_info["returnOnAssets"]],
    ["return On Equity", profile_info["returnOnEquity"]], 
    ["total Revenue", profile_info["totalRevenue"]],
    ["net IncomeToCommon", profile_info["netIncomeToCommon"]],
    ["trailing Eps", profile_info["trailingEps"]],
    ["forward Eps", profile_info["forwardEps"]],
    ["total Debt/Equity", profile_info["debtToEquity"]],
    ["free Cashflow", profile_info["freeCashflow"]]
    ]

    print(tabulate(table_data1, headers=["Valuation Measures", "Value"], tablefmt="grid"))
    print("====================================================")
    print(tabulate(table_data2, headers=["Financial Highlights", "Value"], tablefmt="grid"))

import yfinance as yf

def get_financial_statements(company_name):
    
    company = yf.Ticker(company_name)
    
    print(f"""
    type 1 for balance sheet for {company_name}
    type 2 for income statement for {company_name}
    type 3 for cashflow statement for {company_name}
    """)
    balance_sheet = company.balance_sheet
    income_statement = company.financials
    cashflow_statement = company.cashflow
    choice=int(input("Enter your choice"))
    
    if choice == 1:
        balance_sheet = company.balance_sheet
        print(f"Balance Sheet for {company_name}:")
        print(balance_sheet)
        return balance_sheet
    elif choice == 2:
        income_statement = company.financials
        print(f"Income Statement for {company_name}:")
        print(income_statement)
        return income_statement
    elif choice == 3:
        cashflow_statement = company.cashflow
        print(f"Cashflow Statement for {company_name}:")
        print(cashflow_statement)
        return cashflow_statement
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return None

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


"""
step1: 
    use yfinance to get input
step2:
    use sklearn finishing data preprocessing
step3:
    calculate the recommendation data

step4: 
    error tolerant mechanism
"""


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
        # """except Exception as e:
        #     # 输出异常的基本信息
        #     print(f"An error occurred: {e}")"""



def main():
    function_num = get_users_command()
    if function_num == 6:
        print("see you the next time~")
    else:
        company = get_company_selection()
        if company is not None:
            print("\n")
            print("\n")
            if function_num == 1:
                company_profile(company)
            elif function_num == 2:
                get_financial_numbers(company)
            elif function_num == 3:
                get_financial_statements(company)
            elif function_num == 4:
                part4_mian(company)
            elif function_num == 5:
                menu_function5(company)
            else:
                pass
        else:
            pass
    



main()

