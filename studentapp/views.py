
from django.shortcuts import render , redirect
from .models import Student
from .forms import StudentForm
from django.db.models import Q
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('student_list')


def update_student(request, student_id):
    student = Student.objects.get(id=student_id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    return render(request, 'update_student.html', {
        'student': student,
        'form': form
    })





def student_list(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    search_query = request.GET.get('search', '')
    students = Student.objects.all()
    total_students = Student.objects.count()
    if search_query:
        if search_query.isdigit():
            students = students.filter(
                Q(name__icontains=search_query) |
                Q(roll_number=int(search_query))
            )
        else:
            students = students.filter(
                name__icontains=search_query
            )

    return render(request, 'student_list.html', {
        'students': students,
        'form': form,
        'total_students': total_students
    })
