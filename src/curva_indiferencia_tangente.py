def curva_indiferencia_tangente(y1,y2,alpha,beta,N,x2_max):
    def u_func(x1,x2,alpha, beta):
      return x1**alpha * x2**beta

    def objective(x1,x2,alpha,u):
      return u_func(x1,x2,alpha,beta) - u
    # = 0 then on indifference curve with utility = u
    # a. utility in (y1,y2)
    u_y = u_func(y1,y2,alpha,beta)

    # b. allocate numpy arrays
    x1_vec = np.empty(N)
    x2_vec = np.linspace(1e-8,x2_max,N)

    # c. loop through x2
    for i,x2 in enumerate(x2_vec):

        x1_guess = 0 # initial guess
        sol = optimize.root(objective, x1_guess, args=(x2,alpha,u_y))
        # optimize.root -> solve objective = 0 starting from x1 = x1_guess

        x1_vec[i] = sol.x[0]

    return x1_vec,x2_vec
