# name variable with format chararcters
formatter = "%r %r %r %r"

# print variable with format chararcters in the ()
print formatter % (1,2,3,4)
# print variable with format chararcters in the ()
print formatter % ("one", "two", "three", "four")
# print variable with format chararcters in the ()
print formatter % (True, False, False,True)
# print variable with format chararcters in the ()
print formatter % (formatter, formatter, formatter, formatter)
# print variable with format chararcters in the (strings)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
