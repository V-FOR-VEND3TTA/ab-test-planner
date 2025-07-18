from django.shortcuts import render, redirect, get_object_or_404
from .forms import ABTestForm, ABTestVariantForm, ABTestOutcomeForm
from .models import ABTest, ABTestVariant, ABTestOutcome

def home(request):
    tests = ABTest.objects.all()
    return render(request, 'tests/home.html', {'tests': tests})

def create_test(request):
    if request.method == 'POST':
        form = ABTestForm(request.POST)
        if form.is_valid():
            test = form.save()
            return redirect('view_test', test_id=test.id)
    else:
        form = ABTestForm()
    return render(request, 'tests/create_test.html', {'form': form})

def view_test(request, test_id):
    test = get_object_or_404(ABTest, pk=test_id)
    variant_form = ABTestVariantForm()
    outcome_form = ABTestOutcomeForm()
    return render(request, 'tests/view_test.html', {
        'test': test,
        'variant_form': variant_form,
        'outcome_form': outcome_form,
    })

def add_variant(request, test_id):
    test = get_object_or_404(ABTest, pk=test_id)
    if request.method == 'POST':
        form = ABTestVariantForm(request.POST)
        if form.is_valid():
            variant = form.save(commit=False)
            variant.test = test
            variant.save()
            return redirect('view_test', test_id=test.id)
    return redirect('view_test', test_id=test.id)

def add_outcome(request, test_id):
    test = get_object_or_404(ABTest, pk=test_id)
    if request.method == 'POST':
        form = ABTestOutcomeForm(request.POST)
        if form.is_valid():
            outcome = form.save(commit=False)
            outcome.test = test
            outcome.save()
            return redirect('view_test', test_id=test.id)
    return redirect('view_test', test_id=test.id)
