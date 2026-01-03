# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# import plotly.express as px
# import snowflake.connector
# import numpy as np
# from datetime import datetime, timedelta

# # --------- Color Palette (Consistent Professional Theme) ---------
# COLORS = {
#     'primary': '#1e3a8a',      # Deep Blue
#     'secondary': '#0891b2',    # Teal
#     'success': '#059669',      # Green
#     'warning': '#d97706',      # Amber
#     'danger': '#dc2626',       # Red
#     'light': '#f1f5f9',        # Light Gray
#     'dark': '#0f172a',         # Dark Blue
# }

# # --------- Snowflake connection ---------
# @st.cache_resource
# def get_conn():
#     return snowflake.connector.connect(
#         account=st.secrets["snowflake"]["account"],
#         user=st.secrets["snowflake"]["user"],
#         password=st.secrets["snowflake"]["password"],
#         warehouse=st.secrets["snowflake"]["warehouse"],
#         database=st.secrets["snowflake"]["database"],
#         schema=st.secrets["snowflake"]["schema"],
#     )

# @st.cache_data
# def load_inventory():
#     conn = get_conn()
#     return pd.read_sql("SELECT * FROM TB_INVENTORY;", conn)

# @st.cache_data
# def load_cascade():
#     conn = get_conn()
#     return pd.read_sql("SELECT * FROM TB_CARE_CASCADE;", conn)

# @st.cache_data
# def load_providers():
#     conn = get_conn()
#     return pd.read_sql("SELECT * FROM TB_PROVIDERS;", conn)

# @st.cache_data
# def load_depots():
#     conn = get_conn()
#     return pd.read_sql("SELECT * FROM TB_DEPOTS;", conn)

# # --------- Custom CSS ---------
# st.markdown("""
# <style>
#     .main {
#         background-color: #f8fafc;
#     }
    
#     .dashboard-header {
#         background: linear-gradient(135deg, #1e3a8a 0%, #0891b2 100%);
#         padding: 2rem;
#         border-radius: 10px;
#         color: white;
#         margin-bottom: 2rem;
#     }
    
#     .dashboard-title {
#         font-size: 2.5rem;
#         font-weight: 700;
#         margin: 0;
#         color: white;
#     }
    
#     .dashboard-subtitle {
#         font-size: 1rem;
#         margin-top: 0.5rem;
#         opacity: 0.9;
#         color: white;
#     }
    
#     .kpi-card {
#         background: white;
#         padding: 1.5rem;
#         border-radius: 8px;
#         border-left: 4px solid #1e3a8a;
#         box-shadow: 0 1px 3px rgba(0,0,0,0.1);
#         flex: 1;
#     }
    
#     .kpi-card.success {
#         border-left-color: #059669;
#     }
    
#     .kpi-card.warning {
#         border-left-color: #d97706;
#     }
    
#     .kpi-card.danger {
#         border-left-color: #dc2626;
#     }
    
#     .kpi-label {
#         font-size: 0.875rem;
#         color: #64748b;
#         font-weight: 500;
#         text-transform: uppercase;
#         letter-spacing: 0.5px;
#     }
    
#     .kpi-value {
#         font-size: 2rem;
#         font-weight: 700;
#         color: #0f172a;
#         margin-top: 0.5rem;
#     }
    
#     .section-header {
#         font-size: 1.5rem;
#         font-weight: 600;
#         color: #1e3a8a;
#         margin: 2rem 0 1rem 0;
#         padding-bottom: 0.5rem;
#         border-bottom: 2px solid #e2e8f0;
#     }
    
#     .info-box {
#         background-color: #eff6ff;
#         border: 1px solid #3b82f6;
#         border-radius: 6px;
#         padding: 1rem;
#         margin: 1rem 0;
#     }
    
#     .info-box-title {
#         font-weight: 600;
#         color: #1e3a8a;
#         margin-bottom: 0.5rem;
#     }
    
#     .alert {
#         padding: 1rem;
#         border-radius: 6px;
#         margin: 0.5rem 0;
#         border-left: 4px solid;
#     }
    
#     .alert-critical {
#         background-color: #fef2f2;
#         border-left-color: #dc2626;
#     }
    
#     .alert-warning {
#         background-color: #fffbeb;
#         border-left-color: #d97706;
#     }
    
#     .alert-success {
#         background-color: #f0fdf4;
#         border-left-color: #059669;
#     }
    
#     .alert-title {
#         font-weight: 600;
#         margin-bottom: 0.5rem;
#     }
    
#     .stTabs [data-baseweb="tab-list"] {
#         gap: 0.5rem;
#         background-color: white;
#         padding: 0.5rem;
#         border-radius: 8px;
#     }
    
#     .stTabs [data-baseweb="tab"] {
#         height: 3rem;
#         padding: 0 1.5rem;
#         background-color: transparent;
#         border-radius: 6px;
#         color: #64748b;
#         font-weight: 500;
#     }
    
#     .stTabs [aria-selected="true"] {
#         background-color: #1e3a8a;
#         color: white;
#     }
    
#     .sidebar-header {
#         font-size: 1.25rem;
#         font-weight: 600;
#         color: #1e3a8a;
#         margin-bottom: 1rem;
#     }
# </style>
# """, unsafe_allow_html=True)

# # --------- Page config ---------
# st.set_page_config(
#     page_title="TB CareMap Indonesia", 
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # --------- Header ---------
# st.markdown("""
# <div class="dashboard-header">
#     <h1 class="dashboard-title">TB CareMap Indonesia Dashboard</h1>
#     <p class="dashboard-subtitle">Comprehensive tuberculosis inventory management, stock monitoring, and care cascade analysis across Indonesian provinces</p>
# </div>
# """, unsafe_allow_html=True)

# # --------- Load data ---------
# with st.spinner('Loading data from Snowflake...'):
#     inv_df = load_inventory()
#     cascade_df = load_cascade()
#     prov_df = load_providers()
#     depots_df = load_depots()

# # Use latest date per location and item
# latest = inv_df.sort_values("DATE").groupby(["LOCATION", "ITEM"]).tail(1).copy()

# # Calculate stock metrics
# latest["daily_need"] = latest["TB_CASES_ACTIVE"] / 30.0
# latest["days_of_therapy_left"] = np.where(
#     latest["daily_need"] > 0,
#     latest["CLOSING_STOCK"] / latest["daily_need"],
#     np.nan,
# )
# latest["stock_risk_flag"] = latest["days_of_therapy_left"] < latest["LEAD_TIME_DAYS"]
# latest["programmatic_risk"] = np.where(
#     latest["stock_risk_flag"], latest["TB_RISK_SCORE"] * 2, latest["TB_RISK_SCORE"]
# )
# latest["days_until_stockout_vs_lead"] = (
#     latest["days_of_therapy_left"] - latest["LEAD_TIME_DAYS"]
# )

# # Calculate reorder suggestions
# latest["suggested_reorder_qty"] = np.where(
#     latest["stock_risk_flag"],
#     latest["daily_need"] * (latest["LEAD_TIME_DAYS"] + 30),
#     0
# )

# # --------- Sidebar Filters ---------
# with st.sidebar:
#     st.markdown('<p class="sidebar-header">Filter Settings</p>', unsafe_allow_html=True)
    
#     selected_locations = st.multiselect(
#         "Provinces",
#         options=sorted(latest["LOCATION"].unique()),
#         default=sorted(latest["LOCATION"].unique())
#     )
    
#     selected_items = st.multiselect(
#         "Tuberculosis Regimens",
#         options=sorted(latest["ITEM"].unique()),
#         default=sorted(latest["ITEM"].unique())
#     )
    
#     risk_threshold = st.slider(
#         "Risk Threshold",
#         min_value=0,
#         max_value=10,
#         value=8,
#         help="Alert threshold for programmatic risk score"
#     )
    
