/* ==================== LeafSense — Main JavaScript ==================== */
document.addEventListener('DOMContentLoaded', () => {
    initThemeToggle();
    initNavbar();
    initMobileMenu();
    initScrollAnimations();
    initDragDrop();
    initSampleCards();
    initConfidenceBars();
    initFlashMessages();
    initRippleEffects();
});

/* ==================== Theme Toggle ==================== */
function initThemeToggle() {
    const toggle = document.getElementById('themeToggle');
    if (!toggle) return;

    toggle.addEventListener('click', () => {
        // Disable transitions briefly for instant swap
        document.body.classList.add('theme-switching');

        const current = document.documentElement.getAttribute('data-theme') || 'light';
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('leafsense-theme', next);

        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                document.body.classList.remove('theme-switching');
            });
        });
    });
}

/* ==================== Navbar Scroll ==================== */
function initNavbar() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;

    const onScroll = () => {
        navbar.classList.toggle('scrolled', window.scrollY > 20);
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
}

/* ==================== Mobile Menu ==================== */
function initMobileMenu() {
    const btn = document.getElementById('mobileMenuToggle');
    const links = document.getElementById('navLinks');
    if (!btn || !links) return;

    btn.addEventListener('click', () => {
        const isOpen = links.classList.toggle('active');
        // Animate hamburger to X
        const spans = btn.querySelectorAll('span');
        if (isOpen) {
            if (spans[0]) { spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)'; }
            if (spans[1]) { spans[1].style.opacity = '0'; }
            if (spans[2]) { spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)'; }
        } else {
            spans.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
        }
    });

    // Close on link click
    links.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            links.classList.remove('active');
            const spans = btn.querySelectorAll('span');
            spans.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
        });
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
        if (!btn.contains(e.target) && !links.contains(e.target) && links.classList.contains('active')) {
            links.classList.remove('active');
            const spans = btn.querySelectorAll('span');
            spans.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
        }
    });
}

/* ==================== Scroll Animations ==================== */
function initScrollAnimations() {
    const targets = document.querySelectorAll(
        '.feature-card, .step, .plant-badge, .metric-card, .pipeline-step, .plant-coverage-card, ' +
        '.tech-card, .objective-item, .glass-section, .hero-stat, .architecture-flow, .arch-note, ' +
        '.comparison-card, .dataset-stats, .dataset-info-card, .mission-content, .mission-stats, ' +
        '.disclaimer-card, .sample-card'
    );

    if (!targets.length) return;

    // Set initial state
    targets.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    targets.forEach(el => observer.observe(el));
}

