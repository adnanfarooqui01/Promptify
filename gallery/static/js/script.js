// ===== DOM Content Loaded =====
document.addEventListener("DOMContentLoaded", () => {
    // Copy prompt button functionality (keep your existing feature)
    const copyButtons = document.querySelectorAll(".copy-btn");
    
    copyButtons.forEach(btn => {
        btn.addEventListener("click", (e) => {
            e.preventDefault();
            e.stopPropagation();
            
            const prompt = btn.getAttribute("data-prompt");
            
            navigator.clipboard.writeText(prompt).then(() => {
                // Change button appearance
                btn.innerHTML = '<i class="bi bi-check"></i>';
                btn.classList.add('copied');
                
                // Reset after 2 seconds
                setTimeout(() => {
                    btn.innerHTML = '<i class="bi bi-clipboard"></i>';
                    btn.classList.remove('copied');
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy:', err);
            });
        });
    });

    // Keep the existing menu toggle if you had mobile menu
    const menuToggle = document.getElementById("menu-toggle");
    if (menuToggle) {
        menuToggle.addEventListener("click", function() {
            document.querySelector(".sidebar").classList.toggle("active");
        });
    }
});



