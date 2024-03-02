import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="dark")

def create_sales_performance_df(df):
    sales_performance = df.groupby('seller_city')["price"].sum().reset_index()
    sales_performance_sorted = sales_performance.sort_values(by='price', ascending=False)
    
    return sales_performance_sorted

def create_monthly_sales_df(df):
    trend_df = df.copy()
    trend_df['order_purchase_timestamp'] = pd.to_datetime(trend_df['order_purchase_timestamp'])
    trend_df['year_month'] = trend_df['order_purchase_timestamp'].dt.to_period('M')
    monthly_sales = trend_df.groupby('year_month')['price'].sum().reset_index()
    
    return monthly_sales

def create_payment_each_method_df(df):
    payment_each_method = df.copy()
    payment_each_method = payment_each_method.groupby(by="payment_type")["payment_value"].sum().reset_index()
    
    return payment_each_method

def create_total_orders(df):
    total = pd.value_counts(values=df['order_id']).sum()
   
    return total

def create_total_payments(df):
    total = df['payment_value'].sum()

    return "${}".format(total)

def create_total_sellers(df):
    total = df['seller_id'].nunique()

    return total

# Load Data
main_df = pd.read_csv(filepath_or_buffer="https://raw.githubusercontent.com/adigntr/dicoding-dataset/main/E-Commerce%20Public%20Dataset/main_df.csv")

main_df['order_purchase_timestamp'] = pd.to_datetime(main_df['order_purchase_timestamp'])

start_date = main_df['order_purchase_timestamp'].min()
end_date = main_df['order_purchase_timestamp'].max()

# Header
st.header("Brazilian E-Commerce Public Dataset Analysis")

# Sidebar
with st.sidebar:
    st.image("https://repository-images.githubusercontent.com/350512149/674fe100-90e9-11eb-90ed-9ec65e95c722")
    start_date, end_date = st.date_input(label='Set Time Range',min_value=start_date,
        max_value=end_date,
        value=[start_date, end_date]
    )    

filtered_data = main_df[(main_df["order_purchase_timestamp"] >= str(start_date)) & 
                        (main_df["order_purchase_timestamp"] <= str(end_date))]

sales_performance_df = create_sales_performance_df(filtered_data)
monthly_sales_df = create_monthly_sales_df(filtered_data)
payment_each_method_df = create_payment_each_method_df(filtered_data)
total_payments = create_total_payments(filtered_data)
total_orders = create_total_orders(filtered_data)
total_sellers = create_total_sellers(filtered_data)

# Columns row 1

col1_1, col1_2, col1_3 = st.columns(spec=3)

with col1_1:
    st.metric(label="Total Payments", value=total_payments)

with col1_2:
    st.metric(label="Total Orders", value=total_orders)

with col1_3:
    st.metric(label="Total Sellers", value=total_sellers)

col2_1, col2_2 = st.columns(spec=2)

# Columns row 2

with col2_1:
    fig, ax = plt.subplots(figsize=(9,6))

    sns.barplot(
        y = "seller_city",
        x = "price",
        data = sales_performance_df.head(5)
    )

    ax.set_title("Top 5 Sales by City", loc="center", fontsize=20)
    ax.set_ylabel(None)
    ax.set_xlabel( "Income ($)")
    ax.tick_params(axis='x', labelsize=12)
    st.pyplot(fig=fig)

with col2_2:
    monthly_sales_df['year_month'] = monthly_sales_df['year_month'].astype(str)
    fig, ax = plt.subplots(figsize=(9,6))

    sns.barplot(
        y="payment_value", 
        x="payment_type",
        data=payment_each_method_df.sort_values(by="payment_type", ascending=True)
    )

    ax.set_title("Payment Each Method", loc="center", fontsize=15)
    ax.set_ylabel(ylabel="Value ($)")
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=8)
    st.pyplot(fig)

monthly_sales_df['year_month'] = monthly_sales_df['year_month'].astype(str)

fig, ax = plt.subplots(figsize=(20, 7))

plt.plot(
    monthly_sales_df['year_month'], 
    monthly_sales_df['price'], 
    marker='o'
)

ax.set_title(label='Sales by Month')
ax.set_xlabel(xlabel='Month')
ax.set_ylabel(ylabel='Sales ($1,000,000)')
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=8)
ax.set_xticklabels(monthly_sales_df['year_month'], rotation=45)

st.pyplot(fig)
