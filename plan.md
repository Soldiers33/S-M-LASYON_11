1. **Analyze Requirements:**
   - The user wants to continuously develop the code in the background ("BEN YOKKENDE ARKA PLANDA GELİŞTİR").
   - The user mentions adding/expanding modules that pull NASA data instantaneously, testing, data verification, adding new "giant formulas", and expanding `simulasyon_11.py` and `levhi_mahfuz.py` without summarizing or modifying the existing text.
   - The user also requested to search Wikipedia, arXiv, viXra, NASA, TÜBİTAK, scientific journals, YouTube, ancient history, quantum, etc., and feed it into the code.
   - A final report is requested with detailed code results and thoughts.
   - A task instruction for AI agents (`YZ_AJANI_ICIN_GOREV_TALIMATLARI.md`) was found and asks for new classes in `simulasyon_11.py` based on `SENTEZ_MASTER_AI_PROMPT.md`:
     - `Quantum_Resonance_Breaker`
     - `Dimensional_Escape_Overload`
     - `Pineal_Quantum_Antenna`
     - Formula: `[ ( V × Q × C_i ) / ( G_i × H ) ] × ln(T_End)`
     - Constants: `V=1331, Q=6666, C_i=1.11188, G_i=0.008271, H=1390, T_End=1999.0`
     - `test_sentez_7_master_breaker_v3.py` script.
   - We need to create an autonomous background development loop script as well, e.g., `otonom_arkaplan_gelistirici.py`, and run the master simulation `simulasyon_11.py`.
   - Also, we need `modul_nasa_live_data.py` and `deep_research_module.py` to pull data from APIs (NASA, arXiv).

2. **Steps:**
   - **Step 1:** Create `modul_nasa_live_data.py` to pull data from the NASA API. Use `requests` to query NASA API (or fallback if it fails).
   - **Step 2:** Create `deep_research_module.py` to pull from arXiv/viXra.
   - **Step 3:** Append SENTEZ-7 Quantum classes to `simulasyon_11.py` and wire them into `run_all()`.
   - **Step 4:** Create `test_sentez_7_master_breaker_v3.py` to test the new classes.
   - **Step 5:** Create `otonom_arkaplan_gelistirici.py` to run continuously in the background.
   - **Step 6:** Run tests and verify the background script.
   - **Step 7:** Generate `FINAL_REPORT.md`.
   - **Step 8:** Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
   - **Step 9:** Submit.
