def solution(phone_book):
    ################################################
    # sol 1 (non pass)
    ################################################
    # for idx, num in enumerate(phone_book):
    #     for idx2 in range(idx+1, len(phone_book)):
    #         if num.startswith(phone_book[idx2]):
    #             return False
    #         if phone_book[idx2].startswith(num):
    #             return False
    ################################################
    # sol 2 (pass)
    ################################################
    # phone_book.sort()

    # for idx in range(len(phone_book)-1):
    #     if phone_book[idx+1].startswith(phone_book[idx]):
    #         return False

    # return True
    ################################################
    # sol 3 ()
    ################################################
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        # 2. 접두어가 Hash map에 존재하는지 찾는다
    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    return True