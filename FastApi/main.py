from fastapi import FastAPI
app = FastAPI()

courses_db = [
    {"id": 1, "instructor": "Edip", "title": "Python for Beginners", "category": "Programming Languages"},
    {"id": 2, "instructor": "Ahmet", "title": "Advanced JavaScript", "category": "Web Development"},
    {"id": 3, "instructor": "Yiğit", "title": "Machine Learning Fundamentals", "category": "Data Science"},
    {"id": 4, "instructor": "Edip", "title": "C# Basics", "category": "Software Development"},
    {"id": 5, "instructor": "Atil", "title": "Python Data Analysis", "category": "Data Science"},
    {"id": 6, "instructor": "Mavi", "title": "Web Development with Django", "category": "Web Development"},
    {"id": 7, "instructor": "Zeynep", "title": "React for Frontend Developers", "category": "Web Development"},
]


#endpoint her bir / afteri örnek olarak eğitimler/kurslar  buradaki kurslar bir endpointtir
@app.get("/") # burası path vermek içindir
async def HelloWorld(): #asenkron olarak çalıştırmak amacıyla
    return {"message": "Hello World"}

#JSON js object verileri paylaşmak için client ile sunucu arasında iletişim için kullanılır


@app.get("/courses") # /docs swagger açar
async def get_courses():
    return courses_db

#özel bir şey return ettirmek istersem
#path ve query ile yapılabilir

@app.get("/courses/{course_title}")
async def get_course(course_title: str):
    for course in courses_db:
        if course["title"].casefold() == course_title.casefold():
            return course


@app.get("/courses/{course_id}")
async def get_course_by_id(course_id: int):
    for course in courses_db:
        if course.get("id").casefold()  == course_id:
            return course

@app.get("/courses/by_id/{course_id}")
async def get_course_by_id(course_id: int):
    for course in courses_db:
        if course.get("id")  == course_id:
            return course
