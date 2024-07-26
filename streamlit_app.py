import streamlit as st

st.title("🎈 SQL TEST")


conn = st.connection('TOMSsql_Database', type = 'sql')
trades = conn.query('select * from Trading_Data')
st.dataframe(trades)
