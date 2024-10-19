
from flask import Flask, render_template, request
from flask_session import Session

from transformers import AutoTokenizer
from datasets import load_dataset
from transformers import pipeline, set_seed

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

csv_url = "C:\\Users\\Zachary Root Laptop\\Downloads\\CORE_HackOhio_subset_cleaned_downsampled 1.csv"

@app.route("/", methods=["GET"])
def index():

    # just give the first 10 posts that exist in the database
    issues = get_important_issues(csv_url)
    print(issues)

    return render_template("index.html", issues=issues)

"""
def preprocess_function(examples):
    tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")
    return tokenizer(examples["PNT_ATRISKNOTES_TX"], truncation=True)

"""

def get_important_issues(csv_url):

    dataset = load_dataset("csv", data_files=csv_url)["train"]

    """
    generator = pipeline('text-generation', model='gpt2')
    set_seed(42)
    texts = generator("This is my im.", max_new_tokens=100, num_return_sequences=5, truncation=True)

    for t in texts:
        print(t)
    """
    out = dataset[0:5];

    return [dict(zip(out,t)) for t in zip(*out.values())]



if __name__ == "__main__":
    print(get_important_issues("C:\\Users\\Zachary Root Laptop\\Downloads\\CORE_HackOhio_subset_cleaned_downsampled 1.csv"))
