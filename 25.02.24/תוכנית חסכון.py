def one_month_calculate(month_deposit: float) -> float:
    month_saving = month_deposit * 1.04
    return month_saving


def one_year_calculate(kik_start, monthly_deposit):
    deposit = one_month_calculate(kik_start + monthly_deposit)
    for month in range(11):
        deposit = one_month_calculate(deposit + monthly_deposit)
    return deposit


def printing_saving_info(first_deposit, monthly_deposit):
    # Your saving
    first_year_saving = one_year_calculate(first_deposit, monthly_deposit)
    second_year_saving = one_year_calculate(first_year_saving, monthly_deposit)
    third_year_saving = one_year_calculate(second_year_saving, monthly_deposit)
    fourth_year_saving = one_year_calculate(third_year_saving, monthly_deposit)
    fifth_year_saving = one_year_calculate(fourth_year_saving, monthly_deposit)
    total_saving = one_year_calculate(fifth_year_saving, monthly_deposit)

    # Imaginary character:
    imaginary_character_first_year_saving = one_year_calculate(first_deposit, monthly_deposit / 2)
    imaginary_character_second_year_saving = one_year_calculate(first_year_saving, monthly_deposit / 2)
    imaginary_character_third_year_saving = one_year_calculate(second_year_saving, monthly_deposit / 2)
    imaginary_character_fourth_year_saving = one_year_calculate(third_year_saving, monthly_deposit / 2)
    imaginary_character_fifth_year_saving = one_year_calculate(fourth_year_saving, monthly_deposit / 2)
    imaginary_character_total_saving = one_year_calculate(fifth_year_saving, monthly_deposit / 2)

    print(f"""
    In the first year you saved: {first_year_saving}, 
    In the second year you saved: {second_year_saving}, 
    In the third year you saved: {third_year_saving}, 
    In the fourth year you saved: {fourth_year_saving}, 
    In the fifth year you saved: {fifth_year_saving}, 
    in total you saved: {total_saving}.
    
    In the first year israel israeli saved: {imaginary_character_first_year_saving}, 
    In the second year israel israeli saved: {imaginary_character_second_year_saving}, 
    In the third year israel israeli saved: {imaginary_character_third_year_saving}, 
    In the fourth year israel israeli saved: {imaginary_character_fourth_year_saving}, 
    In the fifth year israel israeli saved: {imaginary_character_fifth_year_saving}, 
    in total israel israeli saved: {imaginary_character_total_saving}.
    """)


printing_saving_info(10, 120)