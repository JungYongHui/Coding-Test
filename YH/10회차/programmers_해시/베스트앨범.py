def solution(genres, plays):
    answer = []

    music = []

    for idx in range(len(genres)):
        music.append([genres[idx], plays[idx], idx])

    music = sorted(music, key=lambda x: (x[0], -x[1], x[2]))

    tot_gen = {}
    for i, j, k in music:
        tot_gen[i] = tot_gen.get(i, 0) + j
    tot_gen = sorted(tot_gen.items(), key=lambda x: -x[1])

    for i, _ in tot_gen:
        count = 0
        for idx in range(len(music)):
            if i == music[idx][0]:
                if count == 2:
                    break
                answer.append(music[idx][2])
                count += 1

    return answer