import pygame

bindings = {
    pygame.K_0: "0",
    pygame.K_GREATER: "greater",
    pygame.K_RALT: "ralt",
    pygame.K_1: "1",
    pygame.K_HASH: "hash",
    pygame.K_RCTRL: "rctrl",
    pygame.K_2: "2",
    pygame.K_HELP: "help",
    pygame.K_RETURN: "return",
    pygame.K_3: "3",
    pygame.K_HOME: "home",
    pygame.K_RIGHT: "right",
    pygame.K_4: "4",
    pygame.K_INSERT: "insert",
    pygame.K_RIGHTBRACKET: "rightbracket",
    pygame.K_5: "5",
    pygame.K_KP0: "kp0",
    pygame.K_RIGHTPAREN: "rightparen",
    pygame.K_6: "6",
    pygame.K_KP1: "kp1",
    pygame.K_RMETA: "rmeta",
    pygame.K_7: "7",
    pygame.K_KP2: "kp2",
    pygame.K_RSHIFT: "rshift",
    pygame.K_8: "8",
    pygame.K_KP3: "kp3",
    pygame.K_RSUPER: "rsuper",
    pygame.K_9: "9",
    pygame.K_KP4: "kp4",
    pygame.K_SCROLLOCK: "scrollock",
    pygame.K_AMPERSAND: "ampersand",
    pygame.K_KP5: "kp5",
    pygame.K_SEMICOLON: "semicolon",
    pygame.K_ASTERISK: "asterisk",
    pygame.K_KP6: "kp6",
    pygame.K_SLASH: "slash",
    pygame.K_AT: "at",
    pygame.K_KP7: "kp7",
    pygame.K_SPACE: "space",
    pygame.K_BACKQUOTE: "backquote",
    pygame.K_KP8: "kp8",
    pygame.K_SYSREQ: "sysreq",
    pygame.K_BACKSLASH: "backslash",
    pygame.K_KP9: "kp9",
    pygame.K_TAB: "tab",
    pygame.K_BACKSPACE: "backspace",
    pygame.K_KP_DIVIDE: "kp_divide",
    pygame.K_UNDERSCORE: "underscore",
    pygame.K_BREAK: "break",
    pygame.K_KP_ENTER: "kp_enter",
    pygame.K_UNKNOWN: "unknown",
    pygame.K_CAPSLOCK: "capslock",
    pygame.K_KP_EQUALS: "kp_equals",
    pygame.K_UP: "up",
    pygame.K_CARET: "caret",
    pygame.K_KP_MINUS: "kp_minus",
    pygame.K_a: "a",
    pygame.K_CLEAR: "clear",
    pygame.K_KP_MULTIPLY: "kp_multiply",
    pygame.K_b: "b",
    pygame.K_COLON: "colon",
    pygame.K_KP_PERIOD: "kp_period",
    pygame.K_c: "c",
    pygame.K_COMMA: "comma",
    pygame.K_KP_PLUS: "kp_plus",
    pygame.K_d: "d",
    pygame.K_DELETE: "delete",
    pygame.K_LALT: "lalt",
    pygame.K_e: "e",
    pygame.K_DOLLAR: "dollar",
    pygame.K_LAST: "last",
    pygame.K_f: "f",
    pygame.K_DOWN: "down",
    pygame.K_LCTRL: "lctrl",
    pygame.K_g: "g",
    pygame.K_END: "end",
    pygame.K_LEFT: "left",
    pygame.K_h: "h",
    pygame.K_EQUALS: "equals",
    pygame.K_LEFTBRACKET: "leftbracket",
    pygame.K_i: "i",
    pygame.K_ESCAPE: "escape",
    pygame.K_LEFTPAREN: "leftparen",
    pygame.K_j: "j",
    pygame.K_EURO: "euro",
    pygame.K_LESS: "less",
    pygame.K_k: "k",
    pygame.K_EXCLAIM: "exclaim",
    pygame.K_LMETA: "lmeta",
    pygame.K_l: "l",
    pygame.K_F1: "f1",
    pygame.K_LSHIFT: "lshift",
    pygame.K_m: "m",
    pygame.K_F10: "f10",
    pygame.K_LSUPER: "lsuper",
    pygame.K_n: "n",
    pygame.K_F11: "f11",
    pygame.K_MENU: "menu",
    pygame.K_o: "o",
    pygame.K_F12: "f12",
    pygame.K_MINUS: "minus",
    pygame.K_p: "p",
    pygame.K_F13: "f13",
    pygame.K_MODE: "mode",
    pygame.K_q: "q",
    pygame.K_F14: "f14",
    pygame.K_NUMLOCK: "numlock",
    pygame.K_r: "r",
    pygame.K_F15: "f15",
    pygame.K_PAGEDOWN: "pagedown",
    pygame.K_s: "s",
    pygame.K_F2: "f2",
    pygame.K_PAGEUP: "pageup",
    pygame.K_t: "t",
    pygame.K_F3: "f3",
    pygame.K_PAUSE: "pause",
    pygame.K_u: "u",
    pygame.K_F4: "f4",
    pygame.K_PERIOD: "period",
    pygame.K_v: "v",
    pygame.K_F5: "f5",
    pygame.K_PLUS: "plus",
    pygame.K_w: "w",
    pygame.K_F6: "f6",
    pygame.K_POWER: "power",
    pygame.K_x: "x",
    pygame.K_F7: "f7",
    pygame.K_PRINT: "print",
    pygame.K_y: "y",
    pygame.K_F8: "f8",
    pygame.K_QUESTION: "question",
    pygame.K_z: "z",
    pygame.K_F9: "f9",
    pygame.K_QUOTE: "quote",
    pygame.K_FIRST: "first",
    pygame.K_QUOTEDBL: "quotedbl",
}

modifier_bindings = [
    (pygame.KMOD_ALT, "alt"),
    (pygame.KMOD_LSHIFT, "lshift"),
    (pygame.KMOD_RCTRL, "rctrl"),
    (pygame.KMOD_CAPS, "caps"),
    (pygame.KMOD_META, "meta"),
    (pygame.KMOD_RMETA, "rmeta"),
    (pygame.KMOD_CTRL, "ctrl"),
    (pygame.KMOD_MODE, "mode"),
    (pygame.KMOD_RSHIFT, "rshift"),
    (pygame.KMOD_LALT, "lalt"),
    (pygame.KMOD_NONE, "none"),
    (pygame.KMOD_SHIFT, "shift"),
    (pygame.KMOD_LCTRL, "lctrl"),
    (pygame.KMOD_NUM, "num"),
    (pygame.KMOD_LMETA, "lmeta"),
    (pygame.KMOD_RALT, "ralt"),
]
