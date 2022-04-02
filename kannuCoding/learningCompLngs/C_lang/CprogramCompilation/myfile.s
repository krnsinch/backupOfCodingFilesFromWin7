	.file	"myfile.c"
	.text
	.globl	_a
	.data
	.align 4
_a:
	.long	23
	.globl	_earth_gravity
	.align 4
_earth_gravity:
	.long	1092413817
	.globl	_mars_gravity
	.align 4
_mars_gravity:
	.long	1080960221
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
	.align 4
LC0:
	.ascii "value of a by including b.c file is %d\12\0"
LC1:
	.ascii "acceleration on earth is %f\12\0"
LC2:
	.ascii "acceleration on mars is %f\12\0"
LC4:
	.ascii "value of pi is %f\12\0"
LC5:
	.ascii "square of 4 is %d\12\0"
LC6:
	.ascii "17:28:10\0"
LC7:
	.ascii "\12Time is %s\12\0"
LC8:
	.ascii "Feb 17 2022\0"
LC9:
	.ascii "Date is %s\12\0"
LC10:
	.ascii ".\\myfile.c\0"
LC11:
	.ascii "Name of this file is %s\12\0"
LC12:
	.ascii "Line is %d\12\0"
LC13:
	.ascii "ANSI: %d\12\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB13:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	_a, %eax
	movl	%eax, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	flds	_earth_gravity
	fstpl	4(%esp)
	movl	$LC1, (%esp)
	call	_printf
	flds	_mars_gravity
	fstpl	4(%esp)
	movl	$LC2, (%esp)
	call	_printf
	fldl	LC3
	fstpl	4(%esp)
	movl	$LC4, (%esp)
	call	_printf
	movl	$16, 4(%esp)
	movl	$LC5, (%esp)
	call	_printf
	movl	$LC6, 4(%esp)
	movl	$LC7, (%esp)
	call	_printf
	movl	$LC8, 4(%esp)
	movl	$LC9, (%esp)
	call	_printf
	movl	$LC10, 4(%esp)
	movl	$LC11, (%esp)
	call	_printf
	movl	$35, 4(%esp)
	movl	$LC12, (%esp)
	call	_printf
	movl	$1, 4(%esp)
	movl	$LC13, (%esp)
	call	_printf
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE13:
	.section .rdata,"dr"
	.align 8
LC3:
	.long	1374389535
	.long	1074339512
	.ident	"GCC: (MinGW.org GCC Build-2) 9.2.0"
	.def	_printf;	.scl	2;	.type	32;	.endef
