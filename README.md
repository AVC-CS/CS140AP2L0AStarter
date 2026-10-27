# AP2L0A — Examples 1 to 3 (IF statements)

Three separate programs, each with its own C++ program in its header: `ex1.asm` (if `i == j`), `ex2.asm` (if `i < j`), `ex3.asm` (if `i < 10`).
Write each one in its own file. Keep every `.data` block as it is, and do not use the
pseudo-instructions `blt`, `bgt`, `ble`, `bge` (use `slt` / `slti` with `beq` / `bne`).
Full instructions are on Canvas.

## Trace it step by step (SPIM)
Open a program (for example `ex1.asm`) in JsSpim (https://shawnzhong.com/JsSpim/) or run `spim` — see the SPIM guide on Canvas.

## Assemble (read any errors it prints)
```
java -jar Mars4_5.jar nc a ex1.asm
```

## Run (type the input, or feed a data file)
```
java -jar Mars4_5.jar nc sm ex1.asm < data/ex1_data1.txt
```

## Check memory after the run
```
java -jar Mars4_5.jar nc sm 0x10010000-0x1001003c ex1.asm < data/ex1_data1.txt
```

## Test (the same checks the autograder runs)
```
data/run.sh
pytest -rP -m T1
pytest -rP -m T2
pytest -rP -m T3
```
`data/run.sh` runs every program on its own data sets (`data/<program>_dataN.txt`) and writes
`result_<program>_N.txt`; T1, T2 and T3 test the three programs in order.

Submit by committing and pushing; the green check on GitHub means the autograder passed.
