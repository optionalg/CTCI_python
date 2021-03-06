# Data Structures questions - chapters 1-4

# ================== chapter 1 =================== #

def is_all_unique_chars(s):
    """
    returns if a string has all unique characters
    """
    # build hashset
    my_dict = {}
    for c in s:
        if c in my_dict:
            return False
        my_dict[c] = True
    return True


def is_all_unique_no_space(s):
    """
    returns if a string has all unique characters without data structs
    """
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True


def is_permutation(a, b):
    """
    returns whether string a is a permutation of string b
    """
    
    # strategy 1: sort both strings then compare them traditionally
    a_list, b_list = [c for c in a], [c for c in b]
    a_list.sort()
    b_list.sort()
    return a_list == b_list


def percent_20_replacements(s):
    """
    replace all instances of a space with a %20
    """

    # build a new string
    new_str = ''
    for c in s:
        if c == ' ':
            new_str += '%20'
        else:
            new_str += c
    return new_str


def percent_20_in_place(s, n):
    """
    replace all instances of a space with a %20 in place
    n refers to the length of the string (character array)
    """
    # make one pass to calculate the final size to allocate
    # then make a second pass to fill out the array
    # tbh excuse to work with arrays

    spaces = 0 
    for c in s:
        if c == ' ':
            spaces += 1

    # for each space - we gain 2 characters

    new_len = n + 2 * spaces 
    new_str = [' ' for _ in range(new_len)]

    j = 0  # counter for new_str
    for i in range(len(s)):
        if s[i] == ' ':
            new_str[j] = '%'
            new_str[j+1] = '2'
            new_str[j+2] = '0'
            j += 3 
        else:
            new_str[j] = s[i]
            j += 1
    ret_str = ''
    for c in new_str:
        ret_str += c
    return ret_str

        
def palindrome_perm(s):
    """
    for all permutations of a string s, determine if any are a palindrome
    """
    # populate a hashset - throw out duplicates
    # if remaining is one or zero characters - true

    my_dict = {}
    for c in s:
        if c in my_dict:
            del my_dict[c]
        else:
            my_dict[c] = True

    return len(my_dict) <= 1


def one_away(a, b):
    """
    three options - insert, remove or replace
    """

    def replace_check(s1, s2):
        """
        check if replacing a single character in s1 becomes s2
        """
        if len(s1) != len(s2):
            return False
        found_diff = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if found_diff:
                    return False
                found_diff = True
        return True

    
    def insert_check(s1, s2):
        """
        inserting a char into s1 becomes s2
        """
        m = len(s1)
        n = len(s2)
        if m + 1 != n:
            return False
        i, j = 0, 0
        inserted = False
        while i < m and j < n:
            if s1[i] != s2[j]:
                if inserted:
                    return False
                inserted = True
                j += 1
            i += 1
            j += 1
        return True

    m = len(a)
    n = len(b)
    if m == n:
        return replace_check(a, b)
    if m > n:
        return insert_check(b, a)
    return insert_check(a, b)


def str_compress(s):
    """
    take the string - reduce to single instance with count
    """
    count = 0
    last = ''
    ret_str = ''
    for i in range(len(s)):
        if s[i] == last:
            count += 1
        else:
            if last:
                ret_str += last + str(count)
            last = s[i]
            count = 1
    ret_str += last + str(count) 
    return ret_str


def rotate_matrix(M):
    """
    assume given a square matrix
    layer by layer
    save temp for top
    top is set to left
    left is set to bot
    bot is set to right
    right is set to temp
    change layer
    """
    n = len(M)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        # now do the swap
        for i in range(first, last):
            offset = i - first
            temp_top = M[first][i]
            # left to top
            M[first][i] = M[last-offset][first] 
            # bottom to left
            M[last-offset][first] = M[last][last-offset] 
            # right to bottom
            M[last][last-offset] = M[i][last]
            # top to right
            M[i][last] = temp_top
    return M
    