#     st.markdown("---")
#     st.markdown('<p class="sidebar-header">Data Summary</p>', unsafe_allow_html=True)
#     st.metric("Total Records", f"{len(inv_df):,}")
#     last_date = str(inv_df["DATE"].max()) if not inv_df.empty else "Not Available"
#     st.markdown(f"**Last Updated:** {last_date}")

# # Filter data
# filtered_latest = latest[
#     (latest["LOCATION"].isin(selected_locations)) & 
#     (latest["ITEM"].isin(selected_items))
# ]

# # --------- Key Performance Indicators ---------
# st.markdown('<h2 class="section-header">Key Performance Indicators</h2>', unsafe_allow_html=True)

# col1, col2, col3, col4, col5 = st.columns(5)

# with col1:
#     st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-label">Total Provinces</div>
#         <div class="kpi-value">{int(inv_df["LOCATION"].nunique())}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown(f"""
#     <div class="kpi-card success">
#         <div class="kpi-label">Tuberculosis Regimens</div>
#         <div class="kpi-value">{int(inv_df["ITEM"].nunique())}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with col3:
#     st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-label">Active Tuberculosis Cases</div>
#         <div class="kpi-value">{int(latest["TB_CASES_ACTIVE"].sum()):,}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with col4:
#     high_risk_count = int((filtered_latest["programmatic_risk"] >= risk_threshold).sum())
#     st.markdown(f"""
#     <div class="kpi-card warning">
#         <div class="kpi-label">High-Risk Pairs</div>
#         <div class="kpi-value">{high_risk_count}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with col5:
#     stockout_count = int((filtered_latest["days_until_stockout_vs_lead"] < 0).sum())
#     st.markdown(f"""
#     <div class="kpi-card danger">
#         <div class="kpi-label">Critical Stockouts</div>
#         <div class="kpi-value">{stockout_count}</div>
#     </div>
#     """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)

# # --------- Main Tabs ---------
# tab1, tab2, tab3, tab4, tab5 = st.tabs([
#     "Inventory Overview", 
#     "Critical Alerts", 
#     "Care Cascade", 
#     "Provider Coverage",
#     "Distribution Network"
# ])

# # --------- TAB 1: Inventory Heatmap ---------
# with tab1:
#     st.markdown('<h2 class="section-header">Inventory Health: Stock Risk Analysis</h2>', unsafe_allow_html=True)
    
#     st.markdown("""
#     <div class="info-box">
#         <div class="info-box-title">Heatmap Interpretation Guide</div>
#         <p><strong style="color: #dc2626;">Red zones:</strong> High tuberculosis burden with inadequate stock levels (urgent action required)</p>
#         <p><strong style="color: #d97706;">Orange zones:</strong> Moderate risk requiring close monitoring</p>
#         <p><strong style="color: #059669;">Green zones:</strong> Adequate stock levels relative to demand</p>
#         <p>Values represent programmatic risk scores calculated from tuberculosis burden and stock availability</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     pivot = filtered_latest.pivot_table(
#         index="LOCATION",
#         columns="ITEM",
#         values="programmatic_risk",
#         aggfunc="mean"
#     )
    
#     fig = go.Figure(
#         data=go.Heatmap(
#             z=pivot.values,
#             x=pivot.columns,
#             y=pivot.index,
#             colorscale="RdYlGn_r",
#             colorbar=dict(
#                 title="Risk Score",
#                 thickness=20,
#                 len=0.7
#             ),
#             text=np.round(pivot.values, 1),
#             texttemplate="%{text}",
#             textfont={"size": 10, "color": "white"},
#             hoverongaps=False,
#             hovertemplate='<b>%{y}</b><br>%{x}<br>Risk: %{z:.1f}<extra></extra>'
#         )
#     )
    
#     fig.update_layout(
#         height=500,
#         xaxis_title="Tuberculosis Regimen",
#         yaxis_title="Province",
#         title={
#             'text': "Programmatic Risk Heatmap by Province and Regimen",
#             'x': 0.5,
#             'xanchor': 'center',
#             'font': {'size': 16, 'color': COLORS['primary']}
#         },
#         font=dict(size=11),
#         plot_bgcolor='white',
#         paper_bgcolor='white'
#     )
    
#     st.plotly_chart(fig, use_container_width=True)
    
#     # Stock status overview
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("**Stock Status Distribution**")
#         status_counts = pd.DataFrame({
#             'Status': ['Critical Stockout', 'Warning Level', 'Adequate Stock'],
#             'Count': [
#                 int((filtered_latest["days_until_stockout_vs_lead"] < 0).sum()),
#                 int(((filtered_latest["days_until_stockout_vs_lead"] >= 0) & 
#                      (filtered_latest["stock_risk_flag"])).sum()),
#                 int((~filtered_latest["stock_risk_flag"]).sum())
#             ]
#         })
        
#         fig_pie = px.pie(
#             status_counts, 
#             values='Count', 
#             names='Status',
#             color='Status',
#             color_discrete_map={
#                 'Critical Stockout': COLORS['danger'],
#                 'Warning Level': COLORS['warning'],
#                 'Adequate Stock': COLORS['success']
#             },
#             hole=0.4
#         )
#         fig_pie.update_traces(textposition='inside', textinfo='percent+label')
#         fig_pie.update_layout(height=350, showlegend=True, paper_bgcolor='white', plot_bgcolor='white')
#         st.plotly_chart(fig_pie, use_container_width=True)
    
#     with col2:
#         st.markdown("**Days of Therapy Remaining by Province**")
#         fig_box = px.box(
#             filtered_latest[filtered_latest["days_of_therapy_left"].notna()],
#             y="days_of_therapy_left",
#             x="LOCATION",
#             color="LOCATION",
#             labels={"days_of_therapy_left": "Days", "LOCATION": "Province"}
#         )
#         fig_box.update_layout(
#             height=350,
#             showlegend=False,
#             yaxis_title="Days of Therapy Remaining",
#             paper_bgcolor='white',
#             plot_bgcolor='white'
#         )
#         st.plotly_chart(fig_box, use_container_width=True)

# # --------- TAB 2: Critical Alerts ---------
# with tab2:
#     st.markdown('<h2 class="section-header">Critical Stock Alerts and Procurement Recommendations</h2>', unsafe_allow_html=True)
    
#     alerts = filtered_latest[filtered_latest["days_until_stockout_vs_lead"] < 0].sort_values(
#         "days_until_stockout_vs_lead"
#     )
    
#     if alerts.empty:
#         st.markdown("""
#         <div class="alert alert-success">
#             <div class="alert-title">All Stock Levels Adequate</div>
#             <p>No critical alerts detected. All inventory levels are sufficient relative to lead times and current demand.</p>
#         </div>
#         """, unsafe_allow_html=True)
#     else:
#         st.markdown(f"""
#         <div class="alert alert-critical">
#             <div class="alert-title">Critical Alert: {len(alerts)} Items Require Immediate Action</div>
#             <p>The following items will exhaust stock before the next scheduled delivery. Immediate procurement action is required.</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Create detailed alert cards
#         for idx, r in alerts.iterrows():
#             days_short = abs(r['days_until_stockout_vs_lead'])
#             severity_label = "CRITICAL" if days_short > 7 else "URGENT"
            
#             st.markdown(f"""
#             <div class="alert alert-critical">
#                 <div class="alert-title">{severity_label}: {r['LOCATION']} - {r['ITEM']}</div>
#                 <p><strong>Stock exhaustion: {days_short:.1f} days before next delivery</strong></p>
#                 <ul style="margin: 0.5rem 0;">
#                     <li>Current stock: {int(r['CLOSING_STOCK'])} units</li>
#                     <li>Active tuberculosis patients: {int(r['TB_CASES_ACTIVE'])}</li>
#                     <li>Days of therapy remaining: {r['days_of_therapy_left']:.1f}</li>
#                     <li>Procurement lead time: {int(r['LEAD_TIME_DAYS'])} days</li>
#                     <li>Tuberculosis risk score: {r['TB_RISK_SCORE']:.1f}/10</li>
#                     <li><strong>Recommended reorder quantity: {int(r['suggested_reorder_qty'])} units</strong></li>
#                 </ul>
#             </div>
#             """, unsafe_allow_html=True)
        
