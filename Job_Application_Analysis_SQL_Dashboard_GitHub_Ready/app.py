import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title='Job Application Analytics',page_icon='📊',layout='wide')
st.title('📊 Job Application Analytics Dashboard')
st.caption('Portfolio project with synthetic sample data. Avoid uploading personal tracker data publicly.')
@st.cache_data
def load_data(): return pd.read_csv('data/job_applications_sample.csv',parse_dates=['applied_date'])
df=load_data(); st.sidebar.header('Filters')
dates=st.sidebar.date_input('Applied date range',[df.applied_date.min().date(),df.applied_date.max().date()])
portals=st.sidebar.multiselect('Portal',sorted(df.job_portal.unique()),default=sorted(df.job_portal.unique()))
roles=st.sidebar.multiselect('Role',sorted(df.job_role.unique()),default=sorted(df.job_role.unique()))
locations=st.sidebar.multiselect('Location',sorted(df.location.unique()),default=sorted(df.location.unique()))
statuses=st.sidebar.multiselect('Status',sorted(df.status.unique()),default=sorted(df.status.unique()))
if len(dates)==2: df=df[(df.applied_date.dt.date>=dates[0])&(df.applied_date.dt.date<=dates[1])]
df=df[df.job_portal.isin(portals)&df.job_role.isin(roles)&df.location.isin(locations)&df.status.isin(statuses)]
positive=df.status.isin(['Shortlisted','Interview Scheduled']).sum(); rate=positive/len(df)*100 if len(df) else 0
a,b,c,d=st.columns(4); a.metric('Applications',len(df)); b.metric('Positive Responses',int(positive)); c.metric('Positive Response Rate',f'{rate:.1f}%'); d.metric('Average Expected Salary',f'{df.expected_salary_lpa.mean():.2f} LPA' if df.expected_salary_lpa.notna().any() else 'N/A')
x,y=st.columns(2)
with x: st.subheader('Applications by Status'); st.plotly_chart(px.bar(df.groupby('status').size().reset_index(name='count'),x='status',y='count',color='status'),use_container_width=True)
with y: st.subheader('Applications by Portal'); st.plotly_chart(px.bar(df.groupby('job_portal').size().reset_index(name='count'),x='job_portal',y='count'),use_container_width=True)
u,v=st.columns(2)
with u: st.subheader('Monthly Application Trend'); monthly=df.groupby(df.applied_date.dt.to_period('M').astype(str)).size().reset_index(name='applications'); st.plotly_chart(px.line(monthly,x='applied_date',y='applications',markers=True),use_container_width=True)
with v: st.subheader('Applications by Role'); rr=df.groupby('job_role').size().reset_index(name='applications').sort_values('applications',ascending=False); st.plotly_chart(px.bar(rr,x='job_role',y='applications'),use_container_width=True)
st.subheader('Application Records'); st.dataframe(df.sort_values('applied_date',ascending=False),use_container_width=True); st.download_button('Download filtered CSV',df.to_csv(index=False).encode(),'filtered_job_applications.csv','text/csv')