def zero_matrix(M):
    """
    M is a (m by n) matrix with m rows and n columns
    for each 0 entry - zero out everythign else
    """
    # one pass to find all the zeros (n^2)
    # populate two lists : cols and rows for zeros
    # then go thru each element - checking if its in a banned row/col
    m = len(M)
    n = len(M[0])
    rows, cols = [], []
    for i in range(m):
        for j in range(n):
            if M[i][j] == 0:
                cols.append(i)
                rows.append(j)
    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                M[i][j] = 0
                
    return M


def is_string_rot(a, b):
    """
    use a single call of is_substring with
    abab
        because it must show up in the ba segement if its going to
    waterbottlewaterbottle
       erbottlewat
    think reductions 
    """
    def is_substring(a, b):
        """
        return true if a is a substring of b
        a in b works in python
        """
        return a in b
    aa = a + a 
    return is_substring(b, aa)


# ================== chapter 2 =================== #

class Link:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def compare_to(a, target):
		if not a and not target:
			return True
		if (a and not target) or (a and not target):
			return False
		if a.val != target.val:
			return False
		if a.next == None and target.next == None:
			return True
		return Link.compare_to(a.next, target.next)

	def len(self):
		c = 0
		while(self):
			self = self.next
			c += 1
		return c

	def append(self, target):
		self.next = target

	def __str__(self):
		return '(' + str(self.val) + ', ' + str(self.next) + ')'

	def __repr__(self):
		return str(self)

class DLink:
    """
    doubly linked list - for queues and stacks
    """

    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


    def compare_to(a, target):
        if not a and not target:
            return True
        if (a and not target) or (a and not target):
            return False
        if a.val != target.val:
            return False
        return Link.compare_to(a.next, target.next)

    def len(self):
        c = 0
        while(self):
            self = self.next
            c += 1
        return c

    def append(self, target):
        self.next = target
        target.prev = self

    def __str__(self):
        return '(' + str(self.val) + ', ' + str(self.next) + ')'

    def __repr__(self):
        return str(self)

def rdl(head):
    """
    remove duplicate link - solved recursively
    keep track of previous (start None) and curr (start head)
    if current in seen? skip it by changing prev's next
        shift over
    """
    
    seen = {}
    prev = None
    curr = head
    while curr:
        if curr.val in seen:
            prev.next = curr.next
        else:
            seen[curr.val] = True
            prev = curr
        curr = curr.next
    return head
         
def kth_to_first(head, k):
    """
    alt helper...
    """
    if k == 0:
        return head
    else:
        return kth_to_first(head.next, k - 1)

def kth_to_last(head, k):
    """
    assumptions:
    1) k <= len of the list 
    2) k = 1 is the last element
    """
    list_len = head.len()
    while k < list_len:
        head = head.next
        k += 1
    return head

# make a ruler of length k (gap between two nodes)
# then slide both down till the end lol

def remove_mid_link(target):
    """
    take the target node, and make it grab its next's info
    """

    if not target or not target.next:
        # can't be at the end
        return False
    next = target.next
    target.val = next.val
    target.next = next.next

def partition_ll(head, target):
    """
    build a before list and an after list
    """
    val = target.val
    all_vals = []
    n = head
    while (n):
        all_vals.append(n.val)
        n = n.next
    all_vals.sort()
    if all_vals:
        new_head = Link(all_vals[0])
        new_tail = new_head
    for v in all_vals[1:]:
        new_tail.next = Link(v)
        new_tail = new_tail.next
    return new_head 

    
def sum_ll(a, b):
    """
    turn a linked list into a number, then conventionally add them
    """
    def link_to_num(link):
        """
        Link(7, Link(1, Link(6))) becomes 617
        """
        val = 0
        place = 1
        while link:
            val += (link.val * place)
            place *= 10
            link = link.next
        return val 

    def num_to_link(num):
        """
        617 becomes Link(7, Link(1, Link(6))) 
        gets the ones, then get the tens etc...
        """
        
        link = Link(num % 10)
        head = link
        while num >= 10:
            num = num // 10
            link.next = Link(num % 10)
            link = link.next
        return head 

    return num_to_link(link_to_num(a) + link_to_num(b)) 
        

