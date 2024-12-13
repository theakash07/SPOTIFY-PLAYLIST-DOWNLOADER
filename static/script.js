async function downloadPlaylist(event) {
    event.preventDefault();
    const urlInput = document.getElementById('url');
    const spinner = document.getElementById('spinner');
    const message = document.getElementById('message');

    message.innerHTML = '';
    spinner.style.display = 'block';

    try {
        const response = await fetch('/download', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: `url=${encodeURIComponent(urlInput.value)}`
        });

        spinner.style.display = 'none';

        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'playlist.zip';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            message.innerHTML = '<div class="alert alert-success">Download started successfully!</div>';
        } else {
            const error = await response.json();
            message.innerHTML = `<div class="alert alert-danger">Error: ${error.error}</div>`;
        }
    } catch (err) {
        spinner.style.display = 'none';
        message.innerHTML = `<div class="alert alert-danger">An unexpected error occurred: ${err.message}</div>`;
    }
}
