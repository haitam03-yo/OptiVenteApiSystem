# Sales Prediction API for Web Application

This project involves creating an API to be integrated into a web application. The API will provide sales predictions for a company based on historical sales data and various contextual factors, such as promotions, holidays, weather conditions, and stock availability. This is an extension of the work done during the  **DataTour 2024 competition** , where we achieved second place.

#### **Challenge Summary:**

**DataTour 2024 Challenge: Predicting Future Sales for a Company Based on Past Sales and Contextual Factors.**

#### **Context:**

Africa is experiencing rapid economic growth with a wide range of businesses operating across various sectors such as retail, e-commerce, and agro-food. One of the major challenges faced by African businesses is managing inventory and predicting future sales. Accurate sales predictions help businesses manage their inventory, optimize promotions, adjust pricing strategies, and maximize profits. Given the volatile demand nature, frequent promotions, fluctuating weather conditions, and special events (like holidays), a data-driven method based on past sales is essential for making reliable forecasts.

#### **Project Goal:**

The goal is to predict the number of units that will be sold between **November 1, 2024** and  **November 30, 2024** , using historical sales data from **January 1, 2022** to  **October 31, 2024** . This prediction will enable businesses to better manage their stock, plan promotional campaigns, and refine marketing strategies.

## **Requirements**

* Python 3.12 or later
* MiniConda for environment management

---

## **Setup Instructions**

### **1. Install MiniConda**

* Download and install MiniConda from [Miniconda Downloads](https://docs.anaconda.com/miniconda/install/).
* Choose the installer that matches your operating system (Windows, macOS, or Linux).

### **2. Create a Python Environment**

* Open your terminal or command prompt and run the following command to create a new environment:

  ```bash
  conda create -n mini-rag-app python=3.12
  ```

### **3. Activate the Environment**

* Activate your newly created environment:

  ```bash
  conda activate mini-rag-app
  ```

## Installation

### Install the Required Packages

```bash
pip install -r requirements.txt
```

### Setup the Environment Variables

```
cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.