def is_link_palindrome(link):
    """
    return if linked list is a palindrome
    maintain a head and tail, then wait till next is tail
    """
    if not Link:
        return 
    tail = None
    head = link

    while head:
        # use a runner to find the tail
        runner = head
        while runner.next != tail:
            runner = runner.next
        # found it set runner to the one before the tail
        if runner.val != head.val:
            return False
        if runner == head or (head.next == runner):
            return True
        tail = runner
        head = head.next
    return True


def link_intersection(a, b):
    """
    return the link that is the intersection between the two lists
    1 2 3 4 5
    2 4 5 
    .... 4 5 are the same branches think of a wishbone
    ...
        ...
     ..
    """
    # obs 1 - if they're intersecting, then they have the same ending
    def find_last(node):
        """
        find the last node in a linked list
        """
        if not node:
            return node
        while node.next:
            node = node.next
        return node

    last_a = find_last(a)
    last_b = find_last(b)

    if last_a != last_b:
        # no intersection
        return None 

    # where to find? cut off extra stuff on the longer one
    # advace one at a time till looking at the same node

    a_len = a.len()
    b_len = b.len()

    if a_len > b_len:
        # cut off the diff from a
        diff = a_len - b_len
        for _ in range(diff):
            a = a.next
    elif a_len < b_len:
        # cut off the diff from b 
        diff = b_len - a_len
        for _ in range(diff):
            b = b.next

    while a != b:
        a = a.next
        b = b.next

    return a


def loop_detect(node):
    """
    return true or false if the above linked list has a loop
    use a slow runner along side a fast runner
    if they meet - then we found a loop
    """

    slow = node
    fast = node
    count = 0
    while slow and fast and count < 10:
        slow = slow.next
        if fast.next and fast.next.next:
            fast = fast.next.next
        else:
            # got to the end
            return False 
        if slow == fast:
            return True 
        count += 1
    return False


def find_loop_point(node):
    """
    first use loop_detect - to see if there's a loop
    if there is a loop - return the first node that's a repeat
    Observations
        1) after k moves slow has moved k and fast has moved 2k
        2) the difference of k % the loop size is their gap
        3) we use phase one to find where they meet
        4) they must meet k moves before the goal node in the loop
        5) which is dist from head - so move slow and set fast to head
        6) return the new intersection

    """
    if not loop_detect(node):
        return False 

    slow = node
    fast = node
    
    done = False
    while slow and fast and not done:
        slow = slow.next
        if fast.next and fast.next.next:
            fast = fast.next.next
            if slow == fast:
                done = True
                break
                
        else:
            # the fast runner hit the end - can't be a loop
            return False

    # part 2
    fast = node  # back to the head
    while fast != slow:
        # one at a time... k times
        fast = fast.next
        slow = slow.next

    return fast  # or return slow

            
# ================== chapter 3 =================== #

class Stack():
    """ 
    representing the stack as as linked list
    """
    def __init__(self, init_list=[]):
        """
        can initialize the stack with a python list of values
        stack object has a head and tail
        """
        if init_list:
            current = DLink(init_list[0])
            self.head = current
            for val in init_list[1:]:
                current.next = DLink(val)
                current = current.next
            self.tail = current
            self.length = len(init_list)
        else:
            self.head = None 
            self.tail = None 
            self.length = 0

    def peek(self):
        """
        return the top element without removing it
        """
        return self.head

    def pop(self):
        """
        return the top element and remove it
        """
        if self.head:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return temp 
        return None

    def push(self, new_elem):
        """
        add something on the top
        """
        new_node = Link(new_elem)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return bool(new_elem) 

    def __len__(self):
        return self.length

    def __str__(self):
        """
        call the linked list str
        """
        return "Stack: " + str(self.head)

    def __repr__(self):
        return str(self)


