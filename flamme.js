const canvas = document.getElementById('flames');
const ctx = canvas.getContext('2d');

// Ajuster la taille du canvas
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

// Configuration des particules
const particles = [];
const colors = ['rgba(255, 69, 0, 0.5)', 'rgba(255, 140, 0, 0.5)', 'rgba(255, 255, 0, 0.3)'];

function createParticle(x, y) {
    const size = Math.random() * 5 + 2;
    const speed = Math.random() * 3 + 1;
    const angle = Math.random() * Math.PI * 2;

    return {
        x: x,
        y: y,
        size: size,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed,
        alpha: 1,
        color: colors[Math.floor(Math.random() * colors.length)],
    };
}

// Animation des particules
function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Ajouter des particules aléatoires
    for (let i = 0; i < 10; i++) {
        particles.push(createParticle(Math.random() * canvas.width, canvas.height));
    }

    // Mettre à jour les particules
    for (let i = 0; i < particles.length; i++) {
        const p = particles[i];

        p.x += p.vx;
        p.y -= p.vy;
        p.alpha -= 0.01;

        // Dessiner les particules
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fillStyle = p.color.replace('0.5', p.alpha.toFixed(2));
        ctx.fill();

        // Supprimer les particules mortes
        if (p.alpha <= 0) {
            particles.splice(i, 1);
            i--;
        }
    }

    requestAnimationFrame(animateParticles);
}

animateParticles();
