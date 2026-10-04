"""Revenue per available bed and gap decomposition vs Max. Run from repo root: python analysis/analysis.py"""
import pandas as pd, matplotlib.pyplot as plt
df = pd.read_csv("data/peer_data.csv")
full = df.dropna(subset=["arpob_rs_per_day", "occupancy"]).copy()      # cleaning: keep chains with both metrics
full["rev_per_bed_lakh"] = full.arpob_rs_per_day * full.occupancy * 365 / 1e5
ref = full[full.chain == "Max Healthcare"].iloc[0]
full["gap_vs_max"] = full.rev_per_bed_lakh - ref.rev_per_bed_lakh
full["price_effect"] = (full.arpob_rs_per_day - ref.arpob_rs_per_day) * ref.occupancy * 365 / 1e5
full["occ_effect"] = (full.occupancy - ref.occupancy) * full.arpob_rs_per_day * 365 / 1e5
assert ((full.price_effect + full.occ_effect - full.gap_vs_max).abs() < 1e-6).all()   # decomposition is exact
peers = full[full.chain != "Max Healthcare"].copy()
peers["price_share"] = peers.price_effect / peers.gap_vs_max
print(full[["chain", "rev_per_bed_lakh"]].round(1).to_string(index=False))
print(peers[["chain", "gap_vs_max", "price_effect", "occ_effect", "price_share"]].round(2).to_string(index=False))
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.barh(full.chain, full.rev_per_bed_lakh, color="#0E6B6F")
for y, v in enumerate(full.rev_per_bed_lakh): ax.text(v + 2, y, f"{v:.0f}", va="center")
ax.set_xlabel("Revenue per available bed, Rs lakh per year (ARPOB x occupancy x 365)")
ax.set_title("FY26 revenue per available bed"); ax.invert_yaxis(); plt.tight_layout()
plt.savefig("charts/revenue_per_bed.png", dpi=150)
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.barh(peers.chain, -peers.price_effect, label="Price / case mix", color="#0E6B6F")
ax.barh(peers.chain, -peers.occ_effect, left=-peers.price_effect, label="Occupancy", color="#E9A36B")
ax.set_xlabel("Revenue-per-bed shortfall vs Max, Rs lakh per year"); ax.set_title("Where the gap to Max comes from")
ax.legend(); ax.invert_yaxis(); plt.tight_layout(); plt.savefig("charts/gap_decomposition.png", dpi=150)
