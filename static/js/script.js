// Variável de controle para verificar se a animação já foi executada
var animationExecuted = false;

// Função para verificar se o elemento está visível na tela
function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Função para verificar a visibilidade do elemento e adicionar classe se estiver visível
function checkVisibility() {
    var elements = document.querySelectorAll('.animate-text');
    elements.forEach(function (element) {
        if (isElementInViewport(element)) {
            if (!animationExecuted) {
                animateText(element);
                animationExecuted = true;
            }
        }
    });
}

// Função para animar o texto
function animateText(element) {
    var text = element.textContent;
    element.textContent = '';
    var index = 0;

    function addLetter() {
        if (index < text.length) {
            element.textContent += text.charAt(index);
            index++;
            setTimeout(addLetter, 2); // ajuste o tempo conforme desejado
        }
    }

    addLetter();
}

window.addEventListener('scroll', checkVisibility);

window.addEventListener('load', function () {
    if (!animationExecuted) {
        checkVisibility(); // Verificar a visibilidade dos elementos quando a página é carregada
    }
});





