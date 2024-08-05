import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from django.shortcuts import render
from .forms import UploadFileForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.conf import settings

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            file_path = default_storage.save(f'tmp/{file.name}', ContentFile(file.read()))

            # Redirect to results view with the file path
            return HttpResponseRedirect(f'results/{file.name}')
    else:
        form = UploadFileForm()
    return render(request, 'analysis/index.html', {'form': form})

def results(request, filename):
    file_path = default_storage.path(f'tmp/{filename}')
    df = pd.read_csv(file_path)

    # Basic data analysis before handling missing values
    head_before = df.head().to_html(classes='table table-striped')
    description_before = df.describe().to_html(classes='table table-striped')
    missing_values_before = df.isnull().sum().to_dict()

    # Automatically fill missing values with mean
    df = df.fillna(df.mean())

    # Data analysis after handling missing values
    head_after = df.head().to_html(classes='table table-striped')
    description_after = df.describe().to_html(classes='table table-striped')
    missing_values_after = df.isnull().sum().to_dict()

    return render(request, 'analysis/results.html', {
        'head_before': head_before,
        'description_before': description_before,
        'missing_values_before': missing_values_before,
        'head_after': head_after,
        'description_after': description_after,
        'missing_values_after': missing_values_after,
        'filename': filename
    })

def visualizations(request, filename):
    file_path = default_storage.path(f'tmp/{filename}')
    df = pd.read_csv(file_path)

    # Automatically fill missing values with mean
    df = df.fillna(df.mean())

    # Create a directory to save plots
    plot_dir = os.path.join('media', 'plots', filename)
    os.makedirs(plot_dir, exist_ok=True)

    # Generate histograms for numerical columns
    numerical_columns = df.select_dtypes(include='number').columns
    plot_paths = []
    for column in numerical_columns:
        plt.figure()
        sns.histplot(df[column], kde=True)
        plot_path = os.path.join(plot_dir, f'{column}.png')
        plt.savefig(plot_path)  # Save the plot
        plt.close()  # Close the figure to free up memory
        plot_paths.append(os.path.join(settings.MEDIA_URL, 'plots', filename, f'{column}.png'))

    return render(request, 'analysis/visualizations.html', {
        'plot_paths': plot_paths,
        'filename': filename
    })
