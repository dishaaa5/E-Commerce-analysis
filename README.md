# Ecommerce-Purchases Analysis

Analyze an e-commerce transactions dataset with **Python + Pandas** in VS Code / Jupyter.  
The project shows how to keep code in Git **without checking large CSVs into the repo**.

---

## 📂 Project Layout

ecommerce-analysis/
├── data/ # ← empty; dataset downloaded here by script
├── notebooks/
│ └── exploration.ipynb
├── scripts/
│ └── fetch_data.py # pulls dataset from Kaggle
├── src/
│ └── analysis.py # reusable analysis functions
├── .gitignore
├── environment.yml # Conda env (alt: requirements.txt)
└── README.md

yaml
Copy
Edit

---

## 🚀 Quick Start

### 1  Clone

```bash
git clone https://github.com/<your-user>/ecommerce-analysis.git
cd ecommerce-analysis
2 Set up Python environment
<details> <summary>Conda (recommended)</summary>
bash
Copy
Edit
conda env create -f environment.yml
conda activate ecommerce-analysis
</details> <details> <summary>pip + venv</summary>
bash
Copy
Edit
python -m venv .venv
# Windows: .venv\Scripts\activate   |   macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
</details>
3 Download the dataset (1st run only)
bash
Copy
Edit
python scripts/fetch_data.py
The helper runs:

bash
Copy
Edit
kaggle datasets download -d <owner>/ecommerce-purchases -p data/ -unzip
Prerequisite:

pip install kaggle

Place your kaggle.json token in ~/.kaggle/ (Windows: C:\Users\<you>\.kaggle\).

4 Explore
Notebook: code . → open notebooks/exploration.ipynb.

Script: python src/analysis.py.

🔍 Questions Answered
Highest / lowest / average purchase price

Count of French-speaking customers

Email for a given IP address

Mastercard users with purchases > $50

Cards expiring in 2020

Job titles containing “Engineer”

Modify the notebook or analysis.py to dig deeper.

🤝 Contributing
Fork → create feature branch

Commit with clear messages

Push → open Pull Request

📝 License
MIT – free to use, modify, and share with attribution.

🙏 Acknowledgements
Dataset originally published on Kaggle by <dataset author>.
Huge thanks to the Pandas, Jupyter, and VS Code teams for their fantastic tools.

bash
Copy
Edit

**Copy → paste → save 🎉**
