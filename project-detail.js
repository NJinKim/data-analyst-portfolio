// 프로젝트 상세 페이지 JavaScript

document.addEventListener('DOMContentLoaded', function() {
    
    // 맨 위로 이동 버튼 기능
    const scrollToTopBtn = document.querySelector('.scroll-to-top-btn');
    if (scrollToTopBtn) {
        scrollToTopBtn.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
        
        // 스크롤 위치에 따라 버튼 표시/숨김
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                scrollToTopBtn.style.display = 'flex';
            } else {
                scrollToTopBtn.style.display = 'none';
            }
        });
        
        // 초기 상태 설정
        scrollToTopBtn.style.display = 'none';
    }
    
    // 프로젝트 네비게이션 기능
    const projectNavLinks = document.querySelectorAll('.project-nav-link');
    const projectSections = document.querySelectorAll('[id^="project"]');
    
    // 스크롤 위치에 따라 활성 링크 업데이트
    function updateActiveNavLink() {
        const scrollPosition = window.pageYOffset + 100;
        
        projectSections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionBottom = sectionTop + section.offsetHeight;
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
                // 모든 링크에서 active 클래스 제거
                projectNavLinks.forEach(link => {
                    link.classList.remove('active');
                });
                
                // 해당 섹션의 링크에 active 클래스 추가
                const activeLink = document.querySelector(`[href="#${section.id}"]`);
                if (activeLink) {
                    activeLink.classList.add('active');
                }
            }
        });
    }
    
    // 스크롤 이벤트 리스너 추가
    if (projectNavLinks.length > 0) {
        window.addEventListener('scroll', updateActiveNavLink);
        
        // 네비게이션 링크 클릭 이벤트
        projectNavLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href').substring(1);
                const targetSection = document.getElementById(targetId);
                
                if (targetSection) {
                    const headerHeight = document.querySelector('.project-header').offsetHeight;
                    const targetPosition = targetSection.offsetTop - headerHeight - 20;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });
        
        // 초기 활성 링크 설정
        updateActiveNavLink();
    }
    
    // 부드러운 스크롤을 위한 CSS 추가
    const style = document.createElement('style');
    style.textContent = `
        html {
            scroll-behavior: smooth;
        }
    `;
    document.head.appendChild(style);
}); 