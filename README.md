# Space Instagram

My tool downloads photos from SpaceX and Hubble.
(You will see the photos in the folder 'images' in the directory with the tool) 
And after that my tool posts the photos to your Instagram account.

### How to install
Python3 should be already installed.

1) clone the repo
2) use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
    ```
    pip install -r requirements.txt
    ```
3) add .env file in the directory of the tool:
    ```
    INSTAGRAM_LOGIN=<your_instagram_login>
    INSTAGRAM_PASSWORD=<your_instagram_password>
    ```

### How to use
1) Write: 
    ```
    python3 main.py 
    ```
2) You are able to choose `flight_number` (SpaceX) , `collection_name` (Hubble)
   and folder in the directory with the tool for saving photos. 
   For example: 
    ```
    python3 main.py --flight_number=55 --collection_name='news' --folder='photos'
    ```
3) Default meanings:
    ```
    flight_number = 64, collection_name = spacecraft, folder = images
    ```
### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).