package user.userManagement.aop;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect // 이 클래스가 AOP(Aspect-Oriented Programming) Aspect임을 나타냄
@Component // 이 클래스가 Spring의 컴포넌트 스캔에 의해 빈으로 등록됨
public class TimeTraceAop {

    // user.userManagement 패키지와 그 하위 패키지에 속한 모든 메서드에 대해 AOP 적용
    @Around("execution(* user.userManagement..*(..))")
    public Object execute(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis(); // 메서드 실행 시작 시간 기록

        System.out.println("START: " + joinPoint.toString());

        try {
            return joinPoint.proceed(); // 대상 메서드 실행
        } finally {
            long finish = System.currentTimeMillis(); // 메서드 실행 종료 시간 기록
            long timeMs = finish - start; // 메서드 실행 시간 계산

            System.out.println("END: " + joinPoint.toString() + " " + timeMs + "ms");
        }
    }
}
