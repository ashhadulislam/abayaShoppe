import streamlit as st
import os


st.set_page_config(layout="wide")

# -------------------------
# CSS
# -------------------------

st.markdown("""
<style>

.product-card {
    position: relative;
    overflow: hidden;
    border-radius: 12px;
}

.product-card img,
.product-card video {
    width: 100%;
    border-radius: 12px;
}

/* SOLD badge */

.sold-overlay {
    position: absolute;
    top: 10px;
    left: 10px;
    background: #c0392b;
    color: white;
    padding: 6px 12px;
    font-weight: bold;
    font-size: 13px;
    border-radius: 6px;
    z-index: 3;
}

/* bottom gradient overlay */

.card-overlay {
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 15px;
    background: linear-gradient(
        transparent,
        rgba(0,0,0,0.75)
    );
    color: white;
}

/* variant title */

.variant-title {
    font-weight: bold;
    font-size: 15px;
}

/* hover button */

.hover-button {
    margin-top: 8px;
    display: none;
}

.product-card:hover .hover-button {
    display: block;
}

.whatsapp-btn {
    background-color: #25D366;
    color: white;
    padding: 6px 12px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: bold;
    font-size: 13px;
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
        "Desert Elegance",
        "Hyderabadi",
        
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
'imp001_1','zoom001_1','mlb003_1','tktk001_1', 
'blk003_2', 'minto001_4'
]


style_info_Desert_Elegance = {

    "uae002": {
        "name": "Midnight Blue Luxe Abaya",
        "desc": "Deep midnight blue abaya with subtle shimmer detailing and fine gold piping along the edges. Elegant and refined, ideal for evening or formal wear. Sizes available: S, M, L, XL."
    },

    "uae001": {
        "name": "Rose Blush Flow Abaya",
        "desc": "Soft blush pink abaya with flowing draped sleeves, paired with a rich maroon hijab. Comes with a matching niqab for a complete modest look. Sizes available: S, M, L, XL."
    },

    "uae003": {
        "name": "Charcoal Grey Modern Abaya",
        "desc": "Sophisticated charcoal grey abaya with a contemporary layered look and subtle floral texture. Minimal and modern for everyday elegance. Sizes available: S, M, L, XL."
    },

    "uae004": {
        "name": "Sand Beige Embroidered Abaya",
        "desc": "Light sand beige abaya with delicate blue embroidery on the sleeves, offering a refined and graceful appearance. Sizes available: S, M, L, XL."
    },

    "uae005": {
        "name": "Desert Brown Heritage Abaya",
        "desc": "Warm brown abaya featuring intricate golden embroidery on the sleeves. Rich earthy tones inspired by traditional desert elegance. Sizes available: S, M, L, XL."
    },

    "uae006": {
        "name": "Ivory Pearl Classic Abaya",
        "desc": "Soft ivory abaya with subtle feather-like patterning and matching cream hijab. Light, graceful and timeless. Sizes available: S, M, L, XL."
    }

}

sold_out_Desert_Elegance = []

prices_Desert_Elegance = {
    "uae001": 2500,
    "uae002": 2500,
    "uae003": 2000,
    "uae004": 2000,
    "uae005": 2000,
    "uae006": 2000,    
}

# -------------------------
# Build Catalog
# -------------------------

@st.cache_data
def build_catalog(IMAGE_FOLDER):

    catalog = {}

    image_ext = (".png", ".jpg", ".jpeg", ".webp")
    video_ext = (".mp4", ".mov", ".webm")

    files = os.listdir(IMAGE_FOLDER)
    files.sort(reverse=True)

    for f in files:
        ext = os.path.splitext(f)[1].lower()
        print(ext)

        if ext not in image_ext and ext not in video_ext:
            continue

        name = os.path.splitext(f)[0]
        parts = name.split("_")

        if len(parts) == 3:

            design = parts[0]   # example: uae_001
            item = parts[1]

            catalog.setdefault(design, {})
            catalog[design].setdefault(item, [])

            media_type = "video" if ext in video_ext else "image"

            catalog[design][item].append({
                "file": f,
                "type": media_type
            })

    return catalog


def render_collection(
    title,
    intro_text,
    image_folder,
    style_info,
    prices,
    sold_out
):

    st.title(title)
    if intro_text:
        st.write(intro_text)

    catalog = build_catalog(image_folder)
    print(f'catalog is {catalog}')

    for design in catalog.keys():
        

        #st.markdown("---")

        info = style_info.get(design, {})
        name = info.get("name", design.upper())
        description = info.get("desc", "")
        print(design,description)
        price = prices.get(design, "N/A")
        
        items = sorted(catalog[design].keys())

        valid_items = [
            item for item in items
            if f"{design}_{item}" not in sold_out
        ]

        if not valid_items:
            continue

        for item_idx, item in enumerate(valid_items):


            variant_id = f"{design}_{item}"
            is_sold = variant_id in sold_out
            if is_sold:
                continue

            if item_idx==0:
                st.header(name)
                st.write(description)        
                st.subheader(f"₹ {price}")

            st.markdown(f"### Variant {item}")

            media_files = catalog[design][item]

            

            if not is_sold:
                whatsapp_url = (
                    f"https://wa.me/916291426885?text="
                    f"Hi%20I%20am%20interested%20in%20{name}%20Variant%20{item}"
                )

                st.markdown(
                    f"""
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
                    """,
                    unsafe_allow_html=True
                )


            for i, media in enumerate(media_files):

                if i % 4 == 0:
                    cols = st.columns(4)

                with cols[i % 4]:

                    path = os.path.join(image_folder, media["file"])

                    st.markdown('<div class="product-card">', unsafe_allow_html=True)

                    if is_sold:
                        st.markdown('<div class="sold-overlay">SOLD OUT</div>', unsafe_allow_html=True)

                    if media["type"] == "image":
                        st.image(path, use_container_width=True)

                    elif media["type"] == "video":
                        st.video(path)

                    if not is_sold:
                        whatsapp_url = (
                            f"https://wa.me/916291426885?text="
                            f"Hi%20I%20am%20interested%20in%20{name}%20Variant%20{item}"
                        )

                        st.markdown(f"""
                        <div class="card-overlay">
                            <div class="variant-title">Variant {item}</div>
                            <div class="hover-button">
                                <a href="{whatsapp_url}" target="_blank" class="whatsapp-btn">
                                    Order on WhatsApp
                                </a>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                    else:
                        st.markdown(f"""
                        <div class="card-overlay">
                            <div class="variant-title">Variant {item}</div>
                        </div>
                        """, unsafe_allow_html=True)

                    st.markdown('</div>', unsafe_allow_html=True)
# -------------------------
# PAGE 1 : HYDERABADI
# -------------------------

if page == "Hyderabadi":
    render_collection(
        title="Hyderabadi Collection",
        intro_text="Traditional silhouettes inspired by Hyderabadi elegance.",
        image_folder="AbayaThumbs/Hyderabadi",
        style_info=style_info_Hyderabadi,
        prices=prices_Hyderabadi,
        sold_out=sold_out_Hyderabadi
    )


# -------------------------
# PAGE 2 : UAE
# -------------------------

elif page == "Desert Elegance":
     render_collection(
        title="Desert Elegance Collection",
        intro_text="""
        Inspired by Gulf elegance and flowing silhouettes.
        Premium fabrics and statement abayas.
        """,
        image_folder="AbayaThumbs/DesertElegance",
        style_info=style_info_Desert_Elegance,
        prices=prices_Desert_Elegance,
        sold_out=sold_out_Desert_Elegance
    )