/* ==================== Ripple Effect on Buttons ==================== */
function initRippleEffects() {
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('click', function (e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            ripple.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                left: ${e.clientX - rect.left - size / 2}px;
                top: ${e.clientY - rect.top - size / 2}px;
                background: rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                transform: scale(0);
                animation: ripple-effect 0.6s ease-out;
                pointer-events: none;
            `;
            this.appendChild(ripple);
            ripple.addEventListener('animationend', () => ripple.remove());
        });
    });

    // Add ripple keyframes if not present
    if (!document.getElementById('ripple-style')) {
        const style = document.createElement('style');
        style.id = 'ripple-style';
        style.textContent = `@keyframes ripple-effect { to { transform: scale(2.5); opacity: 0; } }`;
        document.head.appendChild(style);
    }
}

/* ==================== Drag & Drop Upload ==================== */
function initDragDrop() {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const previewContainer = document.getElementById('image-preview-container');
    const previewImg = document.getElementById('image-preview');
    const fileInfo = document.getElementById('file-info-text');
    const submitBtn = document.getElementById('submit-btn');
    const uploadForm = document.getElementById('upload-form');

    if (!dropZone || !fileInput) return;

    // Drag events
    ['dragenter', 'dragover'].forEach(evt => {
        dropZone.addEventListener(evt, (e) => {
            e.preventDefault();
            dropZone.classList.add('drag-over');
        });
    });

    ['dragleave', 'drop'].forEach(evt => {
        dropZone.addEventListener(evt, (e) => {
            e.preventDefault();
            dropZone.classList.remove('drag-over');
        });
    });

    // Drop handler
    dropZone.addEventListener('drop', (e) => {
        const files = e.dataTransfer.files;
        if (files.length) {
            handleFile(files[0], fileInput, previewContainer, previewImg, fileInfo, submitBtn);
        }
    });

    // Click to browse
    dropZone.addEventListener('click', () => fileInput.click());

    // File input change
    fileInput.addEventListener('change', () => {
        if (fileInput.files.length) {
            handleFile(fileInput.files[0], fileInput, previewContainer, previewImg, fileInfo, submitBtn);
        }
    });

    // Remove file button
    const removeBtn = document.getElementById('remove-file-btn');
    if (removeBtn) {
        removeBtn.addEventListener('click', () => {
            resetUpload(fileInput, previewContainer, submitBtn);
        });
    }

    // Form submit with error handling
    if (uploadForm) {
        uploadForm.addEventListener('submit', (e) => {
            e.preventDefault();
            if (!fileInput.files.length) return;

            const overlay = document.getElementById('loading-overlay');
            if (overlay) overlay.style.display = 'flex';

            const formData = new FormData(uploadForm);
            fetch(uploadForm.action, {
                method: 'POST',
                body: formData
            }).then(res => {
                if (res.status === 413) {
                    if (overlay) overlay.style.display = 'none';
                    Swal.fire({
                        icon: 'error',
                        title: 'File Too Large',
                        text: 'The file exceeds the 10 MB size limit. Please upload a smaller image.',
                        confirmButtonColor: 'var(--primary, #2E7D32)'
                    });
                    return;
                }
                if (res.redirected) {
                    window.location.href = res.url;
                    return;
                }
                return res.text();
            }).then(html => {
                if (html) {
                    document.open();
                    document.write(html);
                    document.close();
                    window.history.pushState({}, '', uploadForm.action);
                }
            }).catch(() => {
                if (overlay) overlay.style.display = 'none';
                Swal.fire({
                    icon: 'error',
                    title: 'Upload Failed',
                    text: 'Something went wrong. Please try again.',
                    confirmButtonColor: 'var(--primary, #2E7D32)'
                });
            });
        });
    }
}

function handleFile(file, fileInput, previewContainer, previewImg, fileInfo, submitBtn) {
    const validTypes = ['image/jpeg', 'image/png', 'image/webp', 'image/bmp'];
    if (!validTypes.includes(file.type)) {
        Swal.fire({
            icon: 'error',
            title: 'Invalid File Type',
            text: 'Please upload a valid image file (JPEG, PNG, WebP, or BMP).',
            confirmButtonColor: 'var(--primary, #2E7D32)'
        });
        return;
    }

    const maxSize = 10 * 1024 * 1024; // 10MB (matches server limit)
    if (file.size > maxSize) {
        Swal.fire({
            icon: 'error',
            title: 'File Too Large',
            text: `File size is ${(file.size / (1024 * 1024)).toFixed(1)} MB. Maximum allowed size is 10 MB.`,
            confirmButtonColor: 'var(--primary, #2E7D32)'
        });
        return;
    }

    // Update file input
    const dt = new DataTransfer();
    dt.items.add(file);
    fileInput.files = dt.files;

    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
        if (previewImg) previewImg.src = e.target.result;
        if (previewContainer) previewContainer.classList.add('active');
    };
    reader.readAsDataURL(file);

    // Show file info
    if (fileInfo) {
        const sizeMB = (file.size / (1024 * 1024)).toFixed(2);
        fileInfo.textContent = `${file.name} (${sizeMB} MB)`;
    }

    // Enable submit
    if (submitBtn) submitBtn.disabled = false;
}

function resetUpload(fileInput, previewContainer, submitBtn) {
    if (fileInput) fileInput.value = '';
    if (previewContainer) previewContainer.classList.remove('active');
    if (submitBtn) submitBtn.disabled = true;
}

/* ==================== Sample Cards ==================== */
function initSampleCards() {
    document.querySelectorAll('.sample-card').forEach(card => {
        card.addEventListener('click', () => {
            const imgSrc = card.dataset.src;
            const imgName = card.dataset.name;
            if (!imgSrc) return;

            // Fetch sample image and submit
            const overlay = document.getElementById('loading-overlay');
            if (overlay) overlay.style.display = 'flex';

            fetch(imgSrc)
                .then(res => res.blob())
                .then(blob => {
                    const file = new File([blob], imgName || 'sample.jpg', { type: blob.type });
                    const dt = new DataTransfer();
                    dt.items.add(file);

                    const fileInput = document.getElementById('file-input');
                    if (fileInput) {
                        fileInput.files = dt.files;
                        const form = document.getElementById('upload-form');
                        if (form) form.submit();
                    }
                })
                .catch(() => {
                    if (overlay) overlay.style.display = 'none';
                    Swal.fire({
                        icon: 'error',
                        title: 'Load Failed',
                        text: 'Failed to load sample image. Please try again.',
                        confirmButtonColor: 'var(--primary, #2E7D32)'
                    });
                });
        });
    });
}

/* ==================== Confidence Bars ==================== */
function initConfidenceBars() {
    const bars = document.querySelectorAll('.confidence-fill');
    if (bars.length === 0) return;

    // Animate after a short delay
    setTimeout(() => {
        bars.forEach(bar => {
            const target = bar.dataset.width;
            if (target) bar.style.width = target + '%';
        });
    }, 300);
}

/* ==================== Flash Messages ==================== */
function initFlashMessages() {
    document.querySelectorAll('.flash-message').forEach(msg => {
        setTimeout(() => {
            msg.style.opacity = '0';
            msg.style.transform = 'translateX(100%)';
            setTimeout(() => msg.remove(), 300);
        }, 5000);
    });
}
