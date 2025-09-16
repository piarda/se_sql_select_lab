# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

# Query all data from the employees table
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)

print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

# STEP 2
df_first_five = pd.read_sql(
    """
    SELECT employeeNumber, lastName
    FROM employees
    """,
    conn
)
print("Step 2 Result: employeeNumber and lastName")
print(df_first_five.head())
print("\n")

# STEP 3
df_five_reverse = pd.read_sql(
    """
    SELECT lastName, employeeNumber
    FROM employees
    """,
    conn
)
print("Step 3 Result: lastName and employeeNumber (reversed)")
print(df_five_reverse.head())
print("\n")

# STEP 4
df_alias = pd.read_sql(
    """
    SELECT lastName, employeeNumber AS ID
    FROM employees
    """,
    conn
)
print("Step 4 Result: lastName and employeeNumber aliased as ID")
print(df_alias.head())
print("\n")

# STEP 5
df_executive = pd.read_sql(
    """
    SELECT
        lastName,
        jobTitle,
        CASE
            WHEN jobTitle = "President" OR jobTitle = "VP Sales" OR jobTitle = "VP Marketing" THEN "Executive"
            ELSE "Not Executive"
        END AS role
    FROM employees
    """,
    conn
)
print("Step 5 Result: jobTitle with role classification")
print(df_executive.head())
print("\n")

# STEP 6
df_name_length = pd.read_sql(
    """
    SELECT LENGTH(lastName) AS name_length
    FROM employees
    """,
    conn
)
print("Step 6 Result: Length of lastName")
print(df_name_length.head())
print("\n")

# STEP 7
df_short_title = pd.read_sql(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
    """,
    conn
)
print("Step 7 Result: First two letters of jobTitle")
print(df_short_title.head())
print("\n")

# STEP 8
sum_total_price_df = pd.read_sql(
    """
    SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_amount
    FROM orderDetails
    """,
    conn
)

# Extract scalar value from DataFrame
sum_total_price = [sum_total_price_df.iloc[0]['total_amount']]
print("Step 8 Result: Total amount for all orders (rounded sum):", sum_total_price, "\n")

# STEP 9
df_day_month_year = pd.read_sql(
    """
    SELECT orderDate,
           SUBSTR(orderDate, 9, 2) AS day,
           SUBSTR(orderDate, 6, 2) AS month,
           SUBSTR(orderDate, 1, 4) AS year
    FROM orders
    """,
    conn
)
print("Step 9 Result: orderDate broken into day/month/year")
print(df_day_month_year.head())
print("\n")

conn.close()
