// DOM이 로드된 후 실행
document.addEventListener('DOMContentLoaded', function() {
    
    // 페이지 로드 시 저장된 스크롤 위치로 이동
    const savedScrollPosition = localStorage.getItem('mainPageScrollPosition');
    if (savedScrollPosition) {
        setTimeout(() => {
            window.scrollTo(0, parseInt(savedScrollPosition));
            localStorage.removeItem('mainPageScrollPosition');
        }, 100);
    }
    
    // 모바일 햄버거 메뉴 토글 기능
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
        
        // 메뉴 링크 클릭 시 모바일 메뉴 닫기
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }
    
    // 스크롤 시 네비게이션 바 스타일 변경
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 100) {
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0,0,0,0.1)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = '0 5px 15px rgba(0,0,0,0.1)';
        }
    });
    
    // 스킬 바 애니메이션 (스크롤 시 실행)
    const skillBars = document.querySelectorAll('.skill-progress');
    
    function animateSkillBars() {
        skillBars.forEach(bar => {
            const rect = bar.getBoundingClientRect();
            const isVisible = rect.top < window.innerHeight && rect.bottom > 0;
            
            if (isVisible) {
                const width = bar.style.width;
                bar.style.width = '0%';
                setTimeout(() => {
                    bar.style.width = width;
                }, 100);
            }
        });
    }
    
    // 스크롤 이벤트에 스킬 바 애니메이션 추가
    window.addEventListener('scroll', animateSkillBars);
    
    // 페이지 로드 시 스킬 바 애니메이션 실행
    animateSkillBars();
    
    // 부드러운 스크롤 기능 (네비게이션 링크 클릭 시)
    const navLinks = document.querySelectorAll('a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const offsetTop = targetSection.offsetTop - 70; // 네비게이션 바 높이만큼 조정
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // 스크롤 시 현재 섹션 하이라이트
    function highlightCurrentSection() {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-link');
        
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            const sectionHeight = section.clientHeight;
            
            if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    }
    
    window.addEventListener('scroll', highlightCurrentSection);
    
    // 현재 섹션 하이라이트를 위한 CSS 클래스 추가
    const style = document.createElement('style');
    style.textContent = `
        .nav-link.active {
            color: var(--secondary-color) !important;
        }
        .nav-link.active::after {
            width: 100% !important;
        }
    `;
    document.head.appendChild(style);
    
    // 프로젝트 카드 클릭 이벤트
    const projectCards = document.querySelectorAll('.project-card');
    
    projectCards.forEach(card => {
        card.addEventListener('click', function() {
            const projectId = this.getAttribute('data-project');
            if (projectId) {
                // 현재 스크롤 위치를 localStorage에 저장
                localStorage.setItem('mainPageScrollPosition', window.pageYOffset.toString());
                
                // 프로젝트 상세 페이지로 이동
                window.location.href = `${projectId}.html`;
            }
        });
        
        // 호버 효과 개선
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // 목차 아이템 호버 효과 개선
    const tocItems = document.querySelectorAll('.toc-item');
    
    tocItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.03)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // 자격증 아이템 호버 효과
    const certificationItems = document.querySelectorAll('.certification-item');
    
    certificationItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // 연락처 링크 클릭 효과
    const contactLinks = document.querySelectorAll('.contact-link');
    
    contactLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // 이메일이나 전화번호 링크가 아닌 경우에만 기본 동작 방지
            if (!this.href.startsWith('mailto:') && !this.href.startsWith('tel:')) {
                e.preventDefault();
            }
            
            // 클릭 효과
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });
    
    // 페이지 로드 시 페이드인 애니메이션
    function fadeInElements() {
        const elements = document.querySelectorAll('.timeline-item, .project-card, .skill-item, .certification-item');
        
        elements.forEach((element, index) => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(30px)';
            
            setTimeout(() => {
                element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }, index * 100);
        });
    }
    
    // 페이지 로드 후 애니메이션 실행
    setTimeout(fadeInElements, 500);
    
    // 스크롤 시 요소들 페이드인 애니메이션
    function fadeInOnScroll() {
        const elements = document.querySelectorAll('.timeline-item, .project-card, .skill-item, .certification-item');
        
        elements.forEach(element => {
            const rect = element.getBoundingClientRect();
            const isVisible = rect.top < window.innerHeight * 0.8;
            
            if (isVisible) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    }
    
    window.addEventListener('scroll', fadeInOnScroll);
    
    // 초기 상태 설정
    fadeInOnScroll();
    
    // 햄버거 메뉴 애니메이션
    if (hamburger) {
        hamburger.addEventListener('click', function() {
            const bars = this.querySelectorAll('.bar');
            
            bars.forEach((bar, index) => {
                if (this.classList.contains('active')) {
                    // X 모양으로 변환
                    if (index === 0) {
                        bar.style.transform = 'rotate(45deg) translate(5px, 5px)';
                    } else if (index === 1) {
                        bar.style.opacity = '0';
                    } else if (index === 2) {
                        bar.style.transform = 'rotate(-45deg) translate(7px, -6px)';
                    }
                } else {
                    // 원래 모양으로 복원
                    bar.style.transform = 'none';
                    bar.style.opacity = '1';
                }
            });
        });
    }
    
    // 터치 디바이스에서 호버 효과 개선
    if ('ontouchstart' in window) {
        const touchElements = document.querySelectorAll('.project-card, .toc-item, .certification-item');
        
        touchElements.forEach(element => {
            element.addEventListener('touchstart', function() {
                this.style.transform = 'translateY(-5px) scale(1.02)';
            });
            
            element.addEventListener('touchend', function() {
                setTimeout(() => {
                    this.style.transform = 'translateY(0) scale(1)';
                }, 200);
            });
        });
    }
    
    // 키보드 접근성 개선
    document.addEventListener('keydown', function(e) {
        // ESC 키로 모바일 메뉴 닫기
        if (e.key === 'Escape' && navMenu && navMenu.classList.contains('active')) {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        }
    });
    
    // 로딩 완료 후 초기화
    window.addEventListener('load', function() {
        // 페이지 로드 완료 후 추가 애니메이션
        document.body.style.opacity = '1';
        
        // 스킬 바 애니메이션 재실행
        setTimeout(animateSkillBars, 500);
    });
    
    // 페이지 로드 시 body 페이드인
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
});

// 성능 최적화를 위한 스크롤 이벤트 쓰로틀링
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// 쓰로틀링 적용
window.addEventListener('scroll', throttle(function() {
    // 스크롤 이벤트 핸들러들
}, 16)); // 약 60fps 