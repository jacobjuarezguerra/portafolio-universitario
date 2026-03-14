const CORRECT_PASSWORD = 'marranapuerk';

document.addEventListener('DOMContentLoaded', function() {
    initTheme();
    initNavigation();
    initScrollAnimations();
    initMobileMenu();
    initLoginForm();
});

function initTheme() {
    const themeToggle = document.getElementById('theme-toggle');
    const savedTheme = localStorage.getItem('theme');
    
    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
        updateThemeIcon(savedTheme);
    }
    
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
            
            console.log('Theme changed to:', newTheme);
        });
    }
}

function updateThemeIcon(theme) {
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
    }
}

function initNavigation() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-links a');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage || (currentPage === '' && href === 'index.html')) {
            link.classList.add('active');
        }
    });
}

function initScrollAnimations() {
    const sections = document.querySelectorAll('.section');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    sections.forEach(section => {
        observer.observe(section);
    });
}

function initMobileMenu() {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navLinks.classList.toggle('active');
        });
        
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });
    }
}

function initLoginForm() {
    const loginForm = document.getElementById('login-form');
    
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const passwordInput = document.getElementById('password');
            const errorMsg = document.querySelector('.error-msg');
            const successMsg = document.querySelector('.success-msg');
            const formContainer = document.querySelector('.login-form');
            
            const enteredPassword = passwordInput.value;
            
            console.log('Login attempt:', enteredPassword === CORRECT_PASSWORD ? 'SUCCESS' : 'FAILED');
            
            if (enteredPassword === CORRECT_PASSWORD) {
                localStorage.setItem('privateAccess', 'granted');
                localStorage.setItem('accessTime', Date.now());
                
                errorMsg.classList.remove('show');
                successMsg.classList.add('show');
                
                setTimeout(() => {
                    showPrivateContent();
                }, 500);
            } else {
                errorMsg.classList.add('show');
                successMsg.classList.remove('show');
                
                passwordInput.value = '';
                passwordInput.focus();
            }
        });
    }
    
    checkPrivateAccess();
}

function checkPrivateAccess() {
    const privateContent = document.getElementById('private-content');
    const loginForm = document.getElementById('login-form-container');
    
    if (privateContent && loginForm) {
        const access = localStorage.getItem('privateAccess');
        const accessTime = localStorage.getItem('accessTime');
        
        const oneHour = 60 * 60 * 1000;
        const isExpired = accessTime && (Date.now() - accessTime > oneHour);
        
        if (access === 'granted' && !isExpired) {
            showPrivateContent();
        } else {
            showLoginForm();
        }
    }
}

function showPrivateContent() {
    const privateContent = document.getElementById('private-content');
    const loginForm = document.getElementById('login-form-container');
    
    if (loginForm) {
        loginForm.style.display = 'none';
    }
    if (privateContent) {
        privateContent.style.display = 'block';
        privateContent.classList.add('visible');
    }
    
    console.log('Private content displayed');
}

function showLoginForm() {
    const privateContent = document.getElementById('private-content');
    const loginForm = document.getElementById('login-form-container');
    
    if (privateContent) {
        privateContent.style.display = 'none';
    }
    if (loginForm) {
        loginForm.style.display = 'block';
    }
}

function logout() {
    localStorage.removeItem('privateAccess');
    localStorage.removeItem('accessTime');
    showLoginForm();
    console.log('User logged out');
}
