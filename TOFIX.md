# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `src/JEnable.java:997` - every error path in `main` (`:1047` bad token list, `:1058` missing token list, `:1084` unknown option, `:1101` token both enabled and disabled) just `return`s, so the JVM exits 0 and scripts cannot detect failure; `processFile` failures (`:714`) are likewise only printed. Exit with `System.exit(1)` on usage errors and return a non-zero status when any file failed.
- `src/JEnable.java:563` - the `BufferedReader` opened here is closed only on the success branches (`:601`, `:694`): a `.javx` file that stays disabled (`toext` and `ext` both `javx`) never closes it, and any exception skips `in.close()`/`out.close()` and the backup streams at `:628`. Use try-with-resources for `in`, `out`, `is` and `os`.
- `src/JEnable.java:1022` - `-b` with a path that is not a directory prints an error but keeps going with that path as the backup directory; abort instead.
- `README.md:14` - says `scripts/javac_build.py` "builds the classes and the jar", but `scripts/javac_build.py:21` only runs `javac` into `bin/`; nothing uses `manifest` to build a jar. Either add the `jar cfm` step (the `manifest` file is ready for it) or fix the README and delete `manifest`.
- `rsconstruct.toml:9` - ruff and mypy (`:13`) list `src`, which holds only Java; use `src_dirs = ["scripts"]`.

## Low

- `src/JEnable.java:1152` - the usage text says version 0.8 while the class javadoc (`:60`) and `doc/Changelog` say 0.9.
- `src/JEnable.java:572` - `Hashtable.contains()` tests values, not keys; it works only because each token is stored as its own value. Use `containsKey()` (or switch the token tables at `:157`/`:160` to `HashSet<String>`; `Vector` at `:951`/`:1008` to `ArrayList`).
- `src/JEnable.java:1011` - `argv[anum].charAt(0)` throws `StringIndexOutOfBoundsException` on an empty-string argument; check `isEmpty()` first.
- `doc/TODO.txt:3` - stale: LICENSE and README.md exist, "move build system to ant" and "upload to ibiblio" no longer apply (the build is rsconstruct). Prune it down to what is still open (tests).
