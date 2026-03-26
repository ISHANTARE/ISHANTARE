import os

README_PATH = "c:\\Users\\Admin\\VIT_Projects\\ISHANTARE\\README.md"

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Tech Core with Periodic Table of Skills
tech_core_old = """<div align="center">
  <h4>» ENGINE & LOGIC «</h4>
  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=python,cpp,r,java,js,go&theme=dark" /></a>
  
  <h4>» NEURAL MATRICES & DATA «</h4>
  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=tensorflow,pytorch,pandas,postgres,mysql&theme=dark" /></a>
  
  <h4>» COMM-SCREENS & INFRASTRUCTURE «</h4>
  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=react,nextjs,nodejs,aws,docker,figma&theme=dark" /></a>
</div>"""

periodic_table = """<div align="center">
  <table style="border-collapse: separate; border-spacing: 5px; background-color: transparent; border: none;">
    <tr>
      <!-- ROW 1: ENGINE & LOGIC -->
      <td align="center" width="75" style="border: 1px solid #00e5ff; border-radius: 8px; background: rgba(0,229,255,0.05); padding: 5px; border-collapse: separate;">
        <img src="https://skillicons.dev/icons?i=python" width="30"/><br><b style="color: #00e5ff;">Py</b><br><sub style="color: #ccc;">Python</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #00e5ff; border-radius: 8px; background: rgba(0,229,255,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=cpp" width="30"/><br><b style="color: #00e5ff;">C++</b><br><sub style="color: #ccc;">C++</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #00e5ff; border-radius: 8px; background: rgba(0,229,255,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=r" width="30"/><br><b style="color: #00e5ff;">R</b><br><sub style="color: #ccc;">R-Lang</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #00e5ff; border-radius: 8px; background: rgba(0,229,255,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=java" width="30"/><br><b style="color: #00e5ff;">Jv</b><br><sub style="color: #ccc;">Java</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #00e5ff; border-radius: 8px; background: rgba(0,229,255,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=js" width="30"/><br><b style="color: #00e5ff;">Js</b><br><sub style="color: #ccc;">JScript</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #00e5ff; border-radius: 8px; background: rgba(0,229,255,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=go" width="30"/><br><b style="color: #00e5ff;">Go</b><br><sub style="color: #ccc;">GoLang</sub>
      </td>
    </tr>
    <tr>
      <!-- ROW 2: NEURAL MATRICES & DATA -->
      <td align="center" width="75" style="border: 1px solid #00FF41; border-radius: 8px; background: rgba(0,255,65,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=tensorflow" width="30"/><br><b style="color: #00FF41;">Tf</b><br><sub style="color: #ccc;">TensorF</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #00FF41; border-radius: 8px; background: rgba(0,255,65,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=pytorch" width="30"/><br><b style="color: #00FF41;">Pt</b><br><sub style="color: #ccc;">PyTorch</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #00FF41; border-radius: 8px; background: rgba(0,255,65,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=pandas" width="30"/><br><b style="color: #00FF41;">Pd</b><br><sub style="color: #ccc;">Pandas</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #00FF41; border-radius: 8px; background: rgba(0,255,65,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=postgres" width="30"/><br><b style="color: #00FF41;">Pg</b><br><sub style="color: #ccc;">Postgres</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #00FF41; border-radius: 8px; background: rgba(0,255,65,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=mysql" width="30"/><br><b style="color: #00FF41;">My</b><br><sub style="color: #ccc;">MySQL</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #00FF41; border-radius: 8px; background: rgba(0,255,65,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=mongodb" width="30"/><br><b style="color: #00FF41;">Mg</b><br><sub style="color: #ccc;">Mongo</sub>
      </td>
    </tr>
    <tr>
      <!-- ROW 3: COMM-SCREENS & INFRASTRUCTURE -->
      <td align="center" width="75" style="border: 1px solid #f9a826; border-radius: 8px; background: rgba(249,168,38,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=react" width="30"/><br><b style="color: #f9a826;">Re</b><br><sub style="color: #ccc;">React</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #f9a826; border-radius: 8px; background: rgba(249,168,38,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=nextjs" width="30"/><br><b style="color: #f9a826;">Nx</b><br><sub style="color: #ccc;">Next.js</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #f9a826; border-radius: 8px; background: rgba(249,168,38,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=nodejs" width="30"/><br><b style="color: #f9a826;">Nd</b><br><sub style="color: #ccc;">Node.js</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #f9a826; border-radius: 8px; background: rgba(249,168,38,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=aws" width="30"/><br><b style="color: #f9a826;">Aw</b><br><sub style="color: #ccc;">AWS</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #f9a826; border-radius: 8px; background: rgba(249,168,38,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=docker" width="30"/><br><b style="color: #f9a826;">Dk</b><br><sub style="color: #ccc;">Docker</sub>
      </td>
      <td align="center" width="75" style="border: 1px solid #f9a826; border-radius: 8px; background: rgba(249,168,38,0.05); padding: 5px;">
        <img src="https://skillicons.dev/icons?i=figma" width="30"/><br><b style="color: #f9a826;">Fg</b><br><sub style="color: #ccc;">Figma</sub>
      </td>
    </tr>
  </table>
</div>"""
content = content.replace(tech_core_old, periodic_table)

