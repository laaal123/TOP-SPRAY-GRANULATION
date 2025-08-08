
import streamlit as st

st.set_page_config(page_title="Top Spray Granulation Scale-Up Tool", layout="wide")

st.title("🔬 Top Spray Granulation Scale-Up Calculator")
st.markdown("Input your small-scale parameters and desired batch size. This tool will auto-suggest optimized parameters for scale-up.")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    small_batch = st.number_input("Small Scale Batch Size (kg)", min_value=1.0, value=240.0, step=10.0)
    spray_rate = st.number_input("Spray Rate (g/min)", min_value=100.0, value=600.0, step=10.0)
    atom_pressure = st.number_input("Atomization Pressure (bar)", min_value=0.5, value=1.0, step=0.1)
    air_volume = st.number_input("Air Volume (CFM)", min_value=200.0, value=650.0, step=10.0)
with col2:
    nozzles = st.number_input("No. of Spray Nozzles", min_value=1, value=4, step=1)
    inlet_temp = st.number_input("Inlet Air Temp during Spray (°C)", min_value=40, value=65, step=1)
    product_temp = st.number_input("Product Temperature (°C)", min_value=25, value=38, step=1)
    target_batch = st.number_input("Target Scale-Up Batch Size (kg)", min_value=10.0, value=360.0, step=10.0)

# Calculations
scale_factor = target_batch / small_batch
opt_spray_rate = spray_rate * scale_factor
opt_atom_pressure = min(round(atom_pressure + 0.3, 2), 1.5)
opt_air_volume = air_volume * scale_factor
opt_nozzles = max(nozzles + 1, 5)

# Output
st.markdown("## 🧮 Scale-Up Results")
st.write(f"**Scale-Up Factor:** {scale_factor:.2f}×")

st.success("### Recommended Parameters for Target Scale-Up")
st.write(f"- **Spray Rate:** {opt_spray_rate:.0f} g/min")
st.write(f"- **Atomization Pressure:** {opt_atom_pressure} bar")
st.write(f"- **Air Volume:** {opt_air_volume:.0f} CFM")
st.write(f"- **No. of Spray Nozzles:** {opt_nozzles}")
st.write(f"- **Inlet Air Temp:** {inlet_temp} °C")
st.write(f"- **Product Temperature:** {product_temp} °C")
st.write(f"- **Expected Drying Time:** {int(60 * scale_factor)} min (est.)")
st.write(f"- **Target LOD Post Drying:** ≤ 3.3%")
