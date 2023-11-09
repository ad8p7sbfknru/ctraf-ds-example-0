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

LOGGER = get_logger(__name__)

def exec():
    st.write("HI")

def dd():
    left_rate = int(st.session_state.d1l)
    right_rate = int(st.session_state.d1r)
    forward_rate = 100 - left_rate - right_rate
    st.session_state.d1f = str(forward_rate)
    st.write(forward_rate)

def run():
    st.set_page_config(
        page_title="CTraf Demo",
        page_icon="🚦",
    )


    st.write("# Welcome to CTraf Demo 🚦")

    st.write("Please enter Delta:")

    d1 = st.number_input("d1", 0, 9999, 100, 1, None, "delta1", "Do Something", on_change=None)
    d2 = st.number_input("d2", 0, 9999, 100, 1, None, "delta2", "Do Something", on_change=None)
    d3 = st.number_input("d3", 0, 9999, 100, 1, None, "delta3", "Do Something", on_change=None)
    d4 = st.number_input("d4", 0, 9999, 100, 1, None, "delta4", "Do Something", on_change=None)
    
    

    st.button("Compute 🚦", "b_exec", None, on_click=exec, args=None)


    if "d1f" not in st.session_state:
      st.session_state.d1f = str(70)
    if "d1l" not in st.session_state:
      st.session_state.d1l = 15
    if "d1r" not in st.session_state:
      st.session_state.d1r = 15
    

    if st.button('Reset  🚗'):
      st.session_state.d1f = str(70)

    
    col1, col2, col3 = st.columns(3)

    with col1:
      st.header("Left turn")
      st.slider("Percentage of vehicles making left turn", min_value=0, max_value=49, value=15, key="d1l", on_change=dd)


    with col2:
      st.header("Forward")
      st.write("Percentage of vehicles going forward")
      placeholder = st.empty()
      d1f_val = placeholder.text_input("", value=70, max_chars=None, key="d1f", disabled=False)

      
    with col3:
      st.header("Right turn")
      st.slider("Percentage of vehicles making right turn", min_value=0, max_value=49, value=15, key="d1r", on_change=dd)



    st.write(d1f_val)


    

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