# 2. Insert Decryption Console after Flagship Projects
decryption_console = """
<details>
  <summary><code><b>[ > INTERCEPT_ENCRYPTED_LOG... PRESS TO DECRYPT ]</b></code></summary>
  <br>
  <div style="background-color: #0e0e0e; border-left: 4px solid #00FF41; padding: 15px; font-family: monospace; color: #00FF41; border-radius: 0px 8px 8px 0px;">
    <code>
      $ authenticate user<br>
      > ACCESS GRANTED. Welcome Commander.<br><br>
      FILE_NAME: <b>CLASSIFIED_DATABANKS.txt</b><br><br>
      > <b>Log Entry 34-A:</b> 'Carter Blaize' wasn't just a sci-fi writing experiment. It traces the architecture of my deep learning pipelines mapped against the vastness of interstellar void.<br>
      > <b>Log Entry 38-C:</b> ASTRA-Core propagates thousands of orbital paths per second. Sometime I wonder, do coordinates dream of endless horizons?<br><br>
      > END OF LOG.
    </code>
  </div>
</details>

<br/>
<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%" />
</div>

## ⚙️ `[ SYS.ARSENAL // TECH_CORE ]`
"""
content = content.replace("## ⚙️ `[ SYS.ARSENAL // TECH_CORE ]`", decryption_console)

# 3. Add Deep Space Scan (APOD) and Carter Blaize Text Adventure at the bottom before footer
new_sections = """## 🔭 `[ SYS.OBSERVATORY // DEEP_SPACE_SCAN ]`

<div align="center">
  <p><i>Uplinking to NASA Mainframe. Accessing Astronomy Picture of the Day...</i></p>
  <!-- START_SECTION:apod -->
  <!-- NASA APOD will be auto-generated here by GitHub Actions -->
  <a href="https://apod.nasa.gov/apod/astropix.html"><img src="https://custom-icon-badges.demolab.com/badge/NASA-Awaiting_Transmission-red.svg?logo=satellite&logoColor=white" /></a>
  <!-- END_SECTION:apod -->
</div>

<br/>
<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%" />
</div>

## 🌌 `[ SYS.SIMULATION // PROTOCOL: CARTER BLAIZE ]`

> *WARNING: You have entered a simulation matrix. The following choices determine the fate of the ASTRA-Core.*

**SCENARIO:** You are adrift orbiting the Kepler-22 star system. A localized solar flare has knocked out your primary navigation matrix. 

Do you:
A) `[` [Reroute power to the Cowell Propagator Engine](#choice-a-cowell) `]`
B) `[` [Manually recalculate telemetry using raw visual data](#choice-b-manual) `]`

<div align="center">
<hr style="width: 50%; border-top: 1px dashed #00e5ff;"/>
</div>

<h4 id="choice-a-cowell">If you chose [A] - Reroute to Cowell Propagator:</h4>
<details>
  <summary><i>Initiating Cowell Phase...</i></summary>
  <blockquote>
    The engine sputters. Your high-fidelity SGP4 models kick in, predicting the exact trajectory around the binary star. The thrusters align perfectly. You break orbit and secure a comm-link back to Nexus HQ. <b>[MISSION SUCCESS]</b>
  </blockquote>
</details>

<h4 id="choice-b-manual">If you chose [B] - Manually recalculate:</h4>
<details>
  <summary><i>Accessing visual arrays...</i></summary>
  <blockquote>
    Raw data floods your screen. You attempt a hasty numerical integration, but the orbital perturbances are too complex for unassisted calculations. The gravitational pull of Kepler-22 captures your ship. At least the view is spectacular. <b>[CRITICAL FAILURE]</b>
  </blockquote>
</details>

<br/>
<div align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%" />
</div>

<!-- FOOTER WITH SHUTDOWN ANIMATION -->
"""

content = content.replace("<!-- FOOTER WITH SHUTDOWN ANIMATION -->", new_sections)

# 4. Insert Binary Transmission at the very end
binary_transmission = """  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" height="150px" style="object-fit:cover; border-radius: 15px;" alt="Space Footer"/>
</div>

<br/>
<div align="center">
  <p style="color: #4a4a4a; font-size: 10px;">
    <code>01001001 01100110 00100000 01111001 01101111 01110101 00100000 01100100 01100101 01100011 01101111 01100100 01100101 01100100 00100000 01110100 01101000 01101001 01110011 00101100 00100000 01111001 01101111 01110101 00100000 01100001 01110010 01100101 00100000 01100001 00100000 01110100 01110010 01110101 01100101 00100000 01101110 01100101 01111000 01110101 01110011 00100000 01100001 01110010 01100011 01101000 01101001 01110100 01100101 01100011 01110100 00101110</code>
  </p>
</div>
"""
content = content.replace('  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" height="150px" style="object-fit:cover; border-radius: 15px;" alt="Space Footer"/>\n</div>', binary_transmission)


with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Update script customized and saved modifications.")
