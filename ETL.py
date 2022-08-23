{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc9a7077",
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install pandas\n",
    "pip install mysql-connector-python\n",
    "\n",
    "us = pd.read_csv(\"C:\\\\Users\\\\Vivek\\\\Desktop\\\\dataset\\\\archive\\\\USvideos.csv\")\n",
    "gb = pd.read_csv(\"C:\\\\Users\\\\Vivek\\\\Desktop\\\\dataset\\\\archive\\\\GBvideos.csv\")\n",
    "de = pd.read_csv(\"C:\\\\Users\\\\Vivek\\\\Desktop\\\\dataset\\\\archive\\\\DEvideos.csv\")\n",
    "ca = pd.read_csv(\"C:\\\\Users\\\\Vivek\\\\Desktop\\\\dataset\\\\archive\\\\CAvideos.csv\")\n",
    "fr = pd.read_csv(\"C:\\\\Users\\\\Vivek\\\\Desktop\\\\dataset\\\\archive\\\\FRvideos.csv\")\n",
    "ru = pd.read_csv(\"C:\\\\Users\\\\Vivek\\\\Desktop\\\\dataset\\\\archive\\\\RUvideos.csv\", encoding=\"latin -1\")\n",
    "mx = pd.read_csv(\"C:\\\\Users\\\\Vivek\\\\Desktop\\\\dataset\\\\archive\\\\MXvideos.csv\", encoding='latin-1')\n",
    "kr = pd.read_csv(\"C:\\\\Users\\\\Vivek\\\\Desktop\\\\dataset\\\\archive\\\\KRvideos.csv\", encoding=\"latin-1\")\n",
    "jp = pd.read_csv(\"C:\\\\Users\\\\Vivek\\\\Desktop\\\\dataset\\\\archive\\\\JPvideos.csv\", encoding='latin-1')\n",
    "ind = pd.read_csv(\"C:\\\\Users\\\\Vivek\\\\Desktop\\\\dataset\\\\archive\\\\INvideos.csv\")\n",
    "\n",
    "prj = pd.concat([us,gb,de,ca,fr,ru,mx,kr,jp,ind],ignore_index=True,axis=0)\n",
    "prj1=prj.fillna(\"good\")\n",
    "prj1.info()\n",
    "\n",
    "mydb = mysql.connector.connect(host=\"localhost\",user=\"root\",password=\"\")\n",
    "print(mydb)\n",
    "mycursor = mydb.cursor(buffered=True)\n",
    "mycursor.execute(\"CREATE DATABASE ETL_project\")\n",
    "mycursor.execute(\"USE etl_project \")\n",
    "mycursor.execute(\"CREATE TABLE prj(video_id VARCHAR(50),trending_date DATE,title VARCHAR(50),channel_title VARCHAR(50),category_id INT(50),publish_time TIME,tags VARCHAR(30),views INT(50) ,likes INT(50),dislikes INT(50),comment_count INT(50),thumbnail_link VARCHAR(100),comments_disabled BOOLEAN,ratings_disabled BOOLEAN,video_error_or_removed BOOLEAN,description VARCHAR(250))\")\n",
    "sql = \"INSERT INTO prj (video_id,trending_date,title,channel_title,category_id,publish_time,tags,views,likes,dislikes,comment_count,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)\"\n",
    "for i,row in prj1.iterrows():\n",
    "            sql = sql = \"INSERT INTO prj (video_id,trending_date,title,channel_title,category_id,publish_time,tags,views,likes,dislikes,comment_count,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)\"\n",
    "            mycursor.execute(sql, tuple(row))\n",
    "            print(\"Record inserted\")\n",
    "            mydb.commit()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
