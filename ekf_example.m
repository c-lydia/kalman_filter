% ekf_example.m
% Extended Kalman Filter example (3-state) using Euler discretization
function ekf_example()
    Ts = 0.1;
    N = 200;
    t = 0:Ts:Ts*(N-1);

    % true initial state
    x_true = [0.5; 0.1; 0.2];
    % initial estimate
    x = [0;0;0];
    P = diag([0.5,0.5,0.5]);

    Qc = diag([0.1, 0.01, 0.01]);
    R = 0.05;

    rng('default');

    for k = 1:N
        tk = t(k);
        % simulate true system (Euler)
        w = mvnrnd([0 0 0], Qc)';
        x_true = x_true + Ts * f_cont(x_true, tk) + sqrt(Ts)*w;

        % measurement
        v = sqrt(R)*randn();
        y = x_true(1) + v;

        % predict
        [x_pred, P_pred] = ekf_predict_matlab(x, P, Ts, Qc, tk);

        % update
        [x, P] = ekf_update_matlab(x_pred, P_pred, y, R);
    end

    disp('Final true state:'); disp(x_true');
    disp('Final estimate:'); disp(x');
end

% Plot results
figure;
tt = 0:Ts:Ts*(N-1);
subplot(3,1,1);
plot(tt, true_states(1,:),'b-', tt, est_states(1,:),'r--');
legend('true omega','est omega'); ylabel('omega');
subplot(3,1,2);
plot(tt, true_states(2,:),'b-', tt, est_states(2,:),'r--');
legend('true a','est a'); ylabel('a');
subplot(3,1,3);
plot(tt, true_states(3,:),'b-', tt, est_states(3,:),'r--');
legend('true b','est b'); ylabel('b'); xlabel('time (s)');


function dx = f_cont(x, t)
    omega = x(1); a = x(2); b = x(3);
    dx = [-a*omega + 1.5*sin(t) + b; 0; 0];
end

function A = A_cont(x, t)
    omega = x(1); a = x(2);
    A = [-a, -omega, 1; 0,0,0; 0,0,0];
end

function [x_pred, P_pred] = ekf_predict_matlab(x, P, Ts, Qc, t)
    x_pred = x + Ts * f_cont(x, t);
    A = eye(3) + Ts * A_cont(x, t);
    P_pred = A * P * A' + Ts * Qc;
end

function [x_upd, P_upd] = ekf_update_matlab(x_pred, P_pred, y, R)
    C = [1 0 0];
    S = C * P_pred * C' + R;
    K = (P_pred * C') / S;
    x_upd = x_pred + K * (y - C * x_pred);
    P_upd = (eye(3) - K * C) * P_pred;
end
