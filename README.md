
## 📦 Dataset

This project uses the [Instacart Online Grocery Shopping Dataset 2017](https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2), containing over **3 million grocery orders** from more than **200,000 users**.


### 🪪 License

- Source: https://gist.github.com/jeremystan/582eba13d6ee27ed465c43dc78934700  
- This dataset is intended for non-commercial, educational, and research purposes.

---

### 📥 How to Download the Dataset

> [!NOTE]
> **You will need a Kaggle account and an API key to download the data.**

#### 1. Generate your Kaggle API key

- Go to your Kaggle account: [https://www.kaggle.com/account](https://www.kaggle.com/account)
- Scroll down to **API > Create New API Token**
- This downloads a file called `kaggle.json`

#### 2. Place the API key in the proper location

Move `kaggle.json` to:

- **Windows**: `C:\Users\<YourUsername>\.kaggle\kaggle.json`
- **Linux/Mac**: `~/.kaggle/kaggle.json`

Or, set environment variables instead:

```bash
export KAGGLE_USERNAME=your_username
export KAGGLE_KEY=your_key
```

#### 3. Run the dataset fetch script

```bash
pip install kaggle
python get_dataset.py
```

The script will:
- Authenticate using the Kaggle API
- Download and extract the dataset to `data/raw/`

---

### 📁 Data Structure

```
project-root/
├── data/
│   ├── raw/              # Original downloaded files
│   │   ├── aisles.csv
│   │   ├── departments.csv
│   │   ├── order_products__prior.csv
│   │   ├── order_products__train.csv
│   │   ├── orders.csv
│   │   └── products.csv
│   └── processed/        # Cleaned / transformed datasets
├── get_dataset.py        # Script to download data via Kaggle API
```

