# def remove_newlines(fname):
#     #flist = open(fname).readlines()
#     with open(fname, 'r') as flist:
#         return [s.rstrip('\n') for s in flist]
#
# print(remove_newlines("/Users/denia.dobras/RepoDeniaDecember/text.txt"))







with open('/Users/denia.dobras/RepoDeniaDecember/text.txt') as txt:
    cleantxt = txt.read()
    cleantxt = cleantxt.replace('\n', '')

print(cleantxt)