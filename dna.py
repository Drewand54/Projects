import csv
import sys


def main():
    # Check for command-line usage

    if len(sys.argv) != 3:
        print("Enter two arguments")
        sys.exit(1)

    f = open(f"{sys.argv[2]}", "r")
    sequence = []
    sequence = f.read()

    #  Find longest match of each STR in DNA sequence

    sequence = {
        "AGATC": str(longest_match(sequence, "AGATC")),
        "TTTTTTCT": str(longest_match(sequence, "TTTTTTCT")),
        "AATG": str(longest_match(sequence, "AATG")),
        "TCTAG": str(longest_match(sequence, "TCTAG")),
        "GATA": str(longest_match(sequence, "GATA")),
        "TATC": str(longest_match(sequence, "TATC")),
        "GAAA": str(longest_match(sequence, "GAAA")),
        "TCTG": str(longest_match(sequence, "TCTG")),
    }

    # Check database for matching profiles
    with open(f"{sys.argv[1]}", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if sys.argv[1][10] == "l":
                if (
                    sequence["AGATC"] == row["AGATC"]
                    and sequence["TTTTTTCT"] == row["TTTTTTCT"]
                    and sequence["AATG"] == row["AATG"]
                    and sequence["TCTAG"] == row["TCTAG"]
                    and sequence["GATA"] == row["GATA"]
                    and sequence["TATC"] == row["TATC"]
                    and sequence["GAAA"] == row["GAAA"]
                    and sequence["TCTG"] == row["TCTG"]
                ):
                    print(row["name"])
                    sys.exit(0)
            elif sys.argv[1][10] == "s":
                if (
                    sequence["AGATC"] == row["AGATC"]
                    and sequence["AATG"] == row["AATG"]
                    and sequence["TATC"] == row["TATC"]
                ):
                    print(row["name"])
                    sys.exit(4)
        else:
            print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
