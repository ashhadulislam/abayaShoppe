import streamlit as st
import os

IMAGE_FOLDER = "AbayaThumbs"

st.set_page_config(layout="wide")

# -------------------------
# CSS
# -------------------------

st.markdown("""
<style>
.product-card {
    position: relative;
}

.sold-overlay {
    position: absolute;
    top: 10px;
    left: 10px;
    background: #c0392b;
    color: white;
    padding: 6px 12px;
    font-weight: bold;
    font-size: 14px;
    border-radius: 6px;
}
</style>
""", unsafe_allow_html=True)


# -------------------------
# Sidebar Navigation
# -------------------------

st.sidebar.title("Musfira")

page = st.sidebar.radio(
    "Collections",
    [
        "Hyderabadi",
        "Desert Elegance"
    ]
)

# -------------------------
# prices_Hyderabadi
# -------------------------

prices_Hyderabadi = {
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

# -------------------------
# Style Info
# -------------------------

style_info_Hyderabadi = {
    "minto001": {"name": "Mint Coat Abaya","desc": "Structured coat-style abaya with a modern silhouette."},
    "mlb001": {"name": "Malbara Essential","desc": "Crafted in premium Malbara fabric."},
    "mlb002": {"name": "Malbara Classic","desc": "Soft Malbara fabric with graceful drape."},
    "mlb003": {"name": "Malbara Self Design","desc": "Malbara fabric with subtle self-print texture."},
    "cy001": {"name": "Crushed Silk Flow","desc": "Crushed-texture fabric with movement."},
    "cnida001": {"name": "Korean Nida Premium","desc": "Wrinkle-free Korean Nida fabric."},
    "cnida002": {"name": "Korean Nida Signature","desc": "Elegant variation of Korean Nida."},
    "bnida001": {"name": "Black Korean Nida","desc": "Classic black Korean Nida abaya."},
    "zoom001": {"name": "Zoom Style Abaya","desc": "Modern cut with contemporary detailing."},
    "slf001": {"name": "Self Design Abaya","desc": "Elegant self-textured fabric."},
    "tktk001": {"name": "Stone Detail Abaya","desc": "Stone embellished festive abaya."},
    "imp001": {"name": "UAE Imported Luxury","desc": "Premium imported abaya."},
    "blk001": {"name": "Black Koti Style","desc": "Layered koti style abaya."},
    "blk002": {"name": "Black Statement Edition","desc": "Modern logo inspired detailing."},
    "blk003": {"name": "Black Handwork Abaya","desc": "Handworked festive elegance."},
}

sold_out_Hyderabadi = [
'minto001_1','minto001_2','cnida001_2','cy001_2',
'imp001_1','zoom001_1','mlb003_1','tktk001_1'
]


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
        
        name = f.replace(".png","")
        parts = name.split("_")

        if len(parts) == 3:

            design = parts[0]
            item = parts[1]

            catalog.setdefault(design,{})
            catalog[design].setdefault(item,[])
            catalog[design][item].append(f)

    return catalog


catalog = build_catalog()

# -------------------------
# PAGE 1 : HYDERABADI
# -------------------------

if page == "Hyderabadi":
    IMAGE_FOLDER = "AbayaThumbs/Hyderabadi"

    st.title("Hyderabadi Collection")
    st.write("Traditional silhouettes inspired by Hyderabadi elegance.")

    for design in catalog.keys():

        st.markdown("---")

        info = style_info_Hyderabadi.get(design,{})
        title = info.get("name",design.upper())
        description = info.get("desc","")

        st.header(title)
        st.write(description)

        price = prices_Hyderabadi.get(design,"N/A")
        st.subheader(f"₹ {price}")

        items = sorted(catalog[design].keys())

        for item in items:

            st.markdown(f"### Variant {item}")

            images = sorted(catalog[design][item])

            variant_id = f"{design}_{item}"
            is_sold = variant_id in sold_out_Hyderabadi

            if not is_sold:

                whatsapp_url = f"https://wa.me/916291426885?text=Hi%20I%20am%20interested%20in%20{title}%20Variant%20{item}"

                st.markdown(f"""
                <a href="{whatsapp_url}" target="_blank">
                <button style="
                background-color:#25D366;
                color:white;
                padding:10px 18px;
                border:none;
                border-radius:6px;
                font-weight:bold;">
                Order on WhatsApp
                </button>
                </a>
                """, unsafe_allow_html=True)

            cols = st.columns(4)

            for i,img in enumerate(images):

                with cols[i % 4]:

                    st.markdown('<div class="product-card">', unsafe_allow_html=True)

                    if is_sold:
                        st.markdown('<div class="sold-overlay">SOLD OUT</div>', unsafe_allow_html=True)

                    st.image(
                        os.path.join(IMAGE_FOLDER,img),
                        use_container_width=True
                    )

                    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------
# PAGE 2 : UAE
# -------------------------

elif page == "UAE Luxury":

    st.title("UAE Luxury Collection")

    st.write("""
    Inspired by Gulf elegance and flowing silhouettes.
    Premium fabrics and statement abayas.
    """)

    st.image(
        "https://images.unsplash.com/photo-1520975922203-b8d66c3f6f8c",
        use_container_width=True
    )

    st.info("UAE collection coming soon.")