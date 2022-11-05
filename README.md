
## Health lab Web Project

This is machine learning wep app that used to Predict  the health disease like Diabetes, Heart, Kidney, Liver, Breast cancer, Stroke.



#### Diabetes
Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.
Your body breaks down most of the food you eat into sugar (glucose) and releases it into your bloodstream. 
#### Heart Attack
The term “heart disease” refers to several types of heart conditions. The most common type of heart disease in the United
States is coronary artery disease (CAD), which affects the blood flow to the heart. Decreased blood flow can cause a heart attack.
#### Chronic Kidney Disease
Chronic kidney disease, also called chronic kidney failure, involves a gradual loss of kidney function.
Your kidneys filter wastes and excess fluids from your blood, which are then removed in your urine. 
Advanced chronic kidney disease can cause dangerous levels of fluid, electrolytes and wastes to build up in your body.
#### Liver Disease
Liver disease doesn't always cause noticeable signs and symptoms. If signs and symptoms of liver disease do occur, 
they may include: Skin and eyes that appear yellowish (jaundice) Abdominal pain and swelling. Swelling in the legs and ankles.
			
#### Breast Cancer
Breast cancer can occur in women and rarely in men.Symptoms of breast cancer include a lump in the breast, 
bloody discharge from the nipple and changes in the shape or texture of the nipple or breast.Its treatment depends 
on the stage of cancer. It may consist of chemotherapy, radiation, hormone therapy and surgery.
#### Stroke
A stroke, sometimes called a brain attack, occurs when something blocks blood supply to part of the brain or when a blood vessel 
in the brain bursts. In either case, parts of the brain become damaged or die. A stroke can cause lasting brain damage,
long-term disability, or even death.

## If you want to view the deployed project, click on the following link:

• https://health-lab.herokuapp.com/

## Screenshots
![Alt text](/static/images/screenshots/01.png?raw=true "Screen 1")
![Alt text](/static/images/screenshots/02.png?raw=true "Screen 2")
![Alt text](/static/images/screenshots/03.png?raw=true "Screen 3")
![Alt text](/static/images/screenshots/04.png?raw=true "Screen 4")
![Alt text](/static/images/screenshots/05.png?raw=true "Screen 5")


## DataSet links
1. [Heart Disease](https://www.kaggle.com/code/cdabakoglu/heart-disease-classifications-machine-learning)

2. [Liver Disease](https://www.kaggle.com/datasets/uciml/indian-liver-patient-records)

3. [Diabetes Disease](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

4. [Stroke Prediction](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

5. [Breast Cancer Disease](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)

6. [Chronic Kidney Disease](https://www.kaggle.com/datasets/mansoordaku/ckdisease)

## Roadmap

- Data Collection
- Data Analysis
- Data Visualization
- Feature Engineering
- Feature Selection
- Model Building
- Model Evalution
- Hyper Parameter Tunning
- Creating Pickle file
- Web App using Flask
- Deployment


## Tech Stack

**python packages:** Pandas, Numpy, Scikit-learn, matplotlib

**ML Algorithms:** Node, Express

**Framework:** Flask

**frontend:** Html, CSS



## Run Locally

Clone the project

```bash
  git clone https://github.com/KaushalSalvatore/health-lab-project.git
```
Install dependencies

```bash
  pip install -r requirements. txt
```

Start the local server

```bash
  Python server.py or server.py
```


## Deploy on a Github

To deploy this project on github use this following command in the project folder.

Initializing a new repository
```bash
  git .init
```

A gitignore file specifies intentionally untracked files that Git should ignore.
```bash
  touch .gitignore
```
Add all the files 
```bash
  git add .
```
Check file status 
```bash
  git status
```
Commit all the file on git
```bash
  git commit -m "your message"
```
Push all the code on github
```bash
  git push <your_branch_name>
```
Push code forcefully 

```bash
  git push origin <your_branch_name> --force
```




## Deploy on heroku

To deploy project on heroku server use this following command.

login in heroku server
```bash
  login heroku
```
Install gunicorn
```bash
  pip install gunicorn
```
Create procfile
```bash
  touch Procfile
```
Create requirements text file 
```bash
  pip freeze > requirements.txt
```
Creates a new empty application on Heroku
```bash
  heroku create -a "project name"
```
Add a remote to your local repository 
```bash
  git remote -v
```
push the code in heroku master branch
```bash
  git push heroku master
```
## Feedback

if you have any suggetion and feedback and need any kind of project related help reach me out at
[linkedin](https://www.linkedin.com/in/kaushal-pandey-067898165/)

#### Thank You 