#         st.markdown("---")
#         st.markdown("**Detailed Alert Table**")
        
#         alert_export = alerts[[
#             "LOCATION", "ITEM", "CLOSING_STOCK", "TB_CASES_ACTIVE",
#             "LEAD_TIME_DAYS", "days_of_therapy_left", "days_until_stockout_vs_lead",
#             "TB_RISK_SCORE", "programmatic_risk", "suggested_reorder_qty"
#         ]].copy()
        
#         alert_export.columns = [
#             "Province", "Tuberculosis Regimen", "Current Stock", "Active Cases",
#             "Lead Time (Days)", "Days Left", "Shortfall (Days)",
#             "Tuberculosis Risk Score", "Programmatic Risk", "Suggested Reorder"
#         ]
        
#         st.dataframe(alert_export, use_container_width=True)
        
#         # Download button
#         csv = alert_export.to_csv(index=False).encode('utf-8')
#         st.download_button(
#             label="Download Priority Procurement List (CSV)",
#             data=csv,
#             file_name=f"tb_critical_alerts_{datetime.now().strftime('%Y%m%d')}.csv",
#             mime="text/csv",
#             help="Export for procurement teams"
#         )
    
#     # Warning items
#     st.markdown("**Items Approaching Low Stock (Monitor Closely)**")
#     warnings = filtered_latest[
#         (filtered_latest["days_until_stockout_vs_lead"] >= 0) & 
#         (filtered_latest["stock_risk_flag"])
#     ].sort_values("days_of_therapy_left")
    
#     if not warnings.empty:
#         for idx, r in warnings.head(10).iterrows():
#             st.markdown(f"""
#             <div class="alert alert-warning">
#                 <strong>{r['LOCATION']} - {r['ITEM']}</strong><br>
#                 Days remaining: {r['days_of_therapy_left']:.1f} | 
#                 Lead time: {int(r['LEAD_TIME_DAYS'])} days | 
#                 Active cases: {int(r['TB_CASES_ACTIVE'])} | 
#                 Reorder quantity: {int(r['suggested_reorder_qty'])} units
#             </div>
#             """, unsafe_allow_html=True)
#     else:
#         st.info("No items in warning zone.")

# # --------- TAB 3: Care Cascade ---------
# with tab3:
#     st.markdown('<h2 class="section-header">Treatment Speed: Care Cascade Analysis</h2>', unsafe_allow_html=True)
    
#     cascade_df = cascade_df.copy()
#     cascade_df["total_delay_days"] = (
#         cascade_df["MEDIAN_PATIENT_DELAY_DAYS"]
#         + cascade_df["MEDIAN_DIAGNOSTIC_DELAY_DAYS"]
#         + cascade_df["MEDIAN_TREATMENT_DELAY_DAYS"]
#     )
    
#     st.markdown("""
#     <div class="info-box">
#         <div class="info-box-title">Care Cascade Metrics</div>
#         <p>Total delay represents the cumulative time from symptom onset to treatment initiation. Shorter delays improve patient outcomes and reduce tuberculosis transmission in communities.</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Stacked bar chart
#     fig_cascade = go.Figure()
    
#     fig_cascade.add_trace(go.Bar(
#         x=cascade_df["LOCATION"],
#         y=cascade_df["MEDIAN_PATIENT_DELAY_DAYS"],
#         name="Patient Delay",
#         marker_color=COLORS['primary'],
#         hovertemplate='<b>%{x}</b><br>Patient: %{y:.1f} days<extra></extra>'
#     ))
    
#     fig_cascade.add_trace(go.Bar(
#         x=cascade_df["LOCATION"],
#         y=cascade_df["MEDIAN_DIAGNOSTIC_DELAY_DAYS"],
#         name="Diagnostic Delay",
#         marker_color=COLORS['secondary'],
#         hovertemplate='<b>%{x}</b><br>Diagnostic: %{y:.1f} days<extra></extra>'
#     ))
    
#     fig_cascade.add_trace(go.Bar(
#         x=cascade_df["LOCATION"],
#         y=cascade_df["MEDIAN_TREATMENT_DELAY_DAYS"],
#         name="Treatment Delay",
#         marker_color=COLORS['warning'],
#         hovertemplate='<b>%{x}</b><br>Treatment: %{y:.1f} days<extra></extra>'
#     ))
    
#     fig_cascade.update_layout(
#         barmode='stack',
#         xaxis_title="Province",
#         yaxis_title="Delay (Days)",
#         height=450,
#         title={
#             'text': "Care Cascade Delay Breakdown by Province",
#             'x': 0.5,
#             'xanchor': 'center',
#             'font': {'size': 16, 'color': COLORS['primary']}
#         },
#         hovermode='x unified',
#         legend=dict(
#             orientation="h",
#             yanchor="bottom",
#             y=1.02,
#             xanchor="right",
#             x=1
#         ),
#         paper_bgcolor='white',
#         plot_bgcolor='white'
#     )
    
#     st.plotly_chart(fig_cascade, use_container_width=True)
    
#     # Detailed analysis
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("**Delay Statistics by Province**")
#         cascade_display = cascade_df[[
#             "LOCATION", "MEDIAN_PATIENT_DELAY_DAYS", 
#             "MEDIAN_DIAGNOSTIC_DELAY_DAYS", "MEDIAN_TREATMENT_DELAY_DAYS",
#             "total_delay_days"
#         ]].copy()
        
#         cascade_display.columns = [
#             "Province", "Patient Delay", "Diagnostic Delay", 
#             "Treatment Delay", "Total Delay"
#         ]
        
#         st.dataframe(cascade_display, use_container_width=True)
    
#     with col2:
#         st.markdown("**Average System Delays**")
#         avg_delays = pd.DataFrame({
#             'Stage': ['Patient Delay', 'Diagnostic Delay', 'Treatment Delay'],
#             'Average (Days)': [
#                 cascade_df["MEDIAN_PATIENT_DELAY_DAYS"].mean(),
#                 cascade_df["MEDIAN_DIAGNOSTIC_DELAY_DAYS"].mean(),
#                 cascade_df["MEDIAN_TREATMENT_DELAY_DAYS"].mean()
#             ]
#         })
        
#         fig_avg = px.bar(
#             avg_delays,
#             x='Stage',
#             y='Average (Days)',
#             color='Stage',
#             color_discrete_sequence=[COLORS['primary'], COLORS['secondary'], COLORS['warning']]
#         )
#         fig_avg.update_layout(height=300, showlegend=False, paper_bgcolor='white', plot_bgcolor='white')
#         st.plotly_chart(fig_avg, use_container_width=True)

# # --------- TAB 4: Provider Coverage ---------
# with tab4:
#     st.markdown('<h2 class="section-header">Healthcare Provider Coverage Analysis</h2>', unsafe_allow_html=True)
    
#     prov_summary = prov_df.groupby("LOCATION").agg(
#         facilities=("FACILITY_ID", "nunique"),
#         total_doctors=("DOCTOR_COUNT", "sum")
#     ).reset_index()
    
