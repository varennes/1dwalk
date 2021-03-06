program random1dWalk

! allocate variables
implicit none

integer :: i, iTemp, iterN, j, k, N, t
integer :: nRun, runTotal

integer, dimension(2) :: r0, rCell, rSim
integer, allocatable :: iterateOrder(:), tRun(:)

real(8) :: L, v, xCOM, xCOMi
real(8) :: pLeft, pRight, r
real(8), allocatable :: x(:)

real(8) :: t0, tf

character(len=1024) :: filename
character(len=1024) :: format_string

call cpu_time(t0)

! initialize parameters, variables
open(unit=11,file='input.txt',status='old',action='read')
read(11,*)
read(11,*) runTotal
read(11,*) N
read(11,*) L
read(11,*) v

pLeft  = 0.5_8 - v
pRight = 0.5_8 + v

write(*,*) 'parameters:'
write(*,*) '      N =',N
write(*,*) '      L =',L
write(*,*) '      v =',v
write(*,*) '  pLeft =',pLeft
write(*,*) ' pRight =',pRight
write(*,*)

call init_random_seed()

do iterN = 10, N, 10

    allocate( x(iterN) )
    allocate( iterateOrder(iterN) )
    allocate( tRun(runTotal) )

    ! initialize arrays
    x(:) = 0.0_8
    tRun(:) = 0

    do i = 1, iterN
        iterateOrder(i) = i
    enddo

do nRun = 1, runTotal

    t = 0

    ! initial walker position
    do i = 1, iterN
        x(i) = real(i-1)
    enddo
    ! inital center of mass (COM) position
    xCOMi = 0.0_8
    xCOMi = sum(x) / real(iterN)
    xCOM  = xCOMi

    do while( (xCOM - xCOMi) < L )

        ! shuffle the order walker moves
        do i = iterN, 2, -1
            call random_number(r)
            k = 1 + floor( real(i) * r )
            iTemp = iterateOrder(i)
            iterateOrder(i) = iterateOrder(k)
            iterateOrder(k) = iTemp
        enddo

        do i = 1, iterN
            iTemp = iterateOrder(i)
            call random_number(r)
            if( r < pRight )then
                if( iTemp /= iterN .AND. iterN /= 1 )then
                    if( x(iTemp+1) /= (x(iTemp)+1.0_8) )then
                        x(iTemp) = x(iTemp) + 1.0_8
                    endif
                else
                    x(iTemp) = x(iTemp) + 1.0_8
                endif
            else
                if( iTemp /= 1 .AND. iterN /= 1 )then
                    if( x(iTemp-1) /= (x(iTemp)-1.0_8) )then
                        x(iTemp) = x(iTemp) - 1.0_8
                    endif
                else
                    x(iTemp) = x(iTemp) - 1.0_8
                endif
            endif
        enddo
        xCOM = sum(x) / real(iterN)

        t = t + 1
    enddo

    tRun(nRun) = t
enddo

! output data
! make filenames for output data
format_string = "(A6,I1,A4)"
write(filename,format_string) "tRun00", iterN, '.dat'
if( iterN >= 10 )then
    format_string = "(A5,I2,A4)"
    write(filename,format_string) "tRun0", iterN, '.dat'
endif
if( iterN >= 100)then
    format_string = "(A4,I3,A4)"
    write(filename,format_string) "tRun", iterN, '.dat'
endif

open(unit=21,file=filename,status='replace',action='write')

do i = 1, runTotal
    write(21,*) tRun(i)
enddo

deallocate( x )
deallocate( iterateOrder )
deallocate( tRun )

close(21)

enddo

call cpu_time(tf)

write(*,*) ' run time =',tf-t0
end program

! initialize RANDOM_SEED
subroutine init_random_seed()
    integer :: values(1:8), k
    integer, dimension(:), allocatable :: seed
    real(8) :: r

    call date_and_time(values=values)

    call random_seed(size=k)
    allocate(seed(1:k))
    seed(:) = values(8)
    call random_seed(put=seed)
end subroutine init_random_seed
