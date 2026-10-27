#!/usr/bin/env python3
"""Añade tarjetas Anki Bridge a notas existentes de Electromagnetismo II,
sin reemplazar las notas ni tocar el registro de Anki. Solo biblioteca estándar.
Uso: python aplicar_tarjetas_anki_bridge.py [RUTA_DE_LA_BOVEDA]
"""
from pathlib import Path
from datetime import datetime
import shutil
import sys

START = '<!-- INICIO TARJETAS ANKI BRIDGE C2 (agregadas sin modificar teoría) -->'
END = '<!-- FIN TARJETAS ANKI BRIDGE C2 -->'

CARDS = {
    'Autoinducción e inductancia.md': r'''### Tarjetas para Anki Bridge — Autoinducción

¿Por qué duplicar el número de espiras de un solenoide largo cuadruplica su inductancia (geometría fija)? ⇢%%oab:basic:v1%%El campo por unidad de corriente se duplica y también el número de espiras que enlazan el flujo: $L=N\Phi_B/i\propto N^2$.

¿Cómo se obtiene la fem autoinducida desde Faraday-Lenz cuando $L$ es constante? ⇢%%oab:basic:v1%%Con $\lambda=N\Phi_B=Li$, Faraday-Lenz da $\mathcal E_{\mathrm{ind}}=-d\lambda/dt=-L\,di/dt$.
''',
    'Energía magnética.md': r'''### Tarjetas para Anki Bridge — Energía magnética

¿Qué representa $u_B$ y cuánto vale para un campo magnético en el vacío? ⇢%%oab:basic:v1%%Es la energía magnética por unidad de volumen: $u_B=B^2/(2\mu_0)$. Puede deducirse para un solenoide ideal usando $U_B=Li^2/2$.

Si $i<0$ pero $di/dt>0$ en un inductor ideal, ¿aumenta o disminuye su energía magnética? ⇢%%oab:basic:v1%%Disminuye: $dU_B/dt=Li\,di/dt<0$. La corriente negativa se aproxima a cero, por lo que disminuye $|i|$.
''',
    'Oscilaciones LC.md': r'''### Tarjetas para Anki Bridge — Oscilaciones LC

¿Cómo compruebas las unidades de la frecuencia angular natural $\omega_0=1/\sqrt{LC}$? ⇢%%oab:basic:v1%%$[L]=\mathrm{V\,s/A}$ y $[C]=\mathrm{A\,s/V}$; por tanto $[LC]=\mathrm{s^2}$ y $[\omega_0]=\mathrm{s^{-1}}$ (rad/s).

Si en un LC ideal $U_E=U_B$, ¿por qué eso no significa que la oscilación se detenga? ⇢%%oab:basic:v1%%Igualdad de energías no implica equilibrio: la corriente sigue siendo no nula, de modo que el capacitor continúa transfiriendo carga.

Con $i=dq/dt$, ¿qué signos tienen $q$, $i$ y $di/dt$ en $t=T/2$ si $q(0)=Q>0$ e $i(0)=0$? ⇢%%oab:basic:v1%%$q=-Q$, $i=0$ y $di/dt=+Q/(LC)>0$. La corriente pasa de negativa a positiva después de ese instante.
'''
}

IGNORE_BLOCK = '''\n# Estado local de Anki Bridge: IDs de Anki y posibles credenciales\n# IMPORTANTE: conservar respaldo privado de este archivo para no perder asociaciones.\n.obsidian-anki-bridge/data.json\n'''

def main() -> None:
    vault = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
    if not (vault / '.gitignore').exists() or not (vault / 'Conceptos').is_dir():
        raise SystemExit(f'No parece la bóveda esperada: {vault}\nSe necesitan .gitignore y la carpeta Conceptos.')
    targets = [(name, vault / 'Conceptos' / name) for name in CARDS]
    missing = [str(p) for _, p in targets if not p.is_file()]
    if missing:
        raise SystemExit('Faltan las notas siguientes; no se modificó nada:\n' + '\n'.join(missing))
    stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup = Path.home() / 'AnkiBridge-Respaldos' / stamp
    backup.mkdir(parents=True, exist_ok=True)
    for _, path in targets:
        shutil.copy2(path, backup / path.name)
    shutil.copy2(vault / '.gitignore', backup / 'gitignore_original.txt')
    registry = vault / '.obsidian-anki-bridge' / 'data.json'
    if registry.exists():
        shutil.copy2(registry, backup / 'anki_bridge_data_backup.json')
    count = 0
    for name, path in targets:
        original = path.read_text(encoding='utf-8-sig')
        if START in original or END in original:
            print(f'YA TIENE TARJETAS: {name} (sin cambios)')
            continue
        block = f'\n\n{START}\n\n{CARDS[name].strip()}\n\n{END}\n'
        # Añadimos antes del cierre, si existe, para preservar los metadatos y la teoría.
        path.write_text(original.rstrip() + block + '\n', encoding='utf-8')
        count += 1
        print(f'ACTUALIZADA: {name}')
    ignore = vault / '.gitignore'
    text = ignore.read_text(encoding='utf-8-sig')
    if '.obsidian-anki-bridge/data.json' not in text:
        ignore.write_text(text.rstrip('\r\n') + '\n' + IGNORE_BLOCK, encoding='utf-8')
        print('ACTUALIZADO: .gitignore')
    else:
        print('YA IGNORADO: .obsidian-anki-bridge/data.json')
    print(f'\nRespaldo privado: {backup}')
    print(f'Se modificaron {count} notas; hay 7 tarjetas nuevas en total.')
    print('No se borraron ni modificaron tarjetas anteriores en Anki ni archivos del registro.')
    print('IMPORTANTE: .gitignore no desindexa archivos ya versionados.')
    print('Si Obsidian Git sincroniza automáticamente, ejecuta lo siguiente ANTES de reabrir Obsidian.')
    print('Si deseas dejar de publicar el registro, ejecuta en la raíz del repositorio:')
    print('  git rm --cached -- .obsidian-anki-bridge/data.json')
    print('  git add .gitignore Conceptos')
    print('  git commit -m "Integrar tarjetas Obsidian-Anki y proteger registro"')
    print('  git push')
    print('Conserva el respaldo del registro FUERA del repositorio.')
    print('Tras crear las nuevas tarjetas, RESPALDA OTRA VEZ data.json, porque ahora tiene sus nuevos ID.')

if __name__ == '__main__':
    main()
