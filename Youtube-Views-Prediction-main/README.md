# YouTube Views Prediction 📺


<img src="https://pnggallery.com/wp-content/uploads/little-krishna-03.png" alt="Funny Indian Gif" width="400" align="center">

Welcome to the YouTube Views Prediction project! This repository contains code and resources for predicting the number of views a YouTube video will receive based on various features such as title, description, tags, and more.

## Table of Contents 📝

<table>
  <tr>
    <td>
      <img src="https://cdn.pnggallery.com/wp-content/uploads/shahrukh-khan-02.png" alt="Funny Indian Gif" width="400">
    </td>
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
  </tr>
</table>

## 1. Introduction 🚀

Predicting the number of views a YouTube video will get can be valuable for content creators and marketers. This project aims to leverage machine learning techniques to make accurate predictions based on video metadata.

## 2. Features ⚖️

- **Data Preprocessing**: Clean and preprocess the data to make it suitable for machine learning models.
- **Feature Extraction**: Extract relevant features from video metadata.
- **Model Training**: Train various machine learning models to predict video views.
- **Model Evaluation**: Evaluate the performance of the models using metrics such as RMSE and R-squared (R²).

## 3. Installation 📖

1. Clone the repository:
    ```sh
    git clone https://github.com/heptaddc/youtube-views-prediction.git
    cd youtube-views-prediction
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

- `trending_date`: The date when the video was trending
- `title`: The title of the video
- `channel_title`: The name of the channel
- `category_id`: The category of the video in label encoding
- `publish_time`: The time the video was published
- `tags`: Tags used on the video
- `views`: Number of views of the video
- `likes`: Number of likes on the video
- `dislikes`: Number of dislikes on the video
- `comment_count`: Number of comments on the video
- `comments_disabled`: Whether the comments are disabled on the video
- `ratings_disabled`: Whether the ratings are disabled on the video
- `video_error_or_removed`: Whether the video is currently error-prone or has been removed
- `description`: Description of the video
- `No_tags`: Number of tags used
- `desc_len`: Length of the video description in words
- `len_title`: Length of the video title in words
- `publish_date`: The date the video was published


## 7. Model 📈

The model used for prediction is a machine learning regression model. Various models such as Linear Regression, Random Forest are explored to find the best performing one.

## 8. Evaluation 📉

Model performance is evaluated using the following metrics:

- **Root Mean Squared Error (RMSE)**: RMSE gives you an idea of how far off your model's predictions are from the actual values, with a lower RMSE indicating a better fit.
- **R-squared (R²)**: Indicates how well the data fit the regression model.

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

![Funny Indian GIF](https://i.ibb.co.com/S0Fbxhb/indian-bobble.gif) <br>

Thank you for using the YouTube Views Prediction project! If you have any questions or feedback, feel free to reach out. Happy predicting!
