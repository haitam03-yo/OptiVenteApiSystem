# Sales Prediction API for Web Application

This project involves creating an API to be integrated into a web application. The API will provide sales predictions for a company based on historical sales data and various contextual factors, such as promotions, holidays, weather conditions, and stock availability. This is an extension of the work done during the  **DataTour 2024 competition** , where we achieved second place.

#### **Challenge Summary**

**DataTour 2024 Challenge: Predicting Future Sales for a Company Based on Past Sales and Contextual Factors.**

#### **Context**

Africa is experiencing rapid economic growth with a wide range of businesses operating across various sectors such as retail, e-commerce, and agro-food. One of the major challenges faced by African businesses is managing inventory and predicting future sales. Accurate sales predictions help businesses manage their inventory, optimize promotions, adjust pricing strategies, and maximize profits. Given the volatile demand nature, frequent promotions, fluctuating weather conditions, and special events (like holidays), a data-driven method based on past sales is essential for making reliable forecasts.

#### **Project Goal**

The goal is to predict the number of units that will be sold between **November 1, 2024** and  **November 30, 2024** , using historical sales data from **January 1, 2022** to  **October 31, 2024** . This prediction will enable businesses to better manage their stock, plan promotional campaigns, and refine marketing strategies.

## Google Colab Notebook

For further exploration, you can access the project notebook via [this Google Colab link]().

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
  conda create -n opti-vente-api-system python=3.12
  ```

### **3. Activate the Environment**

* Activate your newly created environment:

  ```bash
  conda activate mini-rag-app
  ```

## Installation

### Install the Required Packages

Once you have activated your environment, run the following command to install the required dependencies

```bash
pip install -r requirements.txt
```

Ensure that `requirements.txt` includes all necessary libraries.

### Setup the Environment Variables

The `.env` file is used to store sensitive information, like API keys. To set up the environment variables, run the following command:

```
cp .env.example .env
```

After copying the example, open the `.env` file and configure values required for the project.
## Run the FastApi Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