#     # Merge with tuberculosis cases
#     prov_with_cases = prov_summary.merge(
#         latest.groupby("LOCATION")["TB_CASES_ACTIVE"].sum().reset_index(),
#         on="LOCATION",
#         how="left"
#     )
#     prov_with_cases["patients_per_doctor"] = (
#         prov_with_cases["TB_CASES_ACTIVE"] / prov_with_cases["total_doctors"]
#     )
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("**Facilities and Healthcare Providers**")
#         fig_providers = go.Figure()
#         fig_providers.add_trace(go.Bar(
#             x=prov_with_cases["LOCATION"],
#             y=prov_with_cases["facilities"],
#             name="Facilities",
#             marker_color=COLORS['primary']
#         ))
#         fig_providers.add_trace(go.Bar(
#             x=prov_with_cases["LOCATION"],
#             y=prov_with_cases["total_doctors"],
#             name="Doctors",
#             marker_color=COLORS['success']
#         ))
#         fig_providers.update_layout(
#             barmode='group',
#             height=350,
#             xaxis_title="Province",
#             yaxis_title="Count",
#             paper_bgcolor='white',
#             plot_bgcolor='white'
#         )
#         st.plotly_chart(fig_providers, use_container_width=True)
    
#     with col2:
#         st.markdown("**Patient-to-Doctor Ratio**")
#         fig_ratio = px.bar(
#             prov_with_cases,
#             x="LOCATION",
#             y="patients_per_doctor",
#             color="patients_per_doctor",
#             color_continuous_scale=[[0, COLORS['success']], [1, COLORS['danger']]],
#             labels={"patients_per_doctor": "Ratio"}
#         )
#         fig_ratio.update_layout(height=350, showlegend=False, paper_bgcolor='white', plot_bgcolor='white')
#         st.plotly_chart(fig_ratio, use_container_width=True)
    
#     st.markdown("**Provider Summary**")
#     prov_with_cases.columns = ["Province", "Facilities", "Total Doctors", "Active Tuberculosis Cases", "Patients per Doctor"]
#     st.dataframe(prov_with_cases, use_container_width=True)
    
#     st.markdown("---")
#     st.markdown("**Facility Details and Incentive Programs**")
    
#     facility_display = prov_df[[
#         "FACILITY_NAME", "LOCATION", "DOCTOR_COUNT", "INCENTIVE_SCHEME"
#     ]].copy()
#     facility_display.columns = ["Facility Name", "Province", "Doctor Count", "Incentive Scheme"]
    
#     st.dataframe(facility_display, use_container_width=True)

# # --------- TAB 5: Distribution Network ---------
# with tab5:
#     st.markdown('<h2 class="section-header">Tuberculosis Drug Distribution Network</h2>', unsafe_allow_html=True)
    
#     st.markdown("""
#     <div class="info-box">
#         <div class="info-box-title">Distribution Network Overview</div>
#         <p>Strategic depot locations managing tuberculosis pharmaceutical supply chain and distribution logistics across Indonesia</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Map if coordinates available
#     if 'LATITUDE' in depots_df.columns and 'LONGITUDE' in depots_df.columns:
#         st.markdown("**Geographic Distribution of Depots**")
        
#         fig_map = px.scatter_mapbox(
#             depots_df,
#             lat="LATITUDE",
#             lon="LONGITUDE",
#             hover_name="DEPOT_NAME",
#             hover_data=["LOCATION", "REGION", "STOCK_LEVEL"],
#             color="STOCK_LEVEL",
#             size="STOCK_LEVEL",
#             color_continuous_scale=[[0, COLORS['danger']], [1, COLORS['success']]],
#             zoom=4,
#             height=500
#         )
#         fig_map.update_layout(mapbox_style="open-street-map", paper_bgcolor='white')
#         st.plotly_chart(fig_map, use_container_width=True)
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("**Depot Stock Levels**")
#         fig_depot_stock = px.bar(
#             depots_df.sort_values("STOCK_LEVEL", ascending=False),
#             x="DEPOT_NAME",
#             y="STOCK_LEVEL",
#             color="REGION",
#             labels={"STOCK_LEVEL": "Stock Level", "DEPOT_NAME": "Depot"}
#         )
#         fig_depot_stock.update_layout(height=350, paper_bgcolor='white', plot_bgcolor='white')
#         st.plotly_chart(fig_depot_stock, use_container_width=True)
    
#     with col2:
#         st.markdown("**Regional Distribution**")
#         regional_stats = depots_df.groupby("REGION").agg({
#             "DEPOT_ID": "count",
#             "STOCK_LEVEL": "sum"
#         }).reset_index()
#         regional_stats.columns = ["Region", "Depot Count", "Total Stock"]
        
#         fig_regional = px.pie(
#             regional_stats,
#             values="Depot Count",
#             names="Region",
#             hole=0.4
#         )
#         fig_regional.update_layout(height=350, paper_bgcolor='white')
#         st.plotly_chart(fig_regional, use_container_width=True)
    
#     st.markdown("**Complete Depot Listing**")
#     st.dataframe(depots_df, use_container_width=True)

# # --------- Footer ---------
# st.markdown("---")
# st.markdown("""
# <div style="text-align: center; color: #64748b; padding: 2rem;">
#     <p><strong>TB CareMap Indonesia Dashboard</strong></p>
#     <p>Powered by Snowflake Data Platform | Built with Streamlit</p>
#     <p style="font-size: 0.875rem; margin-top: 0.5rem;">@ThalitaZahra Note: All data shown is synthetic for demonstration purposes</p>
# </div>
# """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import snowflake.connector
import numpy as np
from datetime import datetime, timedelta

# --------- Professional Color Palette ---------
COLORS = {
    'primary': '#1e40af',       # Professional Blue
    'primary_light': '#3b82f6',
    'secondary': '#0e7490',     # Deep Teal
    'secondary_light': '#06b6d4',
    'success': '#047857',       # Forest Green
    'success_light': '#10b981',
    'warning': '#b45309',       # Deep Amber
    'warning_light': '#f59e0b',
    'danger': '#b91c1c',        # Deep Red
    'danger_light': '#ef4444',
    'neutral': '#64748b',
    'light_bg': '#f8fafc',
    'white': '#ffffff',
    'text_primary': '#0f172a',
    'text_secondary': '#475569',
}

# --------- Snowflake Connection ---------
@st.cache_resource
def get_conn():
    return snowflake.connector.connect(
        account=st.secrets["snowflake"]["account"],
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        warehouse=st.secrets["snowflake"]["warehouse"],
        database=st.secrets["snowflake"]["database"],
        schema=st.secrets["snowflake"]["schema"],
    )

@st.cache_data
def load_inventory():
    conn = get_conn()
    return pd.read_sql("SELECT * FROM TB_INVENTORY;", conn)

@st.cache_data
def load_cascade():
    conn = get_conn()
    return pd.read_sql("SELECT * FROM TB_CARE_CASCADE;", conn)

@st.cache_data
def load_providers():
    conn = get_conn()
    return pd.read_sql("SELECT * FROM TB_PROVIDERS;", conn)

@st.cache_data
def load_depots():
    conn = get_conn()
    return pd.read_sql("SELECT * FROM TB_DEPOTS;", conn)

