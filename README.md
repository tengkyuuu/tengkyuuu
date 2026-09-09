<!-- =====================================================================
     PROFILE README — monochrome + dark blue

     Palette. Nothing outside this set; no second hue anywhere. Semantic
     signals (availability, project surface) are carried by VALUE and
     FORM, never by colour.

       #0A1628  ground          deep navy
       #0F2039  raised panel
       #1B3A63  mid navy        rules, quiet chips
       #2E5A94  accent navy     arrows, active chips
       #8A94A6  grey            blue-biased, secondary text
       #C9CFD9  light grey
       #FFFFFF  white           primary text on navy

     Graphics. assets/*.png are authored, not stock: built via the Canva
     MCP with add_page + insert_shape + add_text at the exact hexes above,
     then exported at native size. They are COMMITTED FILES, deliberately.
     Third-party render services (capsule-render, github-readme-stats,
     github-profile-trophy, activity-graph) all sit on shared over-quota
     Vercel instances — several already answer 402/503 — and a markdown
     image that fails renders as a broken-image icon. Committed PNGs have
     no such dependency. Total weight is ~95 KB for all three.

     Two constraints worth remembering before editing:
       - GitHub strips <style> and style="". There is no CSS here: no
         borders, shadows or gradients that are not baked into a PNG.
       - <details> is the only clickable element the sanitiser keeps, so
         it carries all the interaction. Everything important stays
         readable with every accordion shut.

     Canva source design: "tengkyuuu README graphics" (4 pages; page 1 is
     an unused 851x315 scratch canvas). Re-export at native size — custom
     width/height export is refused on this plan and fails with a
     misleading "not allowed to access design" error.
     ===================================================================== -->

<p align="center">
  <img src="assets/hero.png" alt="James Vincent Calunsag — Computer Engineer. Embedded firmware, production frontend, brand systems." />
</p>

<p align="center">
  <a href="mailto:jamescalunsag13@gmail.com"><img src="https://img.shields.io/badge/EMAIL-0F2039?style=for-the-badge&logo=gmail&logoColor=C9CFD9&labelColor=0A1628" alt="Email James" /></a>
  <!-- No logo= on the LinkedIn and Adobe chips: simple-icons dropped those
       glyphs over trademark policy, and shields silently renders nothing for
       an unknown slug. Text-only here is deliberate, not an oversight. -->
  <a href="https://www.linkedin.com/in/james-vincent-calunsag"><img src="https://img.shields.io/badge/LINKEDIN-0F2039?style=for-the-badge&labelColor=0A1628" alt="James on LinkedIn" /></a>
  <a href="https://engrjamescalunsag.vercel.app/"><img src="https://img.shields.io/badge/PORTFOLIO.DOCX-2E5A94?style=for-the-badge&logo=vercel&logoColor=FFFFFF&labelColor=0A1628" alt="Portfolio.docx" /></a>
  <img src="https://komarev.com/ghpvc/?username=tengkyuuu&color=0A1628&style=for-the-badge&label=VISITORS" alt="Profile views" />
</p>

<p align="center">
  <a href="#three-domains-one-engineer"><img src="https://img.shields.io/badge/DOMAINS-1B3A63?style=for-the-badge&labelColor=0A1628" alt="Jump to domains" /></a>
  <a href="#selected-work"><img src="https://img.shields.io/badge/WORK-1B3A63?style=for-the-badge&labelColor=0A1628" alt="Jump to selected work" /></a>
  <a href="#the-numbers"><img src="https://img.shields.io/badge/NUMBERS-1B3A63?style=for-the-badge&labelColor=0A1628" alt="Jump to the numbers" /></a>
  <a href="#say-hello"><img src="https://img.shields.io/badge/CONTACT-1B3A63?style=for-the-badge&labelColor=0A1628" alt="Jump to contact" /></a>
</p>

I work where hardware meets software: ESP32 firmware and fabricated PCBs on one side,
production React and brand systems on the other. I think from the silicon up and still
care about the surface people actually touch.

**Dapitan City, Philippines** (UTC+8) &nbsp;·&nbsp; **BS Computer Engineering** &nbsp;·&nbsp;
building [**Portfolio.docx**](https://engrjamescalunsag.vercel.app/), a portfolio that
behaves like a Word document &nbsp;·&nbsp; open to freelance, internships and collaborations.

---

## Three domains, one engineer

<p align="center">
  <img src="assets/domains.png" alt="Three domains: Embedded — ESP32 and AVR firmware, KiCad boards fabricated, Verilog on Quartus. Frontend — React and TypeScript apps that survive real users. Design — identity systems and type scales, plus the components that ship them." />
</p>

<details>
<summary><b>EMBEDDED</b> &nbsp;·&nbsp; ESP32, Arduino, Verilog, C/C++, PCB design</summary>

<br />

<p>
  <img src="https://img.shields.io/badge/ESP32-0F2039?style=for-the-badge&logo=espressif&logoColor=C9CFD9&labelColor=0A1628" alt="ESP32" />
  <img src="https://img.shields.io/badge/ARDUINO-0F2039?style=for-the-badge&logo=arduino&logoColor=C9CFD9&labelColor=0A1628" alt="Arduino" />
  <!-- intel, not xilinx: the FPGA work here is Quartus (see quartus-fpga-bcd),
       and shields ships no xilinx glyph anyway. -->
  <img src="https://img.shields.io/badge/FPGA_%2F_VERILOG-0F2039?style=for-the-badge&logo=intel&logoColor=C9CFD9&labelColor=0A1628" alt="FPGA and Verilog" />
  <img src="https://img.shields.io/badge/C_%2F_C%2B%2B-0F2039?style=for-the-badge&logo=cplusplus&logoColor=C9CFD9&labelColor=0A1628" alt="C and C plus plus" />
  <img src="https://img.shields.io/badge/KICAD-0F2039?style=for-the-badge&logo=kicad&logoColor=C9CFD9&labelColor=0A1628" alt="PCB design in KiCad" />
</p>

Firmware in C and C++ on ESP32 and AVR, boards drawn in KiCad and actually fabricated,
RTL in Verilog on Quartus. Wi-Fi and BLE transport, sensor conditioning, and the
unglamorous power budgeting that decides whether a deployment survives a month.

</details>

<details>
<summary><b>FRONTEND</b> &nbsp;·&nbsp; React, TypeScript, Tailwind, Flutter, Three.js</summary>

<br />

<p>
  <img src="https://img.shields.io/badge/REACT-0F2039?style=for-the-badge&logo=react&logoColor=C9CFD9&labelColor=0A1628" alt="React" />
  <img src="https://img.shields.io/badge/TYPESCRIPT-0F2039?style=for-the-badge&logo=typescript&logoColor=C9CFD9&labelColor=0A1628" alt="TypeScript" />
  <img src="https://img.shields.io/badge/TAILWIND-0F2039?style=for-the-badge&logo=tailwindcss&logoColor=C9CFD9&labelColor=0A1628" alt="Tailwind CSS" />
  <img src="https://img.shields.io/badge/FLUTTER-0F2039?style=for-the-badge&logo=flutter&logoColor=C9CFD9&labelColor=0A1628" alt="Flutter" />
  <img src="https://img.shields.io/badge/THREE.JS-0F2039?style=for-the-badge&logo=threedotjs&logoColor=C9CFD9&labelColor=0A1628" alt="Three.js" />
</p>

Comfortable owning a frontend end to end: routing, state, forms, data fetching,
accessibility, and the build. Flutter for mobile when one codebase is the right call
rather than the lazy one.

</details>

<details>
<summary><b>DESIGN</b> &nbsp;·&nbsp; Figma, Framer, Photoshop, Illustrator</summary>

<br />

<p>
  <img src="https://img.shields.io/badge/FIGMA-0F2039?style=for-the-badge&logo=figma&logoColor=C9CFD9&labelColor=0A1628" alt="Figma" />
  <img src="https://img.shields.io/badge/FRAMER-0F2039?style=for-the-badge&logo=framer&logoColor=C9CFD9&labelColor=0A1628" alt="Framer" />
  <!-- Adobe chips are text-only for the same trademark reason as LinkedIn. -->
  <img src="https://img.shields.io/badge/PHOTOSHOP-0F2039?style=for-the-badge&labelColor=0A1628" alt="Photoshop" />
  <img src="https://img.shields.io/badge/ILLUSTRATOR-0F2039?style=for-the-badge&labelColor=0A1628" alt="Illustrator" />
</p>

Identity systems, type scales, and tokens — then the components that implement them,
so the handoff is a commit instead of a PDF.

</details>

<details>
<summary><b>BACKEND &amp; TOOLS</b> &nbsp;·&nbsp; Node, Python, Firebase, Supabase, Git, Linux</summary>

<br />

<p>
  <img src="https://img.shields.io/badge/NODE.JS-0F2039?style=for-the-badge&logo=nodedotjs&logoColor=C9CFD9&labelColor=0A1628" alt="Node.js" />
  <img src="https://img.shields.io/badge/PYTHON-0F2039?style=for-the-badge&logo=python&logoColor=C9CFD9&labelColor=0A1628" alt="Python" />
  <img src="https://img.shields.io/badge/FIREBASE-0F2039?style=for-the-badge&logo=firebase&logoColor=C9CFD9&labelColor=0A1628" alt="Firebase" />
  <img src="https://img.shields.io/badge/SUPABASE-0F2039?style=for-the-badge&logo=supabase&logoColor=C9CFD9&labelColor=0A1628" alt="Supabase" />
  <img src="https://img.shields.io/badge/GIT-0F2039?style=for-the-badge&logo=git&logoColor=C9CFD9&labelColor=0A1628" alt="Git" />
  <img src="https://img.shields.io/badge/LINUX-0F2039?style=for-the-badge&logo=linux&logoColor=C9CFD9&labelColor=0A1628" alt="Linux" />
</p>

Enough backend to keep a device fleet fed: auth, realtime, storage, scheduled jobs,
and Python for the data wrangling that lives between the sensor and the chart.

</details>

---

## Selected work

| Project | What it is | Surface |
| :--- | :--- | :--- |
| **SHM** | Structural health monitoring — IoT sensors through to dashboard | `EMBEDDED` `WEB` |
| **Stormfresh** | Poultry ERP running on a working farm | `WEB` |
| **Physiopaño** | Mobile app plus an admin web portal | `MOBILE` `WEB` |
| **Rallys Equities** | Company site — brand and build | `BRAND` `WEB` |
| **MYKTECH** | Software studio website | `WEB` |
| **FameCRM** | CRM frontend | `WEB` |

<p align="center">
  <img src="assets/signal-path.png" alt="SHM signal path: sensor (accel/strain) to ESP32 (filter and pack) to transport (wifi/mqtt) to store (time series) to UI (charts/alerts). Every stage is one I had to own; the interesting problems were all at the arrows." />
</p>

SHM is the one to ask about. It is where the whole thesis holds up: a device that has to
stay alive unattended, a link that will drop, and a dashboard someone non-technical has
to trust. Full write-ups, with the constraints and what broke, live on
[**engrjamescalunsag.vercel.app**](https://engrjamescalunsag.vercel.app/).

<details>
<summary><b>How I work</b></summary>

<br />

- Read the datasheet before the tutorial.
- Reach for the scope before the print statement.
- Types at the boundary, freedom in the middle.
- Ship the thin vertical slice, then widen it.
- If it cannot be measured, it is not done.

Repos here are a mix of coursework, hardware experiments, and client work I could
open-source. The interesting failures are written up in the individual READMEs.

</details>

<details>
<summary><b>If you are hiring</b></summary>

<br />

| Need | What I actually do |
| :--- | :--- |
| **Device to dashboard** | Sensor firmware, transport, API, and the UI that reads it — one person, no handoff seams |
| **Frontend that ships** | React and TypeScript apps that survive real users, not just the demo path |
| **Brand and build** | Identity plus the site it lives on, so the design and the code never drift apart |

Freelance, internship and collaboration are all open. UTC+8, which overlaps EU mornings
and US evenings. Fastest path: [email me](mailto:jamescalunsag13@gmail.com) with the
constraint you are stuck on.

</details>

---

## The numbers

<!-- Two sources per card so the stats stay legible on both GitHub themes.
     A single fixed theme is unreadable on one of them. -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=tengkyuuu&hide_border=true&background=00000000&ring=2E5A94&fire=2E5A94&currStreakLabel=C9CFD9&sideLabels=C9CFD9&dates=8A94A6" />
    <img src="https://streak-stats.demolab.com?user=tengkyuuu&hide_border=true&background=00000000&ring=1B3A63&fire=1B3A63&currStreakLabel=0A1628&sideLabels=1F2328&dates=59636E" alt="Contribution streak for tengkyuuu" />
  </picture>
</p>

<!-- ---------------------------------------------------------------------
     The stats and top-languages cards are deliberately NOT here.

     github-readme-stats.vercel.app, github-profile-trophy.vercel.app and
     github-readme-activity-graph.vercel.app were all checked on
     2026-09-09: the first returns 503 on every request and the other two
     return 402, over their Vercel quota. Everyone points at those same
     shared instances, so they are chronically out of budget. A markdown
     image that 503s renders as a broken-image icon, which looks worse on
     a profile than having no card at all.

     The fix is to run your own instance, which you already have Vercel
     for. It takes about five minutes:

       1. Fork  https://github.com/anuraghazra/github-readme-stats
       2. Import the fork on Vercel and deploy it
       3. Add a PAT (no scopes needed) as PAT_1 in its env vars
       4. Swap the host below and uncomment

     Your own instance has your own rate limit, so it stops breaking.
     The colours below are already on-palette: 2E5A94 titles on dark,
     1B3A63 on light, greys from the token set at the top of this file.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://YOUR-INSTANCE.vercel.app/api?username=tengkyuuu&show_icons=true&hide_border=true&bg_color=00000000&title_color=2E5A94&text_color=C9CFD9&icon_color=2E5A94" />
    <img src="https://YOUR-INSTANCE.vercel.app/api?username=tengkyuuu&show_icons=true&hide_border=true&bg_color=00000000&title_color=1B3A63&text_color=1F2328&icon_color=1B3A63" alt="GitHub stats for tengkyuuu" height="165" />
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://YOUR-INSTANCE.vercel.app/api/top-langs/?username=tengkyuuu&layout=compact&hide_border=true&bg_color=00000000&title_color=2E5A94&text_color=C9CFD9" />
    <img src="https://YOUR-INSTANCE.vercel.app/api/top-langs/?username=tengkyuuu&layout=compact&hide_border=true&bg_color=00000000&title_color=1B3A63&text_color=1F2328" alt="Most used languages" height="165" />
  </picture>
</p>
     --------------------------------------------------------------------- -->

---

## Say hello

Bring me a constraint, not a spec sheet. The constraint is where the engineering is.

<p align="center">
  <a href="mailto:jamescalunsag13@gmail.com"><img src="https://img.shields.io/badge/EMAIL_ME-2E5A94?style=for-the-badge&logo=gmail&logoColor=FFFFFF&labelColor=0A1628" alt="Email James" /></a>
  <a href="https://engrjamescalunsag.vercel.app/"><img src="https://img.shields.io/badge/PORTFOLIO.DOCX-1B3A63?style=for-the-badge&logo=vercel&logoColor=FFFFFF&labelColor=0A1628" alt="Portfolio.docx" /></a>
  <a href="https://www.linkedin.com/in/james-vincent-calunsag"><img src="https://img.shields.io/badge/LINKEDIN-0F2039?style=for-the-badge&labelColor=0A1628" alt="James on LinkedIn" /></a>
</p>

<p align="center"><sub>Adaptability is the engineering skill.</sub></p>
