from app_pages.property_maintenance_dashboard import dashboard_body
import streamlit as st
from app_pages.multi_page import MultiPage
# Create the multi-page Streamlit application
app = MultiPage(app_name="Property App")
# Register the Dashboard page and its body function.
app.add_page("Dashboard Test", dashboard_body)
# Start the Streamlit application.
app.run()
