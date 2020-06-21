from grade_rank_system import GradeRankSystem

if __name__ == "__main__":
    grs_rank = GradeRankSystem()
    grs_id = GradeRankSystem()


    grs_rank.read('score.csv')
    print(grs_rank.sort())
    grs_rank.write('score_rank_result.csv')

    grs_id.read('score.csv')
    print(grs_id.sort("gid"))
    grs_id.write('score_id_result.csv',"gid")