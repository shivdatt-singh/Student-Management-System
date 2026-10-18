
from django.shortcuts import render , redirect
from .models import Student
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('student_list')

def update_student(request,student_id):
    student = Student.objects.get(id=student_id)
    
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll_number = request.POST.get('roll_number')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')

        student.save()
        return redirect('student_list')

    return render(request, 'update_student.html', {'student': student})


def student_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        email = request.POST.get('email')
        age = request.POST.get('age')

        Student.objects.create(
            name=name,
            roll_number=roll_number,
            email=email,
            age=age
        )
        return redirect('student_list')

    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