# --------- Enhanced Custom CSS ---------
st.markdown("""
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        background: linear-gradient(to bottom, #f8fafc 0%, #e2e8f0 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Section */
    .dashboard-header {
        background: linear-gradient(135deg, #1e40af 0%, #0e7490 100%);
        padding: 2.5rem 3rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(30, 64, 175, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .dashboard-header::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .dashboard-title {
        font-size: 2.75rem;
        font-weight: 700;
        margin: 0;
        color: #ffffff !important;
        letter-spacing: -0.5px;
        position: relative;
        z-index: 1;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .dashboard-subtitle {
        font-size: 1.1rem;
        margin-top: 0.75rem;
        opacity: 0.95;
        color: #ffffff !important;
        font-weight: 400;
        line-height: 1.6;
        position: relative;
        z-index: 1;
    }
    
    .dashboard-meta {
        margin-top: 1.5rem;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(255,255,255,0.2);
        color: #ffffff;
        opacity: 0.9;
        font-size: 0.9rem;
        position: relative;
        z-index: 1;
    }
    
    /* KPI Cards */
    .kpi-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2rem;
    }
    
    .kpi-card {
        background: white;
        padding: 2rem 1.75rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .kpi-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
    }
    
    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: #1e40af;
    }
    
    .kpi-card.success::before { background: #047857; }
    .kpi-card.warning::before { background: #b45309; }
    .kpi-card.danger::before { background: #b91c1c; }
    
    .kpi-label {
        font-size: 0.75rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.75rem;
    }
    
    .kpi-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #0f172a;
        line-height: 1;
        margin-bottom: 0.5rem;
    }
    
    .kpi-change {
        font-size: 0.875rem;
        color: #64748b;
        font-weight: 500;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 1.75rem;
        font-weight: 700;
        color: #1e40af;
        margin: 3rem 0 1.5rem 0;
        padding-bottom: 1rem;
        border-bottom: 3px solid #e2e8f0;
        position: relative;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -3px;
        left: 0;
        width: 80px;
        height: 3px;
        background: #1e40af;
    }
    
    /* Information Boxes */
    .info-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border: 1px solid #3b82f6;
        border-left: 4px solid #1e40af;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .info-box-title {
        font-weight: 700;
        color: #1e40af;
        margin-bottom: 0.75rem;
        font-size: 1rem;
    }
    
    .info-box p {
        margin: 0.5rem 0;
        color: #475569;
        line-height: 1.6;
    }
    
    .info-legend {
        display: flex;
        gap: 1.5rem;
        margin-top: 1rem;
        flex-wrap: wrap;
    }
    
    .legend-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.875rem;
    }
    
    .legend-color {
        width: 16px;
        height: 16px;
        border-radius: 3px;
    }
    
    /* Alert Boxes */
    .alert {
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid;
        background: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    
    .alert-critical {
        border-left-color: #b91c1c;
        background: linear-gradient(to right, #fef2f2 0%, white 100%);
    }
    
    .alert-warning {
        border-left-color: #b45309;
        background: linear-gradient(to right, #fffbeb 0%, white 100%);
    }
    
    .alert-success {
        border-left-color: #047857;
        background: linear-gradient(to right, #f0fdf4 0%, white 100%);
    }
    
    .alert-title {
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 0.75rem;
        color: #0f172a;
    }
    
    .alert-content {
        color: #475569;
        line-height: 1.6;
    }
    
    .alert-metrics {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 1px solid #e2e8f0;
    }
    
    .alert-metric {
        font-size: 0.875rem;
    }
    
    .alert-metric-label {
        color: #64748b;
        font-weight: 500;
    }
    
    .alert-metric-value {
        color: #0f172a;
        font-weight: 700;
        font-size: 1rem;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: white;
        padding: 0.75rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        border: 1px solid #e2e8f0;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 3.5rem;
        padding: 0 2rem;
        background: transparent;
        border-radius: 8px;
        color: #64748b;
        font-weight: 600;
        font-size: 0.95rem;
        border: none;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1e40af 0%, #0e7490 100%);
        color: white;
        box-shadow: 0 4px 12px rgba(30, 64, 175, 0.3);
    }
    
    /* Sidebar */
    .sidebar-header {
        font-size: 1.25rem;
        font-weight: 700;
        color: #1e40af;
        margin-bottom: 1.5rem;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid #e2e8f0;
    }
    
    .sidebar-section {
        margin-bottom: 2rem;
    }
    
    .sidebar-label {
        font-size: 0.875rem;
        font-weight: 600;
        color: #475569;
        margin-bottom: 0.5rem;
    }
    
    /* Data Tables */
    .dataframe {
        font-size: 0.875rem;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    
    /* Buttons */
    .stDownloadButton button {
        background: linear-gradient(135deg, #1e40af 0%, #0e7490 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(30, 64, 175, 0.2);
    }
    
    .stDownloadButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(30, 64, 175, 0.3);
    }
    
    /* Stats Card */
    .stats-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin: 1rem 0;
    }
    
    .stats-title {
        font-weight: 600;
        color: #475569;
        font-size: 0.875rem;
        margin-bottom: 1rem;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
    }
    
    .stat-item {
        padding: 0.75rem;
        background: #f8fafc;
        border-radius: 6px;
    }
    
    .stat-label {
        font-size: 0.75rem;
        color: #64748b;
        margin-bottom: 0.25rem;
    }
    
    .stat-value {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0f172a;
    }
</style>
""", unsafe_allow_html=True)

