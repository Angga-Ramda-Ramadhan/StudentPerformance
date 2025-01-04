document.getElementById('predictButton').addEventListener('click', async function (event) {
    event.preventDefault(); // Mencegah form submit standar

    // Ambil input dari form
    const studyHours = document.getElementById('study_hours').value;
    const sleepHours = document.getElementById('sleep_hours').value;
    const socioeconomicScore = document.getElementById('socioeconomic_score').value;
    const attendance = document.getElementById('attendance').value;

    // Validasi untuk memastikan input tidak kosong
    if (!studyHours || !sleepHours || !socioeconomicScore || !attendance) {
        alert("All fields are required!");
        return;
    }

    try {
        // Kirim data ke server menggunakan fetch
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'Socioeconomic Score': parseFloat(socioeconomicScore),  // Mengonversi string ke angka
                'Study Hours': parseFloat(studyHours),                   // Mengonversi string ke angka
                'Sleep Hours': parseFloat(sleepHours),                   // Mengonversi string ke angka
                'Attendance (%)': parseFloat(attendance), 
            }),
        });
        console.log({
            'Socioeconomic Score': parseFloat(socioeconomicScore),  // Mengonversi string ke angka
            'Study Hours': parseFloat(studyHours),                   // Mengonversi string ke angka
            'Sleep Hours': parseFloat(sleepHours),                   // Mengonversi string ke angka
            'Attendance (%)': parseFloat(attendance), 
        });

        // Cek apakah respons berhasil
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'An unknown error occurred.');
        }

        const result = await response.json();
        document.getElementById('result').innerText = `Predicted Grade: ${result.result}`;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'An error occurred. Please try again.';
    }
});
