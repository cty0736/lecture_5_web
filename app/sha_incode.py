from passlib.hash import pbkdf2_sha256

password ='1234'

hash_pw = pbkdf2_sha256.hash(password)

print(hash_pw)

print(hash_pw =='$pbkdf2-sha256$29000$w3hvrTWGkFLqfe89JwQAgA$Cub8UFK9wWT5kSAavCPp7HzaOum4BC.hNG4vGutwaos')

#같은 지 확인은 verify이용
print(pbkdf2_sha256.verify(password, hash_pw))