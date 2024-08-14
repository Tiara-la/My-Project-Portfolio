# Airline Customer Value Analysis ✈️


<img src="https://i.ibb.co/fxBHt1V/9179655dd5ff3224af22b769329416d7-removebg-preview.png" alt="Funny Indian Gif" width="400" align="center">

Welcome to the Airline Customer Value Analysis project! This repository contains code and resources for clustering and understanding customer behaviour.

## Table of Contents 📝

<table>
  <tr>
    <td>
        <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#dataset">Dataset</a></li>
        <li><a href="#model">Model</a></li>
        <li><a href="#evaluation">Evaluation</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
      </ul>
    </td>
    <td>
        <img src="https://i.ibb.co/YpTxVrY/Png-Item-1718003.png" alt="Funny Indian Gif" width="400">
    </td>
  </tr>
</table>

## 1. Introduction 🚀

The Airline Customer Value Analysis project aims to analyze customer data from an airline to identify key factors that drive customer value. This analysis will help in understanding customer behavior, preferences, and segments, enabling the airline to tailor its services and marketing strategies to enhance customer satisfaction and loyalty.

## 2. Features ⚖️

- **Data Preprocessing**: Clean and preprocess the data to make it suitable for machine learning models.
- **Feature Extraction**: Extract relevant features from video metadata.
- **Clustering**: Cluster the customer based on their behaviour and preferences.
- **Model Evaluation**: Evaluate the performance of the models using silhouette scores.

## 3. Installation 📖

1. Clone the repository:
    ```sh
    git clone https://github.com/heptaddc/Airline-Customer-Value-Analysis-Case.git
    cd Airline-Customer-Value-Analysis-Case
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## 4. Usage 🔨

1. Prepare your dataset in a CSV file with the required columns (e.g., title, description, tags, etc.).
2. You can find the dataset [here](https://www.kaggle.com/datasets/datasnaek/youtube-new?select=IN_category_id.json)
3. Make sure you already installed the requirements.txt library
4. Run the notebook

## 6. Dataset 📊

The dataset should be a CSV file containing the following columns:

| No | Nama Kolom | Definisi |
| :- | -: | :-: |
| 1 | MEMBER_NO-b | ID Member
| 2 | FFP_DATE | FFP_DATE
| 3 | FIRST_FLIGHT_DATE | Tanggal Penerbangan pertama
| 4 | GENDER | Jenis Kelamin
| 5 | FFP_TIER | Tier dari Frequent Flyer Program
| 6 | WORK_CITY | Kota Asal
| 7 | WORK_PROVINCE | Provinsi Asal
| 8 | WORK_COUNTRY | Negara Asal
| 9 | AGE | Umur Customer
| 10 | LOAD_TIME | Tanggal data diambil
| 11 | FLIGHT_COUNT | Jumlah penerbangan Customer
| 12 | BP_SUM |  Rencana Perjalanan
| 13 | SUM_YR_1 | Fare Revenue
| 14 | SUM_YR_2 | Votes Prices
| 15 | SEG_KM_SUM | Total jarak(km) penerbangan yg sudah dilakukan
| 16 | LAST_FLIGHT_DATE | Tanggal penerbangan terakhir
| 17 | LAST_TO_END | Jarak waktu penerbangan terakhir ke pesanan penerbangan paling akhir
| 18 | AVG_INTERVAL | Rata-rata jarak waktu
| 19 | MAX_INTERVAL | Maksimal jarak waktu
| 20 | EXCHANGE_COUNT | Jumlah penukaran
| 21 | avg_discount | Rata rata discount yang didapat customer
| 22 | Points_Sum |  Jumlah poin yang didapat customer
| 23 | Point_NotFlight |  point yang tidak digunakan oleh members


## 7. Model 📈

We are using KMeans clustering because it is simple to understand and easy to implement. It is computationally efficient, especially with large datasets, because its time complexity is linear in the number of data points.

## 8. Evaluation 📉

Model performance is evaluated using the following metrics:

- **Silhouette Scores**: Silhouette scores are a metric used to evaluate the quality of clusters created by clustering algorithms like K-means. They measure how similar an object is to its own cluster compared to other clusters.

## 9. Contributing 🫂

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## 10. License 🪪

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

![Funny Indian GIF](https://i.ibb.co/WWrzvRW/mochi-cat-peach.gif) <br>

Thank you for using the Airline Customer Value Analysis! If you have any questions or feedback, feel free to reach out. Happy clustering!
