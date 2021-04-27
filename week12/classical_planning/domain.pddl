;; domain.pddl for blocksworld

(define (domain blocksworld)
  (:requirements :strips)

  (:predicates (clear ?x)
               (on-table ?x)
               (holding ?x)   
               (handempty)
               (on ?x ?y))

  (:action pick
           :parameters (?ob)
           :precondition (and (clear ?ob) (on-table ?ob) (handempty))
           :effect (and (holding ?ob) (not (clear ?ob)) (not (handempty)) (not (on-table ?ob))))



  (:action place
           :parameters (?ob ?underob)
           :precondition (and  (clear ?underob) (not (handempty)) (holding ?ob))
           :effect (and (clear ?ob) (on ?ob ?underob) (handempty)
                        (not (clear ?underob)) (not (holding ?ob)))))
