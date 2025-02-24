# Copyright (c) 2025 Thomas Duggan
# This work is licensed under CC BY-SA 4.0


def promotable_eo(grades):
    """Determine whether or not a student is promotable from Engineering One.

    Parameters
    ----------
    grades : iterable
        An iterable of non-negative integers, representing the student's grades in their
        Engineering One courses.

    Returns
    -------
    A boolean value indicating whether or not a student is promotable
    """
    
    
    ################ Math / Assumptions ################
    
    avg = sum(grades)/len(grades) # average of grades
    
    promotability = True # assumes promotable until proven otherwise
    
    ################ Failsafe ################
    
    if len(grades) < 9:
        promotability = False
    
    ################ Path ################
    
    for i in range(len(grades)):
        if grades[i] < 55:		# if less than 55 is found in grades, you are not promotable
            promotability = False
            
    if avg < 65:
        promotability = False	# if average is less than 65, you are not promotable
        
    return promotability
    
   
def promotion_decision(term, grades, history=[]):
    """Determine the promotability of a student in an Engineering academic term
    beyond Engineering One.

    Parameters
    ----------
    term : int
        The student's academic term (from 3 to 8, inclusive)

    grades : iterable
        Course results representing the student's grades in their courses for the term.
        These results will be strings containing either a non-negative integer or the
        string "ABS" (absent, i.e., missed the final exam and needs to write a deferred
        exam).

    history : iterable
        Strings representing the student's previous decision history, e.g.,
        ["PAS", "FR4", "PRP", "FRW"].

    Returns
    -------
    A promotion decision code, e.g., PAS, PRP, FR3, FR4, ..., FRW, FQW or EA.
    """
    
    ################ Failsafes ################
        
    stop = False
    
    if "ABS" in grades: 				# Failsafe to prevent program from doing mathematical operations with a string
        stop = True						# 		PROGRAM WILL NOT WORK WITH THIS REMOVED
        dcode = "EA"
    
    if stop == False:
        if (term >8) or (term <3):		# Failsafe to prevent term numbers outside of range
            stop = True					# 		Program works with this removed
        
        for uwu in range(len(grades)):	# Failsafe to prevent negative grades
            if grades[uwu] < 0:			# 		Program works with this removed
                stop = True				# (Note: "uwu" is an arbitrary variable and is only used to iterate in this function)

    ################ Bool Conversion ################
        
    if stop == False:
        avg = sum(grades)/len(grades) 	# Average of grades
        if avg >= 60:
            bad_average = False
        else:
            bad_average = True
        
        
        for i in range(len(grades)):
            if grades[i] >= 50:       	# if a number less than 50 appears in grades, you have failed a course
                course_failure = False
            else:
                course_failure = True
                break
        
        
        for i in range(len(grades)):
            if grades[i] >= 40:      	# if a number less than 40 appears in grades, you extremely failed a course
                course_extreme_failure = False
            else:
                course_extreme_failure = True
                break
            
            
        if ("FR"+str(term) in history):
            previous_failure = True
        else:                          	# Tests if you have failed the current term
            previous_failure = False
        
        failures = 0
        for owo in range(len(history)):	# Tests how many time FRn or FRW or FQW appears in history
            if True == ("FQW" in history or "FRW" in history or "FR3" in history or "FR4" in history or "FR5" in history or "FR6" in history or "FR7" in history or "FR8" in history):
                failures += 1
            
        ################ Path ################
            
        if bad_average == True:				# runs if average is less than 60
            if (previous_failure == True) or (failures >= 2): 
                dcode = "FQW"
            else:
                if course_extreme_failure == True: 	# runs if a number less than 40 appeared in grades
                    dcode = "FRW"
                else:
                    dcode = "FR"+str(term) 			# takes the number of "term" and attaches it to the FRn decision code
            
        elif course_failure == True:  				# runs if a number less than 50 appears in grades, AND average is more than or equal to 60
            if course_extreme_failure == True:		# runs if a number less than 40 appears in grades
                if (previous_failure == True) or (failures >= 2): 			# \
                    dcode = "FQW"						# \
                else:									# \
                    if course_extreme_failure == True:	# < - identical to above
                        dcode = "FRW"					# /
                    else:								# /
                        dcode = "FR"+str(term) 			# /
            else:
                dcode = "PRP" 	# if all courses are above or equal to 40, and average is above or equal to 60, this will run
            
        else:
            dcode = "PAS" 		# if all courses are above or equal to 50, and average is above or equal to 60, this will run
        
    return dcode