#ifndef PID_H
#define PID_H

class Pid
{
public:
    Pid() = default;
    Pid(double const kp,
        double const ki,
        double const kd,
        double const minOutput,
        double const maxOutput,
        double const minIntegral,
        double const maxIntegral);

    void setTarget(double const target) { target_ = target;};

    /// \brief Perform one update loop of the pid for time t.
    /// \param[in] input : double - new input value (measurement)
    /// \param[in] delta_time : double - time elapsed since last loop
    double update(double const input, double const delta_time);

    /// \brief Rest current values but not parameters.
    void reset();

    void setKp(double const kp) { kp_ = kp; };
    void setKi(double const ki) { ki_ = ki; };
    void setKd(double const kd) { kd_ = kd; };
    void setMin(double const min) { min_ = min; };
    void setMax(double const max) { max_ = max; };
    void setMinIntegral(double const min) { minIntegral_ = min; error_integral_ = 0.0; };
    void setMaxIntegral(double const max) { maxIntegral_ = max; error_integral_ = 0.0; };

    void print();

private:
    double kp_{0.0};
    double ki_{0.0};
    double kd_{0.0};
    double error_integral_{0.0};
    double previous_error_{0.0};
    double minIntegral_{0.0};
    double maxIntegral_{0.0};
    double min_{0.0};
    double max_{0.0};
    double target_{0.0};
    double output_{0.0};
};

#endif 
