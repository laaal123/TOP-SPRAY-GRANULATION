import streamlit as st

st.set_page_config(page_title="Top Spray Granulation Area-Based Scale-Up", layout="wide")

st.title("🔬 Top Spray Granulation Area-Based Scale-Up Calculator")
st.markdown("Use fluid bed area-based scaling to calculate optimal spray rate, air volume, and other critical parameters.")

# User Inputs
st.header("🔽 Small-Scale Granulation Inputs")
col1, col2 = st.columns(2)
with col1:
    small_batch = st.number_input("Small Batch Size (kg)", min_value=1.0, value=240.0, step=10.0)
    spray_rate = st.number_input("Spray Rate (g/min)", min_value=100.0, value=600.0, step=10.0)
    air_volume = st.number_input("Air Volume (CFM)", min_value=100.0, value=650.0, step=10.0)
    atom_pressure = st.number_input("Atomization Pressure (bar)", min_value=0.5, value=1.0, step=0.1)
with col2:
    small_area = st.number_input("Fluid Bed Area - Small Scale (m²)", min_value=0.1, value=1.4, step=0.1)
    nozzles = st.number_input("No. of Spray Nozzles - Small Scale", min_value=1, value=4, step=1)
    inlet_temp = st.number_input("Inlet Air Temp (°C)", min_value=30, value=65, step=1)
    product_temp = st.number_input("Product Temp (°C)", min_value=25, value=38, step=1)

st.header("🔼 Large-Scale Equipment Inputs")
col3, col4 = st.columns(2)
with col3:
    large_batch = st.number_input("Target Batch Size (kg)", min_value=10.0, value=360.0, step=10.0)
    large_area = st.number_input("Fluid Bed Area - Large Scale (m²)", min_value=0.1, value=1.88, step=0.01)
    target_nozzles = st.number_input("Planned No. of Nozzles - Large Scale", min_value=1, value=5, step=1)

# Area-based calculations
area_ratio = large_area / small_area
spray_rate_large = spray_rate * area_ratio
air_volume_large = air_volume * area_ratio
spray_rate_per_nozzle = spray_rate_large / target_nozzles
atom_pressure_large = min(round(atom_pressure + 0.3, 2), 1.5)

# Results
st.markdown("## 📈 Scale-Up Results")
st.write(f"**Area Ratio (A2/A1):** {area_ratio:.2f}")

st.success("### 🌟 Recommended Parameters for Large Scale")
st.write(f"- **Spray Rate (total):** {spray_rate_large:.0f} g/min")
st.write(f"- **Spray Rate per Nozzle:** {spray_rate_per_nozzle:.0f} g/min")
st.write(f"- **Air Volume:** {air_volume_large:.0f} CFM")
st.write(f"- **Atomization Pressure:** {atom_pressure_large:.2f} bar")
st.write(f"- **Inlet Air Temp:** {inlet_temp} °C (keep constant)")
st.write(f"- **Product Temp:** {product_temp} °C (monitor for binder activation)")



