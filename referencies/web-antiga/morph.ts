// src/lib/effects/morph.ts
import * as opentype from 'opentype.js';
import * as flubber from 'flubber';

let font: opentypejs.Font | null = null;

async function loadFont(): Promise<opentypejs.Font> {
    if (font) return font;
    return new Promise((resolve, reject) => {
        import('$lib/static/fonts/Roboto/static/Roboto-Regular.ttf').then(({ default: fontUrl }) => {
            opentype.load(fontUrl, (err, loaded) => {
                if (err || !loaded) reject(err);
                else {
                    font = loaded;
                    resolve(loaded);
                }
            });
        });
    });
}

function getPathForLetter(letter: string): string {
    if (!font) throw new Error('Font not loaded');
    const path = font.getPath(letter, 0, 72, 72);
    return path.toPathData(2);
}

function createSvg(d: string): SVGSVGElement {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');

    svg.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    svg.setAttribute('width', '100vw');
    svg.setAttribute('height', '100vh');
    svg.setAttribute('viewBox', '0 0 100 100');
    svg.style.position = 'fixed';
    svg.style.left = '0';
    svg.style.top = '0';
    svg.style.zIndex = '9999';
    svg.style.pointerEvents = 'none';
    svg.style.color = 'inherit';
    svg.style.fill = 'currentColor';
    svg.style.overflow = 'visible';

    path.setAttribute('d', d);
    path.setAttribute('fill', 'currentColor');
    svg.appendChild(path);
    return svg;
}

function getRandomTargetPath(minSize = 20): string {
    const basePath = 'M0,0h100v100h-100z';
    const getRandom = (min: number, max: number) => Math.random() * (max - min) + min;

    const size = getRandom(minSize, 60);
    const cx = 50;
    const cy = 50;

    const circle = flubber.toCircle(basePath, cx, cy, size)(1);
    const rect = flubber.toRect(basePath, cx - size / 2, cy - size / 2, cx + size / 2, cy + size / 2)(1);
    const triangle = `M${50},${50 - size} L${50 + size},${50 + size} L${50 - size},${50 + size} Z`;

    const shapes = [circle, rect, triangle];
    return shapes[Math.floor(Math.random() * shapes.length)];
}

function interpolateTransform(from: string, to: string): (t: number) => string {
    const fromMatch = from.match(/translate\(([^ ]+) ([^ ]+)\) scale\(([^)]+)\)/);
    const toMatch = to.match(/translate\(([^ ]+) ([^ ]+)\) scale\(([^)]+)\)/);

    if (!fromMatch || !toMatch) return () => to;

    const [fx, fy, fs] = fromMatch.slice(1).map(Number);
    const [tx, ty, ts] = toMatch.slice(1).map(Number);

    return (t: number) => {
        const x = fx + (tx - fx) * t;
        const y = fy + (ty - fy) * t;
        const s = fs + (ts - fs) * t;
        return `translate(${x} ${y}) scale(${s}) translate(-50 -50)`;
    };
}

function easeInOutCubic(t: number): number {
    return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
}

export function morph(node: HTMLElement) {
    (async () => {
        await loadFont();
        const text = node.textContent || '';
        node.textContent = '';

        for (const char of text) {
            const span = document.createElement('span');
            span.style.display = 'inline-block';
            span.textContent = char;
            node.appendChild(span);

            if (char === ' ') continue;

            const originalPath = getPathForLetter(char);
            const targetPath = getRandomTargetPath();

            let svg: SVGSVGElement | null = null;
            let frame: number | null = null;

            const animateMorph = (
                from: string,
                to: string,
                fromTransform: string,
                toTransform: string,
                onDone?: () => void
            ) => {
                if (!svg) return;
                const path = svg.querySelector('path');
                if (!path) return;

                const interpolator = flubber.interpolate(from, to);
                const transformInterpolator = interpolateTransform(fromTransform, toTransform);

                let progress = 0;
                function step() {
                    progress += 0.03;
                    const eased = easeInOutCubic(Math.min(progress, 1));

                    path?.setAttribute('d', interpolator(eased));
                    path?.setAttribute('transform', transformInterpolator(eased));

                    if (progress < 1) {
                        frame = requestAnimationFrame(step);
                    } else {
                        onDone?.();
                    }
                }
                step();
            };

            span.addEventListener('mouseenter', () => {
                const rect = span.getBoundingClientRect();
                const centerX = rect.left + rect.width / 2;
                const centerY = rect.top + rect.height / 2;

                const scale = Math.random() * 2 + 1;
                const finalX = Math.random() * window.innerWidth;
                const finalY = Math.random() * window.innerHeight;

                const fromTransform = `translate(${centerX} ${centerY}) scale(1) translate(-50 -50)`;
                const toTransform = `translate(${finalX} ${finalY}) scale(${scale}) translate(-50 -50)`;

                svg = createSvg(originalPath);
                document.body.appendChild(svg);
                span.style.color = 'white';

                animateMorph(originalPath, targetPath, fromTransform, toTransform);
            });

            span.addEventListener('mouseleave', () => {
                if (!svg) return;
                if (frame) cancelAnimationFrame(frame);

                const rect = span.getBoundingClientRect();
                const centerX = rect.left + rect.width / 2;
                const centerY = rect.top + rect.height / 2;

                const fromTransform = svg.querySelector('path')?.getAttribute('transform') || '';
                const toTransform = `translate(${centerX} ${centerY}) scale(1) translate(-50 -50)`;

                animateMorph(targetPath, originalPath, fromTransform, toTransform, () => {
                    svg?.remove();
                    span.style.color = '';
                    svg = null;
                });
            });
        }
    })();

    return {
        destroy() {
            // cleanup if needed
        }
    };
}