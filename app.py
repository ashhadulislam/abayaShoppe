import streamlit as st
from pathlib import Path
import zipfile
import io

# --------------------
# Config
# --------------------
st.set_page_config(page_title="Abaya Selector", layout="wide")

IMAGES_DIR = Path("images")
IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]
SELECTION_FILE = Path("selected_images.txt")

# --------------------
# Helpers
# --------------------
def load_selections():
    if SELECTION_FILE.exists():
        return set(SELECTION_FILE.read_text().splitlines())
    return set()

def save_selections_if_changed(new_selection):
    old_selection = load_selections()
    if new_selection != old_selection:
        SELECTION_FILE.write_text("\n".join(sorted(new_selection)))

# --------------------
# Load images
# --------------------
image_files = sorted(
    [p for p in IMAGES_DIR.iterdir() if p.suffix.lower() in IMAGE_EXTENSIONS]
)

# --------------------
# Session state init
# --------------------
if "selected_images" not in st.session_state:
    st.session_state.selected_images = load_selections()

# --------------------
# Sidebar Navigation
# --------------------
page = st.sidebar.radio(
    "Navigation",
    ["All Images", "Shortlisted Images"]
)

# --------------------
# Page 1: All Images
# --------------------
if page == "All Images":
    st.title("All Abaya Images")

    # Clear all button
    if st.button("🧹 Clear all selections"):
        st.session_state.selected_images.clear()
        save_selections_if_changed(st.session_state.selected_images)
        st.rerun()

    if not image_files:
        st.warning("No images found in the images folder.")
    else:
        cols = st.columns(4)

        selection_changed = False

        for idx, img_path in enumerate(image_files):
            with cols[idx % 4]:
                st.image(str(img_path), use_container_width=True)

                key = f"select_{img_path.name}"
                checked = img_path.name in st.session_state.selected_images

                new_checked = st.checkbox(
                    "Select",
                    value=checked,
                    key=key
                )

                if new_checked and not checked:
                    st.session_state.selected_images.add(img_path.name)
                    selection_changed = True
                elif not new_checked and checked:
                    st.session_state.selected_images.discard(img_path.name)
                    selection_changed = True

        if selection_changed:
            save_selections_if_changed(st.session_state.selected_images)

        st.success(f"Selected images: {len(st.session_state.selected_images)}")

# --------------------
# Page 2: Shortlisted Images
# --------------------
elif page == "Shortlisted Images":
    st.title("Shortlisted Abayas")

    selected = [
        p for p in image_files if p.name in st.session_state.selected_images
    ]

    if not selected:
        st.info("No images selected yet.")
    else:
        cols = st.columns(4)
        selection_changed = False

        for idx, img_path in enumerate(selected):
            with cols[idx % 4]:
                st.image(str(img_path), use_container_width=True)

                if st.button(
                    "❌ Remove",
                    key=f"remove_{img_path.name}"
                ):
                    st.session_state.selected_images.remove(img_path.name)
                    selection_changed = True
                    st.rerun()

        if selection_changed:
            save_selections_if_changed(st.session_state.selected_images)

        # --------------------
        # Download ZIP
        # --------------------
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for img_path in selected:
                zip_file.write(img_path, arcname=img_path.name)

        st.download_button(
            label="⬇️ Download Selected Images",
            data=zip_buffer.getvalue(),
            file_name="selected_abayas.zip",
            mime="application/zip"
        )