# single array to manage three stacks
class TripleStack():
    """
    single array - 3 stacks inside
    """
    def __init__(self):
        """
        counts - use this to find where in the array to go

        """
        self.main_list = []
        self.first = 0 
        self.second = 0 
        self.third = 0 


    # PEEK COMMANDS 

    def peek_one(self):
        if self.first:
            return self.main_list[0]
        else:
            return "First Stack indefined"

    def peek_two(self):
        if self.second:
            return self.main_list[self.first]
        else:
            return "Second Stack indefined"
        
    def peek_three(self):
        if self.third:
            return self.main_list[self.first + self.second]
        else:
            return "Third Stack indefined"

    # POP COMMANDS

    def pop_one(self):
        if self.first:
            head = self.main_list[0]
            self.main_list = self.main_list[1:]
            self.first -= 1
            return head
        else:
            return "First Stack undefined"

    def pop_two(self):
        if self.second:
            head = self.main_list[self.first]
            self.main_list = self.main_list[self.first + 1:]
            self.second -= 1
            return head
        else:
            return "Second Stack undefined"

    def pop_three(self):
        if self.third:
            head = self.main_list[self.first + self.second]
            self.main_list = self.main_list[self.first + 
                    self.second + 1:]
            self.third -= 1
            return head
        else:
            return "Third Stack undefined"

    def push_one(self, elem):
        self.first += 1
        self.main_list = [elem] + self.main_list

    def push_two(self, elem):
        self.second += 1
        index = self.first
        self.main_list = self.main_list[:index] + [elem] + self.main_list[index:]

    def push_three(self, elem):
        self.third += 1
        index = self.first + self.second
        self.main_list = self.main_list[:index] + [elem] + self.main_list[index:]

    def __str__(self):
        return "Triple Stack " + str(self.main_list)
    
    def __repr__(self):
        return str(self)

# 3.2 Stack Min
class MinStack():
    """
    regular stack, but each node has the min in its current state
    node represented with a tuple
    tuple = (val, min)
    """
    def __init__(self):
        self.main_list = []
        self.min = None

    def push(self, val):
        """
        push a tuple with the val, then the min)
        """
        if self.min:
            tup = (val, min(self.min, val))
        else:
            tup = (val, val)  # can't take the min of 'None'
        self.min = tup[1]
        self.main_list = [tup] + self.main_list

    def pop(self):
        """
        pop the top element from the list
        """
        top_tup = self.main_list[0]
        self.main_list = self.main_list[1:]
        self.min = self.main_list[0][1] 
        return top_tup[0]  # don't return min, return the element
        
    def get_min(self):
        return self.min


    # alternatively - keep a second list
    # only pop an element from the "mins here list" when equal to min
    # can have a whole stack of say ... 5s
    # less than or equal to the last reigning min? - push it
    # saves space in theory - but all the same number does nothing
        

class PlatesStack():
	"""
	init function with a stack cap
	anything else goes to a second stack
	maintain a stack of stacks
		pop from the most recent stack lol
	I'm assuming cap is inclusive (at capacity is ok)
	"""

	def __init__(self, cap=None):
		"""
		no cap means a normal stack
		"""
		self.stacks = Stack()
		self.curr = Stack()
		self.stacks.push(self.curr)
		self.cap = cap
	
	def pop(self):
		"""
		pop from the current stack
		if the current stack is empty pop a stack off the shelf
		"""
		if self.curr and len(self.curr) > 0:
			return self.curr.pop()
		elif self.stacks and len(self.stacks) > 1:
			# there will always be at least one stack
			self.curr = self.stacks.pop()
			
			return self.curr.pop()
		else:
			return "Stack undefined"
	
	def push(self, elem):
		"""
		if there's room, add it to the current stack
		otherwise - make a new stack and add it to that one
		"""
		if len(self.curr) < self.cap:
			self.curr.push(elem)
		else:
			self.curr = Stack()
			self.curr.push(elem)
	
	def __str__(self):
		return str(self.stacks)
	
	def __repr__(self):
		return str(self)

			
		

