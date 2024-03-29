-- 코드를 입력하세요
SELECT a.APNT_NO, p.PT_NAME, p.PT_NO, a.MCDP_CD, d.DR_NAME, a.APNT_YMD FROM APPOINTMENT AS a 
INNER JOIN PATIENT AS p ON a.PT_NO = p.PT_NO
INNER JOIN DOCTOR AS d ON a.MDDR_ID = d.DR_ID
WHERE LEFT(a.APNT_YMD,10) = '2022-04-13' AND a.APNT_CNCL_YN = 'N'
ORDER BY a.APNT_YMD