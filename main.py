import faker
import psycopg2
from datetime import datetime
import random


fake = faker.Faker()

def generate_transaction():
    user = fake.simple_profile()

    return {
        "transactionId": fake.uuid4(),
        "userId": user['username'],
        "timestamp": datetime.utcnow().timestamp(),
        "amount": round(random.uniform(10, 1000), 2),
        "currency": random.choice(['USD', 'GBP']),
        'city': fake.city(),
        "country": fake.country(),
        "merchantName": fake.company(),
        "paymentMethod": random.choice(['credit_card', 'debit_card', 'online_transfer']),
        "ipAddress": fake.ipv4(),
        "voucherCode": random.choice(['', 'DISCOUNT10', '']),
        'affiliateId': fake.uuid4()
    }

if __name__ == "__main__":
    conn = psycopg2.connect(
        host='localhost',
        database='financial_db',
        user='postgres',
        password='postgres',
        port=5432
    )

    transaction = generate_transaction()
    cur = conn.cursor()
    print(transaction)

    cur.execute(
        """
        INSERT INTO transactions(transaction_id, user_id, timestamp, amount, currency, city, country, merchant_name, payment_method, 
        ip_address, affiliateId, voucher_code)
        VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (transaction["transactionId"], transaction["userId"], datetime.fromtimestamp(transaction["timestamp"]).strftime('%Y-%m-%d %H:%M:%S'),
              transaction["amount"], transaction["currency"], transaction["city"], transaction["country"],
              transaction["merchantName"], transaction["paymentMethod"], transaction["ipAddress"],
              transaction["affiliateId"], transaction["voucherCode"])
    )

    cur.close()
    conn.commit()