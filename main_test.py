# AP2L0A tests (git-asmt-repo L2 mips-mars). data/run.sh runs each example program in MARS on
# its own data sets: data/<prog>_dataN.txt -> result_<prog>_N.txt (the program's output, then the
# Mem[...] lines).
#   T1 — ex1.asm (i == j)   T2 — ex2.asm (i < j)   T3 — ex3.asm (i < 10)
#   On every data set of that program: it PRINTS f, and f holds it in memory after the run.
#   Each group also checks that its program uses no blt / bgt / ble / bge pseudo-instruction.
import pytest
import re

DATA = 0x10010000

# program -> (address of f, {data set: (input, expected f)})
PROGS = {
    'ex1': (DATA + 16, {1: ('5 5', 42), 2: ('5 7', 18), 3: ('-3 -3', 42)}),
    'ex2': (DATA + 16, {1: ('3 5', 42), 2: ('5 5', 18), 3: ('-2 1', 42), 4: ('7 -1', 18)}),
    'ex3': (DATA + 12, {1: ('9', 42), 2: ('10', 18), 3: ('-5', 42), 4: ('15', 18)}),
}


def num_re(v):
    """The integer v as a whole number: 42 does not match inside -42 or 420."""
    return r'(?<![\d-])%s(?!\d)' % re.escape(str(v))


def values_in_order(expected, out):
    """Each value appears in the output, in this order (labels and newlines around it are fine)."""
    text = '\n'.join(out)
    pos = 0
    for v in expected:
        m = re.compile(num_re(v)).search(text, pos)
        assert m, f'Expected to see {v} in the output (in this order: {expected}); got {out}'
        pos = m.end()


def result(prog, n):
    """(output_lines, memory) of result_<prog>_N.txt; `memory` maps a word address to its value."""
    out, mem = [], {}
    with open(f'result_{prog}_{n}.txt', 'r') as f:
        for line in f:
            m = re.search(r'Mem\[(0x[0-9a-fA-F]+)\]((?:\s+0x[0-9a-fA-F]{8})+)', line)
            if m:
                addr = int(m.group(1), 16)
                for k, w in enumerate(m.group(2).split()):
                    mem[addr + 4 * k] = int(w, 16)
            else:
                out.append(line.strip())
    return out, mem


def word(mem, addr, signed=True):
    """The word at `addr`, as a signed int."""
    assert addr in mem, f'{addr:#010x} is not in the memory lines - did the program run?'
    w = mem[addr]
    return w - (1 << 32) if signed and w & 0x80000000 else w


def no_pseudo_branch(path):
    """No blt / bgt / ble / bge (or their u forms) outside comments. bltz, blez, bgez, bgtz are
    real instructions and are allowed."""
    bad = []
    for k, line in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
        code = line.split('#', 1)[0]
        if re.search(r'\b(blt|bgt|ble|bge)u?\b', code):
            bad.append(f'line {k}: {line.strip()}')
    assert not bad, (f'{path}: blt / bgt / ble / bge are pseudo-instructions, not allowed here - '
                     'use slt / slti with beq / bne:\n  ' + '\n  '.join(bad))


def check_prog(prog):
    addr, cases = PROGS[prog]
    for n, (inp, f_val) in cases.items():
        out, mem = result(prog, n)
        print(f'{prog}.asm, data/{prog}_data{n}.txt: input {inp} -> expected f = {f_val}')
        values_in_order([f_val], out)
        got = word(mem, addr)
        assert got == f_val, f'{prog}: f ({addr:#010x}) should be {f_val} after the run, but holds {got}'
    no_pseudo_branch(f'{prog}.asm')


@pytest.mark.T1
def test_t1():
    check_prog('ex1')


@pytest.mark.T2
def test_t2():
    check_prog('ex2')


@pytest.mark.T3
def test_t3():
    check_prog('ex3')
