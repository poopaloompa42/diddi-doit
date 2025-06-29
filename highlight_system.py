from ursina import *

last_highlighted = None

def highlight_logic(targets):
    global last_highlighted

    hovered = mouse.hovered_entity

    if hovered and hovered in targets:
        if hovered != last_highlighted:
            # Unhighlight previous
            if last_highlighted and hasattr(last_highlighted, 'set_highlighted'):
                last_highlighted.set_highlighted(False)
            # Highlight new one
            if hasattr(hovered, 'set_highlighted'):
                hovered.set_highlighted(True)
            last_highlighted = hovered
    else:
        # Unhighlight if no valid hover
        if last_highlighted and hasattr(last_highlighted, 'set_highlighted'):
            last_highlighted.set_highlighted(False)
        last_highlighted = None
