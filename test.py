; ModuleID = 'arithmetic'
target triple = "unknown-unknown-unknown"
target datalayout = ""

define double @main() {
entry:
  %addtmp = fadd double 8.000000e+00, 2.000000e+00
  %multmp = fmul double %addtmp, 1.000000e+01
  ret double %multmp
}
