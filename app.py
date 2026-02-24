import streamlit as st
import os
from collections import defaultdict

IMAGE_FOLDER = "AbayaThumbs"
st.set_page_config(layout="wide")

# -------------------------
# Prices Dictionary
# -------------------------
prices = {
    "minto001": 1920,
    "mlb001": 2250,
    "cy001": 2175,
    "cnida001": 3075,
    "zoom001": 2325,
    "bnida001": 2775,
    "cnida002": 2475,
    "slf001": 2325,
    "tktk001": 2400,
    "imp001": 4125,
    "mlb002": 2475,
    "mlb003": 2475,
    "blk001": 2550,
    "blk002": 3600,
    "blk003": 2775,
}

style_info = {
    "minto001": {
        "name": "Mint Coat Abaya",
        "desc": "Structured coat-style abaya with a modern silhouette. Perfect for elevated everyday wear."
    },
    "mlb001": {
        "name": "Malbara Essential",
        "desc": "Crafted in premium Malbara fabric, offering a smooth flow and refined elegance."
    },
    "mlb002": {
        "name": "Malbara Classic",
        "desc": "Soft Malbara fabric with graceful drape. Lightweight and ideal for daily sophistication."
    },
    "mlb003": {
        "name": "Malbara Self Design",
        "desc": "Malbara fabric with subtle self-print texture for understated elegance."
    },
    "cy001": {
        "name": "Crushed Silk Flow",
        "desc": "Crushed-texture fabric that adds movement and dimension to a timeless abaya silhouette."
    },
    "cnida001": {
        "name": "Korean Nida Premium",
        "desc": "High-quality Korean Nida fabric known for its wrinkle-free finish and smooth luxurious feel."
    },
    "cnida002": {
        "name": "Korean Nida Signature",
        "desc": "An elegant variation of Korean Nida with structured fall and refined detailing."
    },
    "bnida001": {
        "name": "Black Korean Nida",
        "desc": "Classic black abaya in premium Korean Nida fabric. Smooth, structured and graceful."
    },
    "zoom001": {
        "name": "Zoom Style Abaya",
        "desc": "Modern cut with contemporary detailing, designed for confident modest wear."
    },
    "slf001": {
        "name": "Self Design Abaya",
        "desc": "Elegant self-textured fabric that adds subtle design without overpowering simplicity."
    },
    "tktk001": {
        "name": "Stone Detail Abaya",
        "desc": "Statement abaya featuring delicate stone embellishments for festive occasions."
    },
    "imp001": {
        "name": "UAE Imported Luxury",
        "desc": "Premium imported abaya with superior craftsmanship and elegant finishing."
    },
    "blk001": {
        "name": "Black Koti Style",
        "desc": "Layered koti-style abaya combining structure and modest sophistication."
    },
    "blk002": {
        "name": "Black Statement Edition",
        "desc": "Bold black abaya with modern logo-inspired detailing."
    },
    "blk003": {
        "name": "Black Handwork Abaya",
        "desc": "Handworked detailing on classic black fabric for refined festive elegance."
    },
}

# -------------------------
# Build Catalog
# -------------------------
@st.cache_data
def build_catalog():
    catalog = {}

    files = os.listdir(IMAGE_FOLDER)
    files.sort(reverse=True)

    for f in files:
        if not f.endswith(".png"):
            continue
        
        name = f.replace(".png", "")
        parts = name.split("_")

        if len(parts) == 3:
            design = parts[0]
            item = parts[1]

            if design not in catalog:
                catalog[design] = {}

            if item not in catalog[design]:
                catalog[design][item] = []

            catalog[design][item].append(f)

    return catalog

catalog = build_catalog()

# -------------------------
# UI
# -------------------------




st.title("Abaya Collection")

#for design in sorted(catalog.keys()):
for design in catalog.keys():    
    
    st.markdown("---")

    info = style_info.get(design, {})
    title = info.get("name", design.upper())
    description = info.get("desc", "")

    st.header(title)
    st.write(description)

    price = prices.get(design, "N/A")
    st.subheader(f"₹ {price}")

    items = sorted(catalog[design].keys())

    for item in items:
        st.markdown(f"### Variant {item}")

        images = sorted(catalog[design][item])

        cols = st.columns(4)
        for i, img in enumerate(images):
            with cols[i % 4]:
                st.image(
                    os.path.join(IMAGE_FOLDER, img),
                    use_container_width=True
                )