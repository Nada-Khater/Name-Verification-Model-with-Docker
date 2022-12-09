# Name-Verification-Model-with-Docker
## Overview

Name verification model using tensorflow v2 and word embedding that classifies the input name into real and fake name with accuracy of 99%

## Dataset
Dataset available at: https://www.kaggle.com/code/mohamedmagdy11/identify-egyptian-high-school-students-gender/data?select=01_firstExam_data_arabic_extra_gender_feature_v1.csv

## Data Generation
For Real Data: dropping all columns except name column then take only the first three names from each name.
For Fake Data: taking 30% from real data then shuffling them.

![ds](https://user-images.githubusercontent.com/75952748/206811530-879bd7c2-b5c9-41a2-ab72-38e0ae8b5e5f.png)


## How to build docker image

- Create requirement.txt file in your project folder with the version of the used libraries in your model:

```bash
numpy==1.23.5
tensorflow==2.8.0
keras==2.8.0
Flask==2.2.2
```
- Create a dockerfile in your project folder with the following script:

```python
FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```
- Then open cmd in the path of your local project and run the following:

```bash
docker image build -t namemodel .
```

```bash
docker run -p 5000:5000 -d namemodel
```

```bash
docker container ls
```

- Output should be like this:
![Docker](https://user-images.githubusercontent.com/75952748/206787660-28353199-ac28-4c49-8144-a001999e2cc1.png)

## How to test the model

Move at this link: http://localhost:5000/ and in URL type the following 
- http://127.0.0.1:5000/?name= عمر محمد احمد => Real Name
- http://127.0.0.1:5000/?name= اان$رلاا //رر => Fake Name 

- Output should be like this:

![Real](https://user-images.githubusercontent.com/75952748/206790131-678f21ff-3511-406e-91ac-9affadcab1ae.png)
![Fake](https://user-images.githubusercontent.com/75952748/206789208-b39d20ba-eaab-4bc5-8f1b-ba6b21699d92.png)

## Docker Container
![Docker2](https://user-images.githubusercontent.com/75952748/206789352-1c00a2ef-33c7-4ee0-87a5-0534c28cd0d2.png)
![Docker1](https://user-images.githubusercontent.com/75952748/206789368-3c1015bd-63e3-476e-b141-82183a7d8725.png)







