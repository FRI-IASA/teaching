;; problem file: blocksworld-prob1.pddl

(define (problem blocksworld-prob1)
  (:domain blocksworld)
  (:objects a b c d)
  (:init (on-table a) (handempty) (on-table b) (on-table c) (on-table d) (clear a) (clear b) (clear c) (clear d))
  (:goal (and (on a b) (on b c) (on c d))))