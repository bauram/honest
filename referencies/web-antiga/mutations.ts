// src/lib/actions/mutation.ts
const maxDistanceFactor = 0.2; // 50% of viewport size max
export function mutation(node: HTMLElement) {
    const original = node.cloneNode(true) as HTMLElement;

    function wrapLetters(el: HTMLElement) {
        const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
        const textNodes: Text[] = [];

        while (walker.nextNode()) {
            const current = walker.currentNode as Text;
            if (current.nodeValue?.trim() || current.nodeValue === ' ') {
                textNodes.push(current);
            }
        }

        for (const textNode of textNodes) {
            const parent = textNode.parentElement;
            if (!parent) continue;

            const fragment = document.createDocumentFragment();
            const chars = textNode.nodeValue!.split('');

            for (const char of chars) {
                const wrapper = document.createElement('span');
                wrapper.style.position = 'relative';
                wrapper.style.display = 'inline-block';

                const span = document.createElement('span');
                span.textContent = char;
                span.style.display = 'inline-block';

                wrapper.appendChild(span);
                fragment.appendChild(wrapper);

                if (char === ' ') continue;

                let shape: HTMLDivElement | null = null;

                wrapper.addEventListener('mouseenter', () => {
                    if (shape) return;

                    const size = Math.random() * 100 + 30;
                    shape = document.createElement('div');

                    shape.style.position = 'absolute';
                    shape.style.left = '50%';
                    shape.style.top = '50%';
                    shape.style.transform = 'translate(-50%, -50%)';
                    shape.style.width = `${size}px`;
                    shape.style.height = `${size}px`;
                    shape.style.zIndex = '10';
                    shape.style.backgroundColor = getRandomColor();
                    shape.style.transition = 'transform 0.6s ease, opacity 0.6s ease';
                    shape.style.opacity = '1';
                    shape.style.pointerEvents = 'none';

                    switch (Math.floor(Math.random() * 3)) {
                        case 0:
                            shape.style.borderRadius = '50%';
                            break;
                        case 1:
                            shape.style.borderRadius = '0';
                            break;
                        case 2:
                            shape.style.clipPath = 'polygon(50% 0%, 0% 100%, 100% 100%)';
                            break;
                    }

                    document.body.appendChild(shape);

                    const rect = wrapper.getBoundingClientRect();
                    const centerX = rect.left + rect.width / 2;
                    const centerY = rect.top + rect.height / 2;
                    shape.style.left = `${centerX}px`;
                    shape.style.top = `${centerY}px`;
                    shape.style.transform = 'translate(-50%, -50%) scale(1)';

                    // Set letter color to white
                    span.style.color = 'white';

                    requestAnimationFrame(() => {
                        const maxX = window.innerWidth * maxDistanceFactor;
                        const maxY = window.innerHeight * maxDistanceFactor;
                        const dx = (Math.random() - 0.5) * 2 * maxX;
                        const dy = (Math.random() - 0.5) * 2 * maxY;
                        const scale = Math.random() * 2 + 1;

                        shape!.style.transform = `translate(${dx}px, ${dy}px) scale(${scale})`;
                    });

                    wrapper.addEventListener(
                        'mouseleave',
                        async () => {
                            if (!shape) return;
                            await new Promise((res) => setTimeout(res, 1000));

                            shape.style.transform = 'translate(-50%, -50%) scale(1)';
                            shape.style.opacity = '0';
                            span.style.color = ''; // Reset color

                            setTimeout(() => {
                                shape?.remove();
                                shape = null;
                            }, 600);
                        },
                        { once: true }
                    );
                });
            }

            parent.replaceChild(fragment, textNode);
        }
    }

    function getRandomColor() {
        const colors = ['#387b4f', '#334c80', '#c43e2f', '#f7de50', '#387b4f', '#c43e2f'];
        return colors[Math.floor(Math.random() * colors.length)];
    }

    wrapLetters(node);

    return {
        destroy() {
            node.replaceWith(original);
        }
    };
}