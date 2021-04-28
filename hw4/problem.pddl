(define (problem problem_logistics)
(:domain basic_logistics)
(:requirements :strips :typing)

    (:objects 
        wp1 wp2 wp3 wp4 wp5 wp6 wp7 wp8 wp9 wp10 wp11 - location
        t1 t2 - truck
        dr1 dr2 - driver
        pack1 pack2 pack3 pack4 - package
    )
    
    (:init
        ;; initial location of drivers
        ()
        ()
        
        ;; initial location of trucks
        ()
        ()
        
        ;; intial location packages
        ()
        ()
        ()
        ()
        
        ;; routes that connect the locations
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
        ()
    )
    
    (:goal (and 
        ;; drivers home
        (at dr1 wp1)
        (at dr2 wp1)
        
        ;; packages delivered
        (at pack1 wp9)
        (at pack2 wp2)
        (at pack3 wp9)
        (at pack4 wp2)
    ))
)