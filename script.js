// Matrix Digital Rain Animation
const canvas = document.getElementById('matrix-canvas');
if (canvas) {
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const chars = '01';
    const fontSize = 14;
    const columns = canvas.width / fontSize;
    const drops = [];

    for (let i = 0; i < columns; i++) {
        drops[i] = 1;
    }

    function draw() {
        ctx.fillStyle = 'rgba(5, 5, 26, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#0F0';
        ctx.font = fontSize + 'px monospace';

        for (let i = 0; i < drops.length; i++) {
            const text = chars.charAt(Math.floor(Math.random() * chars.length));
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);

            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i]++;
        }
    }

    setInterval(draw, 33);

    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
}

// Navbar Scroll Effect
window.addEventListener('scroll', () => {
    const nav = document.getElementById('navbar');
    if (window.scrollY > 50) {
        nav.classList.add('bg-blue-950/80', 'backdrop-blur-xl', 'py-4', 'border-b', 'border-white/10');
        nav.classList.remove('py-8');
    } else {
        nav.classList.remove('bg-blue-950/80', 'backdrop-blur-xl', 'py-4', 'border-b', 'border-white/10');
        nav.classList.add('py-8');
    }
});

// Mobile Menu
function toggleMobileMenu() {
    const menu = document.getElementById('mobileMenu');
    const isHidden = menu.classList.contains('hidden');

    if (isHidden) {
        menu.classList.remove('hidden');
        setTimeout(() => {
            menu.classList.remove('opacity-0');
        }, 10);
    } else {
        menu.classList.add('opacity-0');
        setTimeout(() => {
            menu.classList.add('hidden');
        }, 300);
    }
}

// Initialize Lucide Icons
lucide.createIcons();

// Back to Top Button
const backToTopBtn = document.getElementById('backToTop');

window.addEventListener('scroll', () => {
    if (backToTopBtn) {
        if (window.scrollY > 300) {
            backToTopBtn.classList.remove('opacity-0', 'translate-y-10', 'pointer-events-none');
        } else {
            backToTopBtn.classList.add('opacity-0', 'translate-y-10', 'pointer-events-none');
        }
    }
});

function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}
