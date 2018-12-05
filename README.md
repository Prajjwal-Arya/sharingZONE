## sharingZONE
The simplest way to send big files around the world. Today we’re a set of beautifully obvious tools that bring your ideas to life.
Built to get files from one place to the other, this is the classic way of sharing experience. Send up to 5gb of files per 
transfer and we will handle it with ease. 

## Working Example 
http://tonypapa077.pythonanywhere.com/

## Running Locally

```bash
git clone https://github.com/Prajjwal-Arya/sharingZONE.git
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```


###Usage

###Views

Four views handle sharing, detail, and deletion. 

####ProgressBarUploadView

Validates form input to upload files. Optionally adds files to a specified folder. 
Shows how much file has been uploaded. 

URL: `mysite/core/ProgressBarUploadView`

Template: `photos/prgogress_bar_upload/index.html`

####DragAndDropUploadView

Validates form input to upload files. Files can be uploaded through this via drag and drop.

URL: `mysite/core/DragAndDropUploadView`

Template: `photos/drag_and_drop/index.html`

####HomeView

Checks if the storage is below an expected amount, deletes all the files if the storage is low.

URL: `mysite/core/HomeView`

Template: `mysite/core/home.html`

##Contributing
`https://github.com/Prajjwal-Arya`







	
