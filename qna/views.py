from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    """
    Q&A 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    # 조회
    question_list = Question.objects.order_by('-create_date')
    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, './qna/question_list.html', context)


def detail(request, question_id):
    """
    Q&A 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, './qna/question_detail.html', context)

@login_required(login_url='common:login')
# 비로그인 시 질문 작성을 하면 오류페이지가 발생하도록 하는게 아닌 로그인을 요구하는 페이지로 이동하게
def answer_create(request, question_id):
    """
    Q&A 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.CustomUser  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('qna:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'qna/question_detail.html', context)
    # render, redirect 개념 정리 answer_create같은 경우 url이 아닌 int:question이라 다르게 연결 (urls.py참조)

@login_required(login_url='common:login')
def question_create(request):
    """
    Q&A 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.CustomUser  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('qna:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'qna/question_form.html', context)