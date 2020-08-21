#Description : Create the program for resume scanner

#import docx2txt for docx file
import docx2txt

#load the data 
from google.colab import files
uploaded = files.upload()

#Store the resume into variable
resume=docx2txt.process("kumavat.resume.docx")

#Print the Resume
print(resume)

# open the other file
uploaded = files.upload()

#Store the job  description into a variavle
job_description = docx2txt.process("Job_Description.docx")

#Print the job_description 
print(job_description)

# A list of text 
text = [resume,job_description]

#import sklearn
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
count_matrix=cv.fit_transform(text)

#import cosine_similarity for matches
from sklearn.metrics.pairwise import cosine_similarity

#Print the similarity scores
print("\nSimilarity Scores : ")
print(cosine_similarity(count_matrix))

#get the match percentage 
matchPercentage = cosine_similarity(count_matrix)[0][1]*100
matchPercentage = round(matchPercentage,2) #round of two decimal numbers
print("Your resume matches about" + str(matchPercentage)+"% of the job discription.")

