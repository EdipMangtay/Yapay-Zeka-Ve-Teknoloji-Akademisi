from fastapi import FastAPI,Body
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

#Query yapmak
@app.get("/courses/")
async def get_categoryByQuery(category: str):
    """
    Belirli bir kategoriye ait kursları döndürür.

    Args:
    - category (str): Sorgu parametresi olarak alınan kategori adı.

    Returns:
    - List: Belirtilen kategoriye ait tüm kursları içeren bir liste.
    """
    course_to_return = []  # Kategorisi uygun olan kursları saklayacak liste
    for course in courses_db:
        # category ile eşleşen kursları bul
        if course.get("category").casefold() == category.casefold():
            course_to_return.append(course)  # Listeye ekle
    return course_to_return  # Döngü tamamlandıktan sonra listeyi döndür


@app.get("/courses/{course_instructor}/")
async def get_instructor_category_by_query(course_instructor: str, category: str):
    """
    Bu fonksiyon, belirli bir eğitmen ve kategoriye uygun olan kursları döndürür.

    Args:
        course_instructor (str): Eğitmenin adı.
        category (str): Kurs kategorisi.

    Returns:
        list: Eğitmen ve kategoriye uygun olan kurslar.
    """
    courses_to_return = []  # Uygun kursları depolamak için bir liste oluşturulur.

    # 'courses_db' adlı veritabanında her bir kurs için döngü başlatılır.
    for course in courses_db:
        # Eğitmen adı ve kategori eşleşiyorsa, kurs listeye eklenir.
        if (
            course.get('instructor').casefold() == course_instructor.casefold()  # Eğitmen adı kontrol edilir (case-insensitive).
            and course.get('category').casefold() == category.casefold()        # Kategori kontrol edilir (case-insensitive).
        ):
            courses_to_return.append(course)  # Uygun kurs listeye eklenir.

    # Sonuçlar döndürülür.
    return courses_to_return


@app.post("/courses/create_post")
async def create_course(new_course=Body()):
    courses_db.append(new_course)
    return new_course


@app.put("/courses/update_course")
async def update_course(updated_course=Body()):
    """
    Belirtilen ID'ye sahip bir kursu günceller.

    Args:
        updated_course (dict): Güncellenmek istenen kurs bilgilerini içeren sözlük. İçerisinde `id` anahtarı bulunmalıdır.

    Returns:
        dict: Güncellenmiş kurs bilgileri.
    """
    # Tüm kursları indeksleriyle birlikte dolaş
    for index in range(len(courses_db)):
        # Eğer kursun 'id'si, güncellenmek istenen kursun 'id'sine eşitse
        if courses_db[index].get("id") == updated_course.get("id"):
            # Eski kursu, güncellenmiş kursla değiştir
            courses_db[index] = updated_course
            return updated_course  # Güncellenmiş kursu döndür

    # Eğer belirtilen ID ile eşleşen bir kurs bulunamazsa, hata mesajı döndür
    return {"error": "Course with the specified ID not found."}

@app.delete("/courses/delete_course")
async def delete_course(course_id: int):
    for index in range(len(courses_db)):
        if courses_db[index].get("id") == course_id:
            del courses_db[index]
            return {"message": "Course deleted successfully."}
        else:
            return {"error": "Course with the specified ID not found."}