# --------- Page Configuration ---------
st.set_page_config(
    page_title="TB CareMap Indonesia", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------- Header ---------
st.markdown(f"""
<div class="dashboard-header">
    <h1 class="dashboard-title" style="color: #ffffff !important;">TB CareMap Indonesia</h1>
    <p class="dashboard-subtitle" style="color: #ffffff !important;">National Tuberculosis Inventory Management System<br>
    Real-time monitoring of pharmaceutical supply chain, stock levels, and treatment cascade across Indonesian provinces</p>
    <div class="dashboard-meta" style="color: rgba(255,255,255,0.9) !important;">
        Powered by Snowflake Data Platform • Built for Indonesia Ministry of Health
    </div>
</div>
""", unsafe_allow_html=True)

# --------- Load Data ---------
with st.spinner('Loading data from Snowflake database...'):
    inv_df = load_inventory()
    cascade_df = load_cascade()
    prov_df = load_providers()
    depots_df = load_depots()

# Calculate metrics from latest data
latest = inv_df.sort_values("DATE").groupby(["LOCATION", "ITEM"]).tail(1).copy()

# Stock calculations
latest["daily_need"] = latest["TB_CASES_ACTIVE"] / 30.0
latest["days_of_therapy_left"] = np.where(
    latest["daily_need"] > 0,
    latest["CLOSING_STOCK"] / latest["daily_need"],
    np.nan,
)
latest["stock_risk_flag"] = latest["days_of_therapy_left"] < latest["LEAD_TIME_DAYS"]
latest["programmatic_risk"] = np.where(
    latest["stock_risk_flag"], latest["TB_RISK_SCORE"] * 2, latest["TB_RISK_SCORE"]
)
latest["days_until_stockout_vs_lead"] = (
    latest["days_of_therapy_left"] - latest["LEAD_TIME_DAYS"]
)
latest["suggested_reorder_qty"] = np.where(
    latest["stock_risk_flag"],
    latest["daily_need"] * (latest["LEAD_TIME_DAYS"] + 30),
    0
)

# --------- Sidebar Filters ---------
with st.sidebar:
    st.markdown('<p class="sidebar-header">Filter Controls</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-label">Geographic Scope</p>', unsafe_allow_html=True)
    selected_locations = st.multiselect(
        "Select Provinces",
        options=sorted(latest["LOCATION"].unique()),
        default=sorted(latest["LOCATION"].unique()),
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-label">Treatment Regimens</p>', unsafe_allow_html=True)
    selected_items = st.multiselect(
        "Select TB Regimens",
        options=sorted(latest["ITEM"].unique()),
        default=sorted(latest["ITEM"].unique()),
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-label">Risk Parameters</p>', unsafe_allow_html=True)
    risk_threshold = st.slider(
        "Programmatic Risk Threshold",
        min_value=0,
        max_value=10,
        value=8,
        help="Alert threshold for programmatic risk score (0-10 scale)"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown('<p class="sidebar-header">Data Summary</p>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="stats-card">
        <div class="stats-grid">
            <div class="stat-item">
                <div class="stat-label">Total Records</div>
                <div class="stat-value">{len(inv_df):,}</div>
            </div>
            <div class="stat-item">
                <div class="stat-label">Provinces</div>
                <div class="stat-value">{inv_df["LOCATION"].nunique()}</div>
            </div>
            <div class="stat-item">
                <div class="stat-label">Last Updated</div>
                <div class="stat-value" style="font-size: 0.9rem;">{str(inv_df["DATE"].max()) if not inv_df.empty else "N/A"}</div>
            </div>
            <div class="stat-item">
                <div class="stat-label">Data Points</div>
                <div class="stat-value">{len(latest):,}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Filter data
filtered_latest = latest[
    (latest["LOCATION"].isin(selected_locations)) & 
    (latest["ITEM"].isin(selected_items))
]

# --------- KPI Section ---------
st.markdown('<h2 class="section-header">Key Performance Indicators</h2>', unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Provinces</div>
        <div class="kpi-value">{int(inv_df["LOCATION"].nunique())}</div>
        <div class="kpi-change">Geographic Coverage</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">TB Regimens</div>
        <div class="kpi-value">{int(inv_df["ITEM"].nunique())}</div>
        <div class="kpi-change">Treatment Options</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Active Cases</div>
        <div class="kpi-value">{int(latest["TB_CASES_ACTIVE"].sum()):,}</div>
        <div class="kpi-change">Patients in Treatment</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    high_risk_count = int((filtered_latest["programmatic_risk"] >= risk_threshold).sum())
    st.markdown(f"""
    <div class="kpi-card warning">
        <div class="kpi-label">High-Risk Pairs</div>
        <div class="kpi-value">{high_risk_count}</div>
        <div class="kpi-change">Requires Monitoring</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    stockout_count = int((filtered_latest["days_until_stockout_vs_lead"] < 0).sum())
    st.markdown(f"""
    <div class="kpi-card danger">
        <div class="kpi-label">Critical Alerts</div>
        <div class="kpi-value">{stockout_count}</div>
        <div class="kpi-change">Immediate Action Required</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --------- Main Tabs ---------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Inventory Analysis", 
    "Critical Alerts", 
    "Care Cascade", 
    "Provider Network",
    "Distribution System"
])

# --------- TAB 1: Inventory Analysis ---------
with tab1:
    st.markdown('<h2 class="section-header">Inventory Health Assessment</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <div class="info-box-title">Programmatic Risk Heatmap - Interpretation Guide</div>
        <p>This visualization displays the intersection of tuberculosis disease burden and pharmaceutical inventory adequacy across Indonesian provinces. Risk scores are calculated using a weighted algorithm that considers stock levels relative to lead times and active case loads.</p>
        <div class="info-legend">
            <div class="legend-item">
                <div class="legend-color" style="background: #b91c1c;"></div>
                <span><strong>Critical Risk (Red):</strong> Inadequate stock with high TB burden</span>
            </div>
            <div class="legend-item">
                <div class="legend-color" style="background: #f59e0b;"></div>
                <span><strong>Moderate Risk (Orange):</strong> Requires close monitoring</span>
            </div>
            <div class="legend-item">
                <div class="legend-color" style="background: #10b981;"></div>
                <span><strong>Low Risk (Green):</strong> Adequate supply levels</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    pivot = filtered_latest.pivot_table(
        index="LOCATION",
        columns="ITEM",
        values="programmatic_risk",
        aggfunc="mean"
    )
    
    fig = go.Figure(
        data=go.Heatmap(
            z=pivot.values,
            x=pivot.columns,
            y=pivot.index,
            colorscale=[
                [0, COLORS['success']],
                [0.5, COLORS['warning']],
                [1, COLORS['danger']]
            ],
            colorbar=dict(
                title=dict(text="Risk Score", font=dict(size=12)),
                thickness=15,
                len=0.7,
                tickfont=dict(size=10)
            ),
            text=np.round(pivot.values, 1),
            texttemplate="%{text}",
            textfont={"size": 9, "color": "white"},
            hoverongaps=False,
            hovertemplate='<b>Province:</b> %{y}<br><b>Regimen:</b> %{x}<br><b>Risk Score:</b> %{z:.1f}<extra></extra>'
        )
    )
    
    fig.update_layout(
        height=550,
        xaxis_title="Treatment Regimen",
        yaxis_title="Province",
        title={
            'text': "Programmatic Risk Matrix: Province × Regimen",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': COLORS['primary'], 'family': 'Inter'}
        },
        font=dict(size=10, family='Inter'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(l=150, r=50, t=80, b=80)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Analytics Grid
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Stock Status Distribution**")
        status_counts = pd.DataFrame({
            'Status': ['Critical Stockout', 'Warning Level', 'Adequate Supply'],
            'Count': [
                int((filtered_latest["days_until_stockout_vs_lead"] < 0).sum()),
                int(((filtered_latest["days_until_stockout_vs_lead"] >= 0) & 
                     (filtered_latest["stock_risk_flag"])).sum()),
                int((~filtered_latest["stock_risk_flag"]).sum())
            ]
        })
        
        fig_pie = px.pie(
            status_counts, 
            values='Count', 
            names='Status',
            color='Status',
            color_discrete_map={
                'Critical Stockout': COLORS['danger'],
                'Warning Level': COLORS['warning'],
                'Adequate Supply': COLORS['success']
            },
            hole=0.5
        )
        fig_pie.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            textfont_size=11
        )
        fig_pie.update_layout(
            height=400, 
            showlegend=True,
            paper_bgcolor='white',
            plot_bgcolor='white',
            font=dict(family='Inter', size=11),
            legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.1)
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.markdown("**Days of Therapy Remaining Distribution**")
        fig_box = px.box(
            filtered_latest[filtered_latest["days_of_therapy_left"].notna()],
            y="days_of_therapy_left",
            x="LOCATION",
            color="LOCATION",
            labels={"days_of_therapy_left": "Days Remaining", "LOCATION": "Province"}
        )
        fig_box.update_layout(
            height=400,
            showlegend=False,
            yaxis_title="Days of Therapy Supply",
            xaxis_title="",
            paper_bgcolor='white',
            plot_bgcolor='white',
            font=dict(family='Inter', size=11)
        )
        fig_box.update_xaxes(tickangle=45)
        st.plotly_chart(fig_box, use_container_width=True)

# --------- TAB 2: Critical Alerts ---------
with tab2:
    st.markdown('<h2 class="section-header">Critical Stock Alerts and Procurement Recommendations</h2>', unsafe_allow_html=True)
    
    alerts = filtered_latest[filtered_latest["days_until_stockout_vs_lead"] < 0].sort_values(
        "days_until_stockout_vs_lead"
    )
    
    if alerts.empty:
        st.markdown("""
        <div class="alert alert-success">
            <div class="alert-title">All Stock Levels Adequate</div>
            <div class="alert-content">
                <p>Comprehensive analysis indicates that all inventory levels across monitored provinces and regimens are sufficient relative to procurement lead times and current patient demand. No immediate procurement action is required at this time.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="alert alert-critical">
            <div class="alert-title">CRITICAL ALERT: {len(alerts)} Items Require Immediate Procurement Action</div>
            <div class="alert-content">
                <p>The following pharmaceutical inventory items will exhaust available stock before the next scheduled delivery arrives. Immediate emergency procurement procedures must be initiated to prevent treatment interruptions.</p>
            </div>
            <div class="alert-metrics">
                <div class="alert-metric">
                    <div class="alert-metric-label">Critical Items</div>
                    <div class="alert-metric-value">{len(alerts)}</div>
                </div>
                <div class="alert-metric">
                    <div class="alert-metric-label">Provinces Affected</div>
                    <div class="alert-metric-value">{alerts['LOCATION'].nunique()}</div>
                </div>
                <div class="alert-metric">
                    <div class="alert-metric-label">Patients at Risk</div>
                    <div class="alert-metric-value">{int(alerts['TB_CASES_ACTIVE'].sum()):,}</div>
                </div>
                <div class="alert-metric">
                    <div class="alert-metric-label">Avg Shortfall</div>
                    <div class="alert-metric-value">{abs(alerts['days_until_stockout_vs_lead'].mean()):.1f} days</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Detailed alert cards
        for idx, r in alerts.iterrows():
            days_short = abs(r['days_until_stockout_vs_lead'])
            severity_label = "CRITICAL" if days_short > 7 else "URGENT"
            severity_class = "alert-critical" if days_short > 7 else "alert-warning"
            
            st.markdown(f"""
            <div class="alert {severity_class}">
                <div class="alert-title">{severity_label}: {r['LOCATION']} — {r['ITEM']}</div>
                <div class="alert-content">
                    <p><strong>Stock Exhaustion Forecast:</strong> {days_short:.1f} days before next scheduled delivery</p>
                </div>
                <div class="alert-metrics">
                    <div class="alert-metric">
                        <div class="alert-metric-label">Current Stock</div>
                        <div class="alert-metric-value">{int(r['CLOSING_STOCK'])} units</div>
                    </div>
                    <div class="alert-metric">
                        <div class="alert-metric-label">Active Patients</div>
                        <div class="alert-metric-value">{int(r['TB_CASES_ACTIVE'])}</div>
                    </div>
                    <div class="alert-metric">
                        <div class="alert-metric-label">Days Supply Left</div>
                        <div class="alert-metric-value">{r['days_of_therapy_left']:.1f} days</div>
                    </div>
                    <div class="alert-metric">
                        <div class="alert-metric-label">Lead Time</div>
                        <div class="alert-metric-value">{int(r['LEAD_TIME_DAYS'])} days</div>
                    </div>
                    <div class="alert-metric">
                        <div class="alert-metric-label">TB Risk Score</div>
                        <div class="alert-metric-value">{r['TB_RISK_SCORE']:.1f} / 10</div>
                    </div>
                    <div class="alert-metric">
                        <div class="alert-metric-label">Recommended Order</div>
                        <div class="alert-metric-value">{int(r['suggested_reorder_qty'])} units</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("**Comprehensive Alert Data Table**")
        st.caption("Complete dataset for procurement planning and emergency response coordination")
        
        alert_export = alerts[[
            "LOCATION", "ITEM", "CLOSING_STOCK", "TB_CASES_ACTIVE",
            "LEAD_TIME_DAYS", "days_of_therapy_left", "days_until_stockout_vs_lead",
            "TB_RISK_SCORE", "programmatic_risk", "suggested_reorder_qty"
        ]].copy()
        
        alert_export.columns = [
            "Province", "Treatment Regimen", "Current Stock", "Active Cases",
            "Lead Time (Days)", "Supply Days Left", "Shortfall (Days)",
            "TB Risk Score", "Programmatic Risk", "Recommended Order Quantity"
        ]
        
        st.dataframe(alert_export, use_container_width=True, height=400)
        
        # Download functionality
        csv = alert_export.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Priority Procurement List (CSV)",
            data=csv,
            file_name=f"tb_critical_procurement_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv",
            help="Export comprehensive alert data for procurement teams and supply chain management"
        )
    
    # Warning items section
    st.markdown("**Items Approaching Critical Threshold**")
    st.caption("Monitor these items closely for potential stockout risk in the near future")
    
    warnings = filtered_latest[
        (filtered_latest["days_until_stockout_vs_lead"] >= 0) & 
        (filtered_latest["stock_risk_flag"])
    ].sort_values("days_of_therapy_left")
    
    if not warnings.empty:
        for idx, r in warnings.head(10).iterrows():
            st.markdown(f"""
            <div class="alert alert-warning">
                <div class="alert-content">
                    <strong>{r['LOCATION']} — {r['ITEM']}</strong><br>
                    Supply remaining: {r['days_of_therapy_left']:.1f} days | 
                    Lead time: {int(r['LEAD_TIME_DAYS'])} days | 
                    Active cases: {int(r['TB_CASES_ACTIVE'])} | 
                    Recommended order: {int(r['suggested_reorder_qty'])} units
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No items currently in warning threshold range")

# --------- TAB 3: Care Cascade ---------
with tab3:
    st.markdown('<h2 class="section-header">Treatment Cascade Time Analysis</h2>', unsafe_allow_html=True)
    
    cascade_df = cascade_df.copy()
    cascade_df["total_delay_days"] = (
        cascade_df["MEDIAN_PATIENT_DELAY_DAYS"]
        + cascade_df["MEDIAN_DIAGNOSTIC_DELAY_DAYS"]
        + cascade_df["MEDIAN_TREATMENT_DELAY_DAYS"]
    )
    
    st.markdown("""
    <div class="info-box">
        <div class="info-box-title">Care Cascade Metrics Overview</div>
        <p>The care cascade represents the temporal progression from symptom onset to treatment initiation. Each stage contributes to the total delay, which directly impacts patient outcomes and disease transmission rates in communities.</p>
        <p><strong>Clinical Significance:</strong> Reduced cascade delays improve treatment success rates and minimize community transmission risk.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stacked bar visualization
    fig_cascade = go.Figure()
    
    fig_cascade.add_trace(go.Bar(
        x=cascade_df["LOCATION"],
        y=cascade_df["MEDIAN_PATIENT_DELAY_DAYS"],
        name="Patient Delay",
        marker_color=COLORS['primary'],
        hovertemplate='<b>%{x}</b><br>Patient Delay: %{y:.1f} days<extra></extra>'
    ))
    
    fig_cascade.add_trace(go.Bar(
        x=cascade_df["LOCATION"],
        y=cascade_df["MEDIAN_DIAGNOSTIC_DELAY_DAYS"],
        name="Diagnostic Delay",
        marker_color=COLORS['secondary'],
        hovertemplate='<b>%{x}</b><br>Diagnostic Delay: %{y:.1f} days<extra></extra>'
    ))
    
    fig_cascade.add_trace(go.Bar(
        x=cascade_df["LOCATION"],
        y=cascade_df["MEDIAN_TREATMENT_DELAY_DAYS"],
        name="Treatment Initiation Delay",
        marker_color=COLORS['warning'],
        hovertemplate='<b>%{x}</b><br>Treatment Delay: %{y:.1f} days<extra></extra>'
    ))
    
    fig_cascade.update_layout(
        barmode='stack',
        xaxis_title="Province",
        yaxis_title="Delay Duration (Days)",
        height=500,
        title={
            'text': "Care Cascade Delay Composition by Province",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': COLORS['primary'], 'family': 'Inter'}
        },
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        ),
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(family='Inter', size=11)
    )
    
    fig_cascade.update_xaxes(tickangle=45)
    
    st.plotly_chart(fig_cascade, use_container_width=True)
    
    # Analytics columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Provincial Delay Statistics**")
        cascade_display = cascade_df[[
            "LOCATION", "MEDIAN_PATIENT_DELAY_DAYS", 
            "MEDIAN_DIAGNOSTIC_DELAY_DAYS", "MEDIAN_TREATMENT_DELAY_DAYS",
            "total_delay_days"
        ]].copy()
        
        cascade_display.columns = [
            "Province", "Patient Delay (Days)", "Diagnostic Delay (Days)", 
            "Treatment Delay (Days)", "Total Delay (Days)"
        ]
        
        st.dataframe(cascade_display, use_container_width=True, height=400)
    
    with col2:
        st.markdown("**National Average Delays by Stage**")
        avg_delays = pd.DataFrame({
            'Cascade Stage': ['Patient Delay', 'Diagnostic Delay', 'Treatment Initiation'],
            'Average Duration (Days)': [
                cascade_df["MEDIAN_PATIENT_DELAY_DAYS"].mean(),
                cascade_df["MEDIAN_DIAGNOSTIC_DELAY_DAYS"].mean(),
                cascade_df["MEDIAN_TREATMENT_DELAY_DAYS"].mean()
            ]
        })
        
        fig_avg = px.bar(
            avg_delays,
            x='Cascade Stage',
            y='Average Duration (Days)',
            color='Cascade Stage',
            color_discrete_sequence=[COLORS['primary'], COLORS['secondary'], COLORS['warning']],
            text='Average Duration (Days)'
        )
        fig_avg.update_traces(texttemplate='%{text:.1f}', textposition='outside')
        fig_avg.update_layout(
            height=350, 
            showlegend=False,
            paper_bgcolor='white',
            plot_bgcolor='white',
            font=dict(family='Inter', size=11)
        )
        st.plotly_chart(fig_avg, use_container_width=True)
        
        # Summary statistics
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-title">National Care Cascade Summary</div>
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-label">Mean Total Delay</div>
                    <div class="stat-value">{cascade_df['total_delay_days'].mean():.1f}</div>
                </div>
                <div class="stat-item">
                    <div class="stat-label">Median Total Delay</div>
                    <div class="stat-value">{cascade_df['total_delay_days'].median():.1f}</div>
                </div>
                <div class="stat-item">
                    <div class="stat-label">Minimum Delay</div>
                    <div class="stat-value">{cascade_df['total_delay_days'].min():.1f}</div>
                </div>
                <div class="stat-item">
                    <div class="stat-label">Maximum Delay</div>
                    <div class="stat-value">{cascade_df['total_delay_days'].max():.1f}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --------- TAB 4: Provider Network ---------
with tab4:
    st.markdown('<h2 class="section-header">Healthcare Provider Network Analysis</h2>', unsafe_allow_html=True)
    
    prov_summary = prov_df.groupby("LOCATION").agg(
        facilities=("FACILITY_ID", "nunique"),
        total_doctors=("DOCTOR_COUNT", "sum")
    ).reset_index()
    
    prov_with_cases = prov_summary.merge(
        latest.groupby("LOCATION")["TB_CASES_ACTIVE"].sum().reset_index(),
        on="LOCATION",
        how="left"
    )
    prov_with_cases["patients_per_doctor"] = (
        prov_with_cases["TB_CASES_ACTIVE"] / prov_with_cases["total_doctors"]
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Healthcare Infrastructure Distribution**")
        fig_providers = go.Figure()
        fig_providers.add_trace(go.Bar(
            x=prov_with_cases["LOCATION"],
            y=prov_with_cases["facilities"],
            name="Healthcare Facilities",
            marker_color=COLORS['primary']
        ))
        fig_providers.add_trace(go.Bar(
            x=prov_with_cases["LOCATION"],
            y=prov_with_cases["total_doctors"],
            name="Medical Practitioners",
            marker_color=COLORS['success']
        ))
        fig_providers.update_layout(
            barmode='group',
            height=400,
            xaxis_title="Province",
            yaxis_title="Count",
            paper_bgcolor='white',
            plot_bgcolor='white',
            font=dict(family='Inter', size=11),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
        )
        fig_providers.update_xaxes(tickangle=45)
        st.plotly_chart(fig_providers, use_container_width=True)
    
    with col2:
        st.markdown("**Patient-to-Doctor Ratio Analysis**")
        fig_ratio = px.bar(
            prov_with_cases,
            x="LOCATION",
            y="patients_per_doctor",
            color="patients_per_doctor",
            color_continuous_scale=[[0, COLORS['success']], [1, COLORS['danger']]],
            labels={"patients_per_doctor": "Ratio", "LOCATION": "Province"}
        )
        fig_ratio.update_layout(
            height=400,
            showlegend=False,
            paper_bgcolor='white',
            plot_bgcolor='white',
            font=dict(family='Inter', size=11),
            yaxis_title="Patients per Doctor"
        )
        fig_ratio.update_xaxes(tickangle=45)
        st.plotly_chart(fig_ratio, use_container_width=True)
    
    st.markdown("**Provincial Healthcare Capacity Summary**")
    prov_with_cases.columns = ["Province", "Healthcare Facilities", "Medical Practitioners", "Active TB Patients", "Patient-Doctor Ratio"]
    st.dataframe(prov_with_cases, use_container_width=True, height=350)
    
    st.markdown("---")
    st.markdown("**Detailed Facility Directory and Incentive Programs**")
    st.caption("Comprehensive listing of TB treatment facilities and performance-based compensation structures")
    
    facility_display = prov_df[[
        "FACILITY_NAME", "LOCATION", "DOCTOR_COUNT", "INCENTIVE_SCHEME"
    ]].copy()
    facility_display.columns = ["Facility Name", "Province", "Medical Practitioners", "Incentive Program"]
    
    st.dataframe(facility_display, use_container_width=True, height=400)

# --------- TAB 5: Distribution Network ---------
with tab5:
    st.markdown('<h2 class="section-header">Pharmaceutical Distribution Network</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <div class="info-box-title">National Distribution Infrastructure</div>
        <p>Strategic depot locations form the backbone of Indonesia's TB pharmaceutical supply chain, managing inventory flow from central procurement to provincial healthcare facilities.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if 'LATITUDE' in depots_df.columns and 'LONGITUDE' in depots_df.columns:
        st.markdown("**Geographic Distribution of Pharmaceutical Depots**")
        
        fig_map = px.scatter_mapbox(
            depots_df,
            lat="LATITUDE",
            lon="LONGITUDE",
            hover_name="DEPOT_NAME",
            hover_data={"LOCATION": True, "REGION": True, "STOCK_LEVEL": True, "LATITUDE": False, "LONGITUDE": False},
            color="STOCK_LEVEL",
            size="STOCK_LEVEL",
            color_continuous_scale=[[0, COLORS['danger']], [0.5, COLORS['warning']], [1, COLORS['success']]],
            zoom=4,
            height=600
        )
        fig_map.update_layout(
            mapbox_style="open-street-map",
            paper_bgcolor='white',
            font=dict(family='Inter', size=11)
        )
        st.plotly_chart(fig_map, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Depot Inventory Levels**")
        fig_depot_stock = px.bar(
            depots_df.sort_values("STOCK_LEVEL", ascending=False),
            x="DEPOT_NAME",
            y="STOCK_LEVEL",
            color="REGION",
            labels={"STOCK_LEVEL": "Inventory Level (Units)", "DEPOT_NAME": "Depot Facility"}
        )
        fig_depot_stock.update_layout(
            height=400,
            paper_bgcolor='white',
            plot_bgcolor='white',
            font=dict(family='Inter', size=11)
        )
        fig_depot_stock.update_xaxes(tickangle=45)
        st.plotly_chart(fig_depot_stock, use_container_width=True)
    
    with col2:
        st.markdown("**Regional Distribution Analysis**")
        regional_stats = depots_df.groupby("REGION").agg({
            "DEPOT_ID": "count",
            "STOCK_LEVEL": "sum"
        }).reset_index()
        regional_stats.columns = ["Region", "Number of Depots", "Total Inventory"]
        
        fig_regional = px.pie(
            regional_stats,
            values="Number of Depots",
            names="Region",
            hole=0.5
        )
        fig_regional.update_traces(textposition='inside', textinfo='percent+label')
        fig_regional.update_layout(
            height=400,
            paper_bgcolor='white',
            font=dict(family='Inter', size=11)
        )
        st.plotly_chart(fig_regional, use_container_width=True)
    
    st.markdown("**Complete Depot Directory**")
    st.dataframe(depots_df, use_container_width=True, height=350)

# --------- Footer ---------
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 2.5rem 1rem; background: white; border-radius: 12px; margin-top: 3rem;">
    <p style="font-size: 1.1rem; font-weight: 600; color: #1e40af; margin-bottom: 0.5rem;">TB CareMap Indonesia</p>
    <p style="font-size: 0.9rem; margin: 0.25rem 0;">National Tuberculosis Inventory Management System</p>
    <p style="font-size: 0.85rem; color: #94a3b8; margin-top: 1rem;">
        Powered by Snowflake Data Cloud Platform • Built with Streamlit Framework
    </p>
    <p style="font-size: 0.8rem; color: #cbd5e1; margin-top: 0.75rem;">
        Note: All displayed data is synthetic and generated for demonstration and educational purposes only
    </p>
</div>
""", unsafe_allow_html=True)