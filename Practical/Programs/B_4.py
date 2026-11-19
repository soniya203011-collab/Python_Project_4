import os

# [SECURE PYTHON: SAFE INPUT VALIDATION]
def read_positive_int(prompt: str) -> int:
    raw = input(prompt).strip()
    try:
        val = int(raw)
        if val <= 0:
            print('[Security Alert] Number must be strictly positive.')
            return None
        return val
    except ValueError:
        print('[Security Alert] Invalid numeric format. Rejected safely.')
        return None

# [SECURE PYTHON: CREDENTIAL PROTECTION]
api_key = os.getenv('WAREHOUSE_API_KEY', 'FALLBACK_LOCAL_DEV_KEY')
print(f'API Token safely retrieved: {api_key[:4]}****')
# Test validation function simulation
for test_input in ['25', '-10', 'abc']:
    print(f'Testing input: {test_input}')
    # Simulated input logic
    try:
        v = int(test_input)
        print('Result:', 'Accepted' if v > 0 else 'Rejected')
    except ValueError:
        print('Result: Rejected safely by ValueError catch')
