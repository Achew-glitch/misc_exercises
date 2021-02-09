# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    h_len_t_n = int(len(ticket_number) / 2)
    first_half = int(ticket_number[:h_len_t_n])
    first_sum = 0
    last_half = int(ticket_number[-h_len_t_n:])
    last_sum = 0
    while first_half:
        first_sum += first_half % 10
        first_half //= 10
    while last_half:
        last_sum += last_half % 10
        last_half //= 10
    if last_sum == first_sum:
        return f'Ticket {ticket_number} is lucky'
    else:
        return f'Ticket {ticket_number} is unlucky'

def lucky_ticket_2(ticket_number):
    dig_sum = 0
    while ticket_number:
        dig_sum += ticket_number % 10
        ticket_number //= 10
    if dig_sum % 2:
        return f'Ticket is unlucky'
    else:
        return f'Ticket is lucky'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

print(lucky_ticket_2(123006))
print(lucky_ticket_2(12321))
print(lucky_ticket_2(436751))