# ================== utils =================== #


def test(call, result=True):
    if call != result:
        print("got: " + str(call))
        raise ValueError("test failed")


# ================== tests =================== #

# CHAPTER 1 

# 1.1 - unique chars
test(is_all_unique_chars("abcde"), True)
test(is_all_unique_chars("thelazydog"), True)
test(is_all_unique_chars("hello"), False)
test(is_all_unique_no_space("abcde"), True)
test(is_all_unique_no_space("thelazydog"), True)
test(is_all_unique_no_space("hello"), False)

# 1.2 - permutations
test(is_permutation("lol", "lol"), True)
test(is_permutation("abcde", "abced"), True)
test(is_permutation("lol", "lolz"), False)
test(is_permutation("123456asdfasdf", "12313asdfasdf"), False)

# 1.3 - %20 replacements
test(percent_20_replacements("hello world test"), 
        "hello%20world%20test")
test(percent_20_in_place("hello world test", 16), 
        "hello%20world%20test")

# 1.4 - palindrome perm
test(palindrome_perm("tactcoa"), True)
test(palindrome_perm("lool"), True)
test(palindrome_perm("o"), True)
test(palindrome_perm("oo"), True)
test(palindrome_perm("abc"), False)
test(palindrome_perm("abbb"), False)

oa = one_away
# 1.5 - one away
test(oa("pale", "ple"))
test(oa("pales", "pale"))
test(oa("pale", "bale"))
test(oa("pale","bake"), False)

# 1.6 - string compression
test(str_compress("aabcccccaaa"), "a2b1c5a3")

# 1.7 - rotate matrix
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M_rot = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
rotate_matrix(M)
test(M, M_rot)

# 1.8 - zero matrix
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = zero_matrix(M)
test(res, M)
M = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
A = [[1, 0, 3], [0, 0, 0], [7, 0, 9]]
test(zero_matrix(M), A)

# 1.9 - string rotation
orig = "waterbottle"
rot = "erbottlewat"
test(is_string_rot(orig, rot))
test(is_string_rot(orig, "test"), False)

# CHAPTER 2

# 2.1 - remove duplicates from a linked list
empty = Link()
one = Link(1)
one_two = Link(1, Link(2))
one_one = Link(1, Link(1))
two_one = Link(2, Link(1))
one_one_one_one = Link(1, Link(1, one_one))
two_two_one_one = Link(2, Link(2, one_one))
test(Link.compare_to(one_one, Link(1, Link(1))), True)
test(Link.compare_to(rdl(one_two), rdl(one)), False)
test(Link.compare_to(rdl(one_two), rdl(one_two)), True)
test(Link.compare_to(rdl(one_two), rdl(one_one)), False)
test(Link.compare_to(rdl(one_one_one_one), one), True)
test(Link.compare_to(rdl(two_two_one_one), two_one), True)

# 2.2 - return kth to last element from a linked list
one_one = Link(1, Link(1))
two_two_one_one = Link(2, Link(2, one_one))
ktl = kth_to_last 
test(Link.compare_to(ktl(two_two_one_one, 1), Link(1)), True)
test(Link.compare_to(ktl(two_two_one_one, 1), Link(2)), False)
test(Link.compare_to(ktl(two_two_one_one, 2), one_one), True)
test(Link.compare_to(ktl(two_two_one_one, 2), one_one_one_one), False)
test(Link.compare_to(ktl(two_two_one_one, 4), two_two_one_one), True)

# 2.3 - delete a middle mode from a linked list
the_list = Link(1, Link(2, Link(3)))
mid = the_list.next
ends = Link(1, Link(3))
second_list = Link(1, Link(2, Link(3, Link(4))))
second_mid = second_list.next
rest = Link(1, Link(3, Link(4)))
rml = remove_mid_link
rml(mid)
test(Link.compare_to(the_list, ends))
rml(second_mid)
test(Link.compare_to(second_list, rest))

