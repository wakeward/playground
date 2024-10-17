# Code Playground

General repository for experimenting with different coding languages

## Assembly

`ww.asm` - "Hello World" example which prints "wakeward"
`rs.asm` - reverse shell in assembly [Thx Xre0uS](https://github.com/Xre0uS/linux-reverse-shell-in-assembly/blob/main/reverse.asm)


### Build and Execution

#### ww.asm

```bash
nasm -f elf32 ww.asm -o ww.o
ld -m elf_i386 ww.o -o ww

./ww
```

#### rs.asm

Setup `nc` listener

```bash
nc -nlvp 4444
```

Build and Execute

```bash
nasm -f elf64 rs.asm -o rs.o
ld rs.o -o rs

./rs
```

### Notes from code reviewing

From `rs.asm`

- `CDQ` - Covert Doubleword to Quadword is an instruction that extends the sign bit of `EAX` into the `EDX` register.
- `syscall` - is default way of entering kernel mode on x86-64. This instruction is not available in 32 bit modes of operation on Intel processors.
- `XCHG` - Exchanges (swaps) the value of 2 registers
- `JNS` - Jump if not sign
- `SIL` - General purpose register (64-bit, the least significant bit 8 bits is assessible)

[Ref](https://www.aldeid.com/wiki/Main_Page)

## Go

Testing

```go
go run main.go
```

Build for Linux (current environment)

```go
go build -o rs main.go
```

## C

Build

```bash
gcc rs.c -o rs
```