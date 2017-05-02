#NLP Case Study

The objective of this case study can be found in case study.md .

To use this tool, place all the reviews file in the **Data** folder in json format and enter the **topic** on which you want to search hotels when promted.

###Dependencies
Install `nltk` package if its not already installed on the machine with:

`pip install nltk`

`nltk.download()` then download whole package from the gui.

Install `numpy` with:

`pip install numpy`

Install `matplotlib` with:

`pip install matplotlib`

In **Reviews.py** change the path in the `getReviews()` method to your local directory where you have cloned the repository.

Run **config.py** 

###Output
The best hotel for the given topic will be suggested in the console.
A bar graph of the hotel comparison will pop up to show where each hotel stands in ratings for easier interpretation.

