program random1dWalk

! allocate variables
implicit none

integer :: i, iTemp, j, k, N, t
integer :: nRun, runTotal

integer, dimension(2) :: r0, rCell, rSim
integer, allocatable :: iterateOrder(:), tRun(:)

real(8) :: L, v, xCOM, xCOMi
real(8) :: pLeft, pRight, r
real(8), allocatable :: x(:)

real(8) :: t0, tf

real(8), dimension(2) :: qtmp

call cpu_time(t0)

! initialize parameters, variables
open(unit=11,file='input.txt',status='old',action='read')
read(11,*)
read(11,*) runTotal
read(11,*) N
read(11,*) L
read(11,*) v

! N = 4
! L = 10_8
! v = 0.25_8

pLeft  = 0.5_8 - v
pRight = 0.5_8 + v

allocate( x(N) )
allocate( iterateOrder(N) )
allocate( tRun(runTotal) )

! initialize arrays
tRun(:) = 0

do i = 1, N
    iterateOrder(i) = i
enddo

write(*,*) 'parameters:'
write(*,*) '      N =',N
write(*,*) '      L =',L
write(*,*) '      v =',v
write(*,*) '  pLeft =',pLeft
write(*,*) ' pRight =',pRight
write(*,*)

call init_random_seed()



do nRun = 1, runTotal

    t = 0

    ! initial walker position
    do i = 1, N
        x(i) = real(i-1)
    enddo
    ! write(*,*) x(:)
    ! inital center of mass (COM) position
    xCOMi = 0.0_8
    xCOMi = sum(x) / real(N)
    xCOM  = xCOMi
    ! write(*,*) xCOMi

    ! do i = N, 2, -1
    !     call random_number(r)
    !     k = 1 + floor( real(i) * r )
    !     iTemp = iterateOrder(i)
    !     iterateOrder(i) = iterateOrder(k)
    !     iterateOrder(k) = iTemp
    ! enddo
    !
    ! do i = 1, N
    !     write(*,*) iterateOrder(i)
    ! enddo

    do while( (xCOM - xCOMi) < L )

        ! shuffle the order walker moves
        do i = N, 2, -1
            call random_number(r)
            k = 1 + floor( real(i) * r )
            iTemp = iterateOrder(i)
            iterateOrder(i) = iterateOrder(k)
            iterateOrder(k) = iTemp
        enddo

        do i = 1, N
            iTemp = iterateOrder(i)
            call random_number(r)
            if( r < pRight )then
                if( iTemp /= N .AND. N /= 1 )then
                    if( x(iTemp+1) /= (x(iTemp)+1.0_8) )then
                        x(iTemp) = x(iTemp) + 1.0_8
                    endif
                else
                    x(iTemp) = x(iTemp) + 1.0_8
                endif
            else
                if( iTemp /= 1 .AND. N /= 1 )then
                    if( x(iTemp-1) /= (x(iTemp)-1.0_8) )then
                        x(iTemp) = x(iTemp) - 1.0_8
                    endif
                else
                    x(iTemp) = x(iTemp) - 1.0_8
                endif
            endif
        enddo
        xCOM = sum(x) / real(N)
        ! write(*,*) x(:)
        t = t + 1
    enddo

    tRun(nRun) = t
enddo

call cpu_time(tf)

open(unit=21,file='tRun.dat',status='replace',action='write')

do i = 1, runTotal
    write(21,*) tRun(i)
enddo

! write(*,*) ' tRun =',tRun
write(*,*) ' FPT =', real(sum(tRun)) / real(runTotal)
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
