import streamlit as st

st.title("🎈 SQL TEST")


conn = st.connection('TOMSsql_Database', type = 'sql')
trades = conn.query('select * from trading_data')
st.dataframe(trades)