# 2.4 partition a linked list around x
in_l =  Link(3, Link(5, Link(8, Link(5, Link(10, Link(2, Link(1)))))))
out_l = Link(1, Link(2, Link(3, Link(5, Link(5, Link(8, Link(10)))))))
test(Link.compare_to(partition_ll(in_l, in_l.next), out_l)) 

# 2.5 sum linked list representations of numbers
six_one_seven = Link(7, Link(1, Link(6)))
two_nine_five = Link(5, Link(9, Link(2)))
nine_one_two = Link(2, Link(1, Link(9)))
test(Link.compare_to(sum_ll(six_one_seven, two_nine_five), nine_one_two))

# 2.6 - linked list is a palindrome
test(is_link_palindrome(six_one_seven), False)
six_one_one_six = Link(6, Link(1, Link(1, Link(6))))
six_one_one_one_six = Link(6, Link(1, Link(1, Link(1, Link(6)))))
six_one_six = Link(6, Link(1, Link(6)))

test(is_link_palindrome(six_one_one_six))
test(is_link_palindrome(six_one_six))
test(is_link_palindrome(six_one_one_one_six))

# 2.7 linked list intersection
one_six = six_one_one_one_six.next.next.next.next
test(link_intersection(one_six, six_one_one_one_six), one_six)
test(link_intersection(six_one_one_one_six, one_six), one_six)
test(link_intersection(one_six, nine_one_two), None)

# 2.8 linked list loop detection
loop = Link(1, Link(2))
loop.next = loop
loop_two = Link(1)
loop_two.next = loop_two
test(loop_detect(loop)) 
test(loop_detect(one_six), False)
test(loop_detect(loop_two))

# 2.81 linked list loop search
test(find_loop_point(loop), loop)
test(find_loop_point(one_six), False)
test(find_loop_point(loop_two), loop_two)
in_l.next.next.next.next.next.next.next = in_l.next.next
test(find_loop_point(in_l), in_l.next.next)

# CHAPTER 3

# basic Stack checking
stack = Stack()
test(len(stack), 0)
stack.push(1)
stack.push(2)
test(len(stack), 2)
test(stack.head.val, 2)

test(stack.pop().val, 2)
test(stack.pop().val, 1)
test(stack.pop(), None)


# 3.1 triple stack
ts = TripleStack()
ts.push_one(1)
ts.push_one(2)
ts.push_one(3)
test(ts.main_list, [3, 2, 1])
test(ts.pop_one(), 3)
test(ts.pop_one(), 2)
ts.push_two(2)
ts.push_three(3)
test(ts.main_list, [1, 2, 3])
ts.push_two(4)
test(ts.main_list, [1, 4, 2, 3])
test(ts.pop_one(), 1)
test(ts.main_list, [4, 2, 3])
ts.push_three(5)
test(ts.main_list, [4, 2, 5, 3])
test(type(ts.pop_one()) == str)

# 3.2 Stack with minValue
ms = MinStack()
ms.push(3)
ms.push(1)
test(ms.get_min(), 1)
ms.push(2)
test(ms.get_min(), 1)
ms.push(1)
test(ms.get_min(), 1)
test([tup[0] for tup in ms.main_list], [1, 2, 1, 3])
test(ms.pop(), 1)
test(ms.pop(), 2)
test(ms.pop(), 1)
test(ms.get_min(), 3)


# 3.2 overflowing Stack checking
# plate analogy
stack = PlatesStack(5)
stack.push(1)
stack.push(2)

test(stack.pop().val, 2)
test(stack.pop().val, 1)
import pdb; pdb.set_trace()
test(stack.pop(), "Stack undefined")
stack = PlatesStack(113)
for i in range(20):
	stack.push(i)
for i in range(19):
	j = 19 - i
	test(stack.pop().val, j)
test(stack.pop(), "Stack undefined")
