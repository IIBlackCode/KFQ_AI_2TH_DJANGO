## WEAREHERE
주관: 한국품질재단  
소속: 인공지능  
조원: 김민서, 김영주, 유수진, 한정탁  
진행기간: 2021-06-15 ~ 2021-07-07  

[최초 1회]  
1. Email 인증  
2. git remote add origin https://github.com/IIBlackCode/KFQ  

[업데이트 시]  
3. git pull url or origin master  
4. git add 폴더경로or파일경로  
5. git commit -m "업데이트 내용"  
6. git push  

[commit 규칙(안)]  
1. 제목과 본문을 빈 행으로 구분한다  
2. 제목을 50글자 내로 제한  
3. 제목 첫글자는 대문자로 작성  
4. 제목 끝에 마침표 넣지 않기  
5. 제목은 명령문으로 사용하며 과거형을 사용하지 않는다 
6. 본문의 각 행은 72글자 내로 제한  
7. 어떻게 보다는 무엇과 왜를 설명한다!  

-깃 업로드 순서 참고용  
1. git pull origin master  
2. git add .  
3. git commit -m "커밋내용"  
4. git checkout master  
5. git merge MS-K 		- 내가 만   
6. git push origin master 	- 최종적으로 깃허브에 업로드  

> 출처  
> [git commit 영어사전](https://blog.ull.im/engineering/2019/03/10/logs-on-git.html)  
> [Commit message 작성 규칙](https://velog.io/@djh20/Git-제대로-사용해보자)  



1. git init : 현재 파일을 깃허브와 연동
2. git remote add origin https://github.com/IIBlackCode/test.git : 깃허브 오리진에 추가
3. git remote -v : 연결확인
1. git pull origin master - 깃허브 소스 내려받기
2. git add . - 로컬소스 스테이징
3. git commit -m "커밋내용" - 커밋
4. git checkout master - master로 ?
5. git merge MS-K - MS-K 브릿지와 master 브릿지 merge
6. git push origin master - 최종적으로 깃허브에 업로드
