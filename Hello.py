# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
from PIL import Image

LOGGER = get_logger(__name__)

def exec():
    st.write("HI")

def dd1():
    left_rate = int(st.session_state.d1l)
    right_rate = int(st.session_state.d1r)
    forward_rate = 100 - left_rate - right_rate
    st.session_state.d1f = str(forward_rate)

def dd2():
    left_rate = int(st.session_state.d2l)
    right_rate = int(st.session_state.d2r)
    forward_rate = 100 - left_rate - right_rate
    st.session_state.d2f = str(forward_rate)

def dd3():
    left_rate = int(st.session_state.d3l)
    right_rate = int(st.session_state.d3r)
    forward_rate = 100 - left_rate - right_rate
    st.session_state.d3f = str(forward_rate)

def dd4():
    left_rate = int(st.session_state.d4l)
    right_rate = int(st.session_state.d4r)
    forward_rate = 100 - left_rate - right_rate
    st.session_state.d4f = str(forward_rate)

def run():
    st.set_page_config(
        page_title="CTraf Demo",
        page_icon="🚦",
    )

    st.write("# Welcome to CTraf Demo 🚦")

    image = Image.open('crossroad.png')

    st.image(image, caption='X-shaped crossroad')


    st.divider()

    st.write("Please enter Delta:")

    dcol1, dcol2, dcol3, dcol4 = st.columns(4)

    with dcol1:
      d1 = st.number_input("d1", 0, 9999, 100, 1, None, "delta1", "Do Something", on_change=None)
    with dcol2:
      d2 = st.number_input("d2", 0, 9999, 100, 1, None, "delta2", "Do Something", on_change=None)
    with dcol3:
      d3 = st.number_input("d3", 0, 9999, 100, 1, None, "delta3", "Do Something", on_change=None)
    with dcol4:
      d4 = st.number_input("d4", 0, 9999, 100, 1, None, "delta4", "Do Something", on_change=None)
    
    st.divider()

    if "d1f" not in st.session_state:
      st.session_state.d1f = str(70)
    if "d1l" not in st.session_state:
      st.session_state.d1l = 15
    if "d1r" not in st.session_state:
      st.session_state.d1r = 15
    
    st.subheader("Direction 1")
    
    col1, col2, col3 = st.columns(3)

    with col1:
      st.write("⬅️ Percentage of vehicles making left turn")
      st.slider("", min_value=0, max_value=49, value=15, key="d1l", on_change=dd1)

    with col2:
      st.write("⬆️ Percentage of vehicles going forward")
      placeholder = st.empty()
      d1f_val = placeholder.text_input("", value=70, max_chars=None, key="d1f", disabled=True)

    with col3:
      st.write("➡️ Percentage of vehicles making right turn")
      st.slider("", min_value=0, max_value=49, value=15, key="d1r", on_change=dd1)

    st.divider()


    if "d2f" not in st.session_state:
      st.session_state.d2f = str(70)
    if "d2l" not in st.session_state:
      st.session_state.d2l = 15
    if "d2r" not in st.session_state:
      st.session_state.d2r = 15
    
    st.subheader("Direction 2")
    
    col1, col2, col3 = st.columns(3)

    with col1:
      st.write("⬅️ Percentage of vehicles making left turn")
      st.slider("", min_value=0, max_value=49, value=15, key="d2l", on_change=dd2)

    with col2:
      st.write("⬆️ Percentage of vehicles going forward")
      placeholder = st.empty()
      d2f_val = placeholder.text_input("", value=70, max_chars=None, key="d2f", disabled=True)

    with col3:
      st.write("➡️ Percentage of vehicles making right turn")
      st.slider("", min_value=0, max_value=49, value=15, key="d2r", on_change=dd2)

    st.divider()


    if "d3f" not in st.session_state:
      st.session_state.d3f = str(70)
    if "d3l" not in st.session_state:
      st.session_state.d3l = 15
    if "d3r" not in st.session_state:
      st.session_state.d3r = 15
    
    st.subheader("Direction 3")
    
    col1, col2, col3 = st.columns(3)

    with col1:
      st.write("⬅️ Percentage of vehicles making left turn")
      st.slider("", min_value=0, max_value=49, value=15, key="d3l", on_change=dd3)

    with col2:
      st.write("⬆️ Percentage of vehicles going forward")
      placeholder = st.empty()
      d3f_val = placeholder.text_input("", value=70, max_chars=None, key="d3f", disabled=True)

    with col3:
      st.write("➡️ Percentage of vehicles making right turn")
      st.slider("", min_value=0, max_value=49, value=15, key="d3r", on_change=dd3)

    st.divider()


    if "d4f" not in st.session_state:
      st.session_state.d4f = str(70)
    if "d4l" not in st.session_state:
      st.session_state.d4l = 15
    if "d4r" not in st.session_state:
      st.session_state.d4r = 15
    
    st.subheader("Direction 4")
    
    col1, col2, col3 = st.columns(3)

    with col1:
      st.write("⬅️ Percentage of vehicles making left turn")
      st.slider("", min_value=0, max_value=49, value=15, key="d4l", on_change=dd4)

    with col2:
      st.write("⬆️ Percentage of vehicles going forward")
      placeholder = st.empty()
      d4f_val = placeholder.text_input("", value=70, max_chars=None, key="d4f", disabled=True)

    with col3:
      st.write("➡️ Percentage of vehicles making right turn")
      st.slider("", min_value=0, max_value=49, value=15, key="d4r", on_change=dd4)

    st.divider()



    #st.write(d1f_val)
    #st.write(d2f_val)
    #st.write(d3f_val)
    #st.write(d4f_val)

    st.button("Compute 🚦", "b_exec", None, on_click=exec, args=None)

    #if st.button('Reset  🚗'):
    #  st.session_state.d1f = str(70)


    delta = [d1, d2, d3, d4, 0, 0, 0, 0]
    st.json(delta)

    dir1 = [int(st.session_state.d1l)/100, int(st.session_state.d1f)/100, int(st.session_state.d1r)/100]
    dir2 = [int(st.session_state.d2l)/100, int(st.session_state.d2f)/100, int(st.session_state.d2r)/100]
    dir3 = [int(st.session_state.d3l)/100, int(st.session_state.d3f)/100, int(st.session_state.d3r)/100]
    dir4 = [int(st.session_state.d4l)/100, int(st.session_state.d4f)/100, int(st.session_state.d4r)/100]

    dir = [dir1, dir2, dir3, dir4]
    st.json(dir)


    st.sidebar.success("CTraf Demo 🚦")



if __name__ == "__main__":
    run()
