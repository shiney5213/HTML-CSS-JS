# 
# Basic Codes for Operators

a <- 4
b <- 3

print(a + b)


if (a > b) {
    print('a is larger than b')
}

if (a > b) {
    print('a is larger than b')
} else {
    print('b is equal or larger than a')
}

if (a > b) {
    print('a is larger than b')
} else if (a == b) {
    print('b is equal to a')
} else {
    print('b is larger than a')
}


gender <- 'woman'
age <- 21

if (gender == 'man'){
    if (age >= 20){
        print('성인 남성')
    }
    else{
        print('미성년자 남성')
    }
}else{
    if (age >= 20) {
        print('성인 여성')
    }
    else{
        print('미성년자 여성')
    }
}


a = 3
ifelse(a %/% 2 == 1, '홀수', '짝수')


# Print Even numbers under 20
for (i in 1:10){
    print(i*2)
}


start <- 1
while (start <= 10) {
    print(start)
    start <- start + 1
}


is_even <- function(n){
    if (n %% 2 == 0) {
        TRUE
    } else if (n %% 2 == 1) {
        FALSE
    }
}

is_even(2) # True

dinner <- 3
choice <- 2

if(dinner == 1){ 
  cat("한식", "\n")
  if( choice == 1) {
    cat("차돌박이 된장찌개") 
    } else cat("삼겹살") 
} else if(dinner == 2){ 
  cat("일식", "\n") 
  if( choice == 1) {
    cat("초밥") 
    } else cat("우동")
} else if(dinner == 3){
  cat("중식", "\n") 
  if( choice == 1) {
    cat("짜장면") 
    } else cat("짬뽕") } 

func17 <- function(x, y) {
  if ( x %% y == 0 ) {
    print("The remainder is 0")
  } else {
    cat(x %% y, "is remainder")
  }
}

menu <- function(choice) { 
  option <- sample(3, size = 1, replace = TRUE)
  if(choice == 1) { cat("한식", "\n") 
    if(option == 1) { 
      cat("차돌박이 된장찌개")
      } else if(option == 2) {
        cat("삼겹살")
      } else cat("제육볶음")
    } else if(choice == 2) { cat("일식", "\n") 
      if(option == 1) {
        cat("초밥")
        } else if(option == 2) {
          cat("우동")
          } else cat("카레")
      } else if(choice == 3) { cat("중식", "\n") 
        if(option == 1) {
          cat("짜장면")
          } else if(option == 2) {
            cat("짬뽕")
          } else cat("볶음밥")
      }
}





menu <- function(x) {
  if(x == 1) {
    "짜장면"
  } else {
    "짬뽕"
  }
}


yoon <- function(year){
    if (year%%4 == 0){
        if (year%%400 == 0){
            print('y')#print('윤년입니다.')
        } else if (year%%100 == 0){
            print('n')#print('윤년이 아닙니다.')
        } else{
            print('y')#print('윤년입니다.')
        }
    } else{
        print('n')#print('윤년이 아닙니다.')
    }
} 
yoon(398)
yoon(400)
yoon(396)
yoon(300)

def yoon(year):
    if year%4 == 0:
        if year%400 == 0:
            print('윤년입니다.')
        elif year%100 == 0:
            print('윤년이 아닙니다.')
        else:
            print('윤년입니다.')

yoon(400)
yoon(396)
yoon(300)

