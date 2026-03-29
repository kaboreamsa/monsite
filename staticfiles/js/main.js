// Scripts généraux pour la plateforme

document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss alerts après 5 secondes
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
        alerts.forEach(function(alert) {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Confirmation pour les actions critiques
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Êtes-vous sûr de vouloir supprimer cet élément ? Cette action est irréversible.')) {
                e.preventDefault();
            }
        });
    });

    // Formatage automatique des montants
    const montantInputs = document.querySelectorAll('input[data-montant]');
    montantInputs.forEach(function(input) {
        input.addEventListener('blur', function() {
            let value = parseFloat(this.value.replace(',', '.'));
            if (!isNaN(value)) {
                this.value = value.toFixed(2);
            }
        });
    });

    // Prévisualisation des images uploadées
    const fileInputs = document.querySelectorAll('input[type="file"][data-preview]');
    fileInputs.forEach(function(input) {
        input.addEventListener('change', function() {
            const preview = document.querySelector(this.dataset.preview);
            if (this.files && this.files[0]) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    if (preview) {
                        preview.src = e.target.result;
                        preview.style.display = 'block';
                    }
                };
                reader.readAsDataURL(this.files[0]);
            }
        });
    });

    // Auto-complétion de la date
    const dateInputs = document.querySelectorAll('input[type="date"]:not([value])');
    dateInputs.forEach(function(input) {
        const today = new Date().toISOString().split('T')[0];
        input.value = today;
    });

    // Calcul automatique du total
    const calculateTotal = function() {
        const montantInputs = document.querySelectorAll('.montant-item');
        let total = 0;
        montantInputs.forEach(function(input) {
            const value = parseFloat(input.value) || 0;
            total += value;
        });
        document.getElementById('total-montant').textContent = total.toFixed(2);
    };

    // Écouteurs pour les changements de montant
    document.querySelectorAll('.montant-item').forEach(function(input) {
        input.addEventListener('input', calculateTotal);
    });

    // Initialisation du calcul
    calculateTotal();

    // Animation des cartes au scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate__animated', 'animate__fadeInUp');
            }
        });
    }, observerOptions);

    // Observer les cartes
    document.querySelectorAll('.card').forEach(function(card) {
        observer.observe(card);
    });

    // Menu mobile
    const menuToggle = document.querySelector('.navbar-toggler');
    const sidebar = document.querySelector('.sidebar');
    
    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', function() {
            sidebar.classList.toggle('show');
        });
    }

    // Tooltips Bootstrap
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Popovers Bootstrap
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
});

// Fonction pour formater un montant
function formatMontant(montant) {
    return new Intl.NumberFormat('fr-FR', {
        style: 'currency',
        currency: 'EUR'
    }).format(montant);
}

// Fonction pour copier du texte
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        alert('Copié dans le presse-papier !');
    }).catch(function(err) {
        console.error('Erreur de copie : ', err);
    });
}

// Débounce pour les recherches
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}