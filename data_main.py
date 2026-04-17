import geometry_utils
import shape_calculator

from data_package import remove_duplicates, strip_whitespaces, calculate_mean, find_maximum, find_minimum


def main():

    operations = {
        "circle_area": geometry_utils.circle_area,
        "circle_perimeter": geometry_utils.circle_perimeter,
        "rectangle_area": geometry_utils.rectangle_area,
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area
    }

    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: _area, _perimeter (e.g., circle_area)")

    op_name = input("Enter the operation you want to perform (eg; circle_area): ").strip().lower()

    if op_name not in operations:
        print("Invalid operation! Check format. (eg; shape_calculation) ")
    else:
        try:
            if "circle" in op_name:
                r = float(input("Enter radius: "))
                result = operations[op_name](r)

            elif "rectangle" in op_name:
                w = float(input("Enter width: "))
                h = float(input("Enter height: "))
                result = operations[op_name](w, h)

            elif "triangle" in op_name:
                wb = float(input("Enter base: "))
                h = float(input("Enter height: "))
                result = operations[op_name](wb, h)

            if result == "Error":
                print("Input Error: Dimensions must be strictly positive.")
            else:
                print(f"Result: {result:.2f}")

        except ValueError:
            print("Input Error: Please enter valid numeric values.")

    
    prompt = "Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8, 21): "
    user_input = input(prompt)

    try:
        raw_list = user_input.split(',')
        stripped_list = strip_whitespaces(raw_list)

        num_list = [float(x) for x in stripped_list if x != ""]

        unique_list = remove_duplicates(num_list)

        print(f"Cleaned and unique data: {unique_list}")
        print("-" * 20)
        print(f"Mean: {calculate_mean(unique_list):.2f}")
        print(f"Maximum: {find_maximum(unique_list)}")
        print(f"Minimum: {find_minimum(unique_list)}")

    except ValueError:
        print("Data Error: Please make sure you only enter numbers separated by commas.")


if __name__ == "__main__":
    main()