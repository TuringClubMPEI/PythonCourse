from bank import Bank
from account import Account


def main():
    bank = Bank()
    accounts = bank.accounts

    misha = Account(1, 'Misha', 10000)
    pasha = Account(2, 'Pasha', 10000)

    accounts.append(misha)
    accounts.append(pasha)

    try:
        print('Перевели 1000 от Миши к Паше')
        bank.transfer(misha, pasha, 1000)
        print(misha.balance)
        print(pasha.balance)
        print()
    except Exception:
        print('Упс! Перевод не удался')

    try:
        print('Положили на счет Мише кес')
        misha.deposit(1000)
        print(misha.balance)
        print()
    except Exception:
        print('Упс! Депозит не удался')

    try:
        print('Сняли кес с Пашиного счета')
        pasha.withdraw(1000)
        print(pasha.balance)
        print()
    except Exception:
        print('Упс! Снятие денег не удалось')


if __name__ == "__main__":
    main()
