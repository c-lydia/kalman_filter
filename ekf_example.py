import numpy as np

def f(x, t):
    # continuous dynamics converted to discrete via Euler (sample time applied outside)
    # x = [omega, a, b]
    omega, a, b = x
    dx1 = -a * omega + 1.5 * np.sin(t) + b
    dx2 = 0.0
    dx3 = 0.0
    return np.array([dx1, dx2, dx3])

def g(x):
    # measurement: y = omega
    return np.array([x[0]])

def A_continuous(x, t):
    # Jacobian of f wrt x (continuous-time)
    omega, a, b = x
    return np.array([[-a, -omega, 1.0],
                     [0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0]])

def C_jacobian(x):
    # Jacobian of g wrt x
    return np.array([[1.0, 0.0, 0.0]])

def ekf_predict(x, P, Ts, Qc, t):
    # discrete-time predict using Euler discretization
    # x_{k} = x_{k-1} + Ts * f(x_{k-1}, t)
    x_pred = x + Ts * f(x, t)
    A = np.eye(3) + Ts * A_continuous(x, t)
    P_pred = A @ P @ A.T + Ts * Qc
    return x_pred, P_pred

def ekf_update(x_pred, P_pred, y, R):
    C = C_jacobian(x_pred)
    S = C @ P_pred @ C.T + R
    K = P_pred @ C.T @ np.linalg.inv(S)
    x_upd = x_pred + (K @ (y - g(x_pred))).reshape(-1)
    P_upd = (np.eye(len(x_pred)) - K @ C) @ P_pred
    return x_upd, P_upd

def simulate_and_run(Ts=0.1, N=200):
    t = 0.0
    # true initial state
    x_true = np.array([0.5, 0.1, 0.2])
    # initial estimate
    x = np.array([0.0, 0.0, 0.0])
    P = np.diag([0.5, 0.5, 0.5])

    # continuous process noise covariance (Qc) and measurement noise (R)
    Qc = np.diag([0.1, 0.01, 0.01])
    R = np.array([[0.05]])

    history = []

    for k in range(N):
        # simulate true system (Euler discrete approx)
        w = np.random.multivariate_normal(np.zeros(3), Qc) * np.sqrt(Ts)
        x_true = x_true + Ts * f(x_true, t) + w

        # measurement
        v = np.random.normal(0, np.sqrt(R[0,0]))
        y = np.array([x_true[0] + v])

        # EKF predict
        x_pred, P_pred = ekf_predict(x, P, Ts, Qc, t)

        # EKF update
        x, P = ekf_update(x_pred, P_pred, y, R)

        history.append((t, x_true.copy(), x.copy(), P.copy(), y.copy()))
        t += Ts

    return history

if __name__ == '__main__':
    hist = simulate_and_run()
    # print final results
    t, x_true, x_est, P, y = hist[-1]
    print('Final time: {:.2f}s'.format(t))
    print('True state: ', x_true)
    print('Estimated:  ', x_est)
    print('Measurement: ', y)

    # Prepare and save plots
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        times = np.array([h[0] for h in hist])
        true_vals = np.vstack([h[1] for h in hist])
        est_vals = np.vstack([h[2] for h in hist])
        meas = np.hstack([h[4][0] for h in hist])

        fig, ax = plt.subplots(3, 1, figsize=(8, 8), sharex=True)
        ax[0].plot(times, true_vals[:,0], label='true omega')
        ax[0].plot(times, est_vals[:,0], label='est omega', linestyle='--')
        ax[0].plot(times, meas, label='measurement', linestyle=':', alpha=0.6)
        ax[0].legend()
        ax[0].set_ylabel('omega')

        ax[1].plot(times, true_vals[:,1], label='true a')
        ax[1].plot(times, est_vals[:,1], label='est a', linestyle='--')
        ax[1].legend()
        ax[1].set_ylabel('a')

        ax[2].plot(times, true_vals[:,2], label='true b')
        ax[2].plot(times, est_vals[:,2], label='est b', linestyle='--')
        ax[2].legend()
        ax[2].set_ylabel('b')
        ax[2].set_xlabel('time [s]')

        plt.tight_layout()
        out_path = 'ekf_plot.png'
        fig.savefig(out_path, dpi=150)
        print(f'Plot saved to {out_path}')
    except Exception as e:
        print('Plotting failed:', e)
