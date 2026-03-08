// ==================== DOM Elements ====================
const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const previewContainer = document.getElementById('preview-container');
const imagePreview = document.getElementById('image-preview');
const removePreview = document.getElementById('remove-preview');
const submitBtn = document.getElementById('submit-btn');
const uploadForm = document.getElementById('upload-form');
const loadingOverlay = document.getElementById('loading-overlay');

const ALLOWED_TYPES = ['image/png', 'image/jpeg', 'image/jpg'];
const MAX_SIZE = 10 * 1024 * 1024; // 10 MB

// ==================== Drag & Drop ====================
if (dropZone) {
    ['dragenter', 'dragover'].forEach(evt => {
        dropZone.addEventListener(evt, e => {
            e.preventDefault();
            e.stopPropagation();
            dropZone.classList.add('drag-over');
        });
    });

    ['dragleave', 'drop'].forEach(evt => {
        dropZone.addEventListener(evt, e => {
            e.preventDefault();
            e.stopPropagation();
            dropZone.classList.remove('drag-over');
        });
    });

    dropZone.addEventListener('drop', e => {
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            handleFile(files[0]);
        }
    });

    // Click on zone (but not on buttons) triggers file input
    dropZone.addEventListener('click', e => {
        if (e.target === dropZone || e.target.closest('.drop-zone-content')) {
            fileInput.click();
        }
    });
}

// ==================== File Input ====================
if (fileInput) {
    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            handleFile(fileInput.files[0]);
        }
    });
}

// ==================== Handle File ====================
function handleFile(file) {
    // Validate type
    if (!ALLOWED_TYPES.includes(file.type)) {
        alert('Invalid file type. Please upload a PNG, JPG, or JPEG image.');
        return;
    }

    // Validate size
    if (file.size > MAX_SIZE) {
        alert('File too large. Maximum size is 10 MB.');
        return;
    }

    // Set file to input
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    fileInput.files = dataTransfer.files;

    // Show preview
    const reader = new FileReader();
    reader.onload = e => {
        imagePreview.src = e.target.result;
        previewContainer.style.display = 'block';
        document.querySelector('.drop-zone-content').style.display = 'none';
        submitBtn.disabled = false;
    };
    reader.readAsDataURL(file);
}

// ==================== Remove Preview ====================
if (removePreview) {
    removePreview.addEventListener('click', e => {
        e.stopPropagation();
        fileInput.value = '';
        previewContainer.style.display = 'none';
        document.querySelector('.drop-zone-content').style.display = 'block';
        submitBtn.disabled = true;
    });
}

// ==================== Form Submit — Loading Spinner ====================
if (uploadForm) {
    uploadForm.addEventListener('submit', () => {
        if (fileInput.files.length > 0) {
            loadingOverlay.style.display = 'flex';
        }
    });
}

// ==================== Sample Image Click ====================
function submitSample(imgElement) {
    const imageUrl = imgElement.getAttribute('data-src');
    const filename = imgElement.getAttribute('data-filename');

    // Show loading
    if (loadingOverlay) {
        loadingOverlay.style.display = 'flex';
    }

    // Fetch the sample image as a blob and submit via form
    fetch(imageUrl)
        .then(resp => resp.blob())
        .then(blob => {
            const file = new File([blob], filename, { type: blob.type });
            const formData = new FormData();
            formData.append('file', file);

            // Submit via hidden form
            const form = imgElement.closest('.sample-form');
            const dt = new DataTransfer();
            dt.items.add(file);
            form.querySelector('.sample-file-input').files = dt.files;
            form.submit();
        })
        .catch(() => {
            if (loadingOverlay) loadingOverlay.style.display = 'none';
            alert('Failed to load sample image. Please try uploading manually.');
        });
}
