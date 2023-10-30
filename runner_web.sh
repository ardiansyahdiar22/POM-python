# Menyimpan argumen yang diberikan saat menjalankan script
TAGS=@login_on_web_app

# Pindah ke direktori proyek Behave Anda
cd /Users/avows/Documents/coding/python_test

# Jalankan Behave dengan formatter Allure dan tagging yang diberikan
behave -f allure_behave.formatter:AllureFormatter -o ./reports/allure-results ./features --tags=$TAGS

# Jalankan laporan Allure
allure serve ./reports/allure-results
