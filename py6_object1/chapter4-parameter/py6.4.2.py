#
def change(n):
    n = 'ls'


name = 'wb'
change(name)
print(name)  # wb 没变


def change2(n):
    n[0] = 'ls'


name2 = ['wb', 'dfy']
# change2(name2)
# print(name2)  # ['ls', 'dfy'] 变化了 又是地址的问题. 引用是没有变的

# 要想不改变name
change2(name2[:])
# n =name2[:]   此时 n is not name2
# n[0] = 'ls'
#
print(name2)  # ['wb', 'dfy']

# 和java一样.
# public static void main(String[] args) {
#   String name = "1";
#   change(name);
#   System.out.println(name); // 1
#   String[] arr = {"a","b"};
#   change(arr);
#   System.out.println(Arrays.toString(arr)); //[s, b]
# }
#
# private static void change(String n) { n = "s";}
#
# private static void change(String[] n) {n[0] = "s";}
