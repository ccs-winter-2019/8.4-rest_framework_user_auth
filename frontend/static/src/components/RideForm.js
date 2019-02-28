import React, {Component} from "react";
import PropTypes from "prop-types";


class RideForm extends Component {
  state = {
    participant_count: '',
    duration: "",
    ride_date: "",
    total: 20
  };

  base_price = 20;

  handleChange = e => {
    this.setState({[e.target.name]: e.target.value});
  };

  handleDurationChange = (e) => {
    var duration = e.target.value;
    var newTotal = this.base_price * parseInt(duration || 30)/30 * parseInt(this.state.participant_count || 1);

    this.setState({'duration': e.target.value, total: newTotal});
  };

  handleParticipantChange = (e) => {
    var participantCount = e.target.value;
    var newTotal = this.base_price * parseInt(this.state.duration || 30)/30 * parseInt(participantCount || 1);

    this.setState({'participant_count': e.target.value, total: newTotal});
  };

  handleSubmit = e => {
    e.preventDefault();

    const {participant_count, duration, ride_date} = this.state;
    const ride = {participant_count, duration, ride_date};

    this.props.createRide(ride);
    this.setState({
      participant_count: '',
      duration: '',
      ride_date: '',
      total: this.base_price
    });
  };

  render() {
    const {participant_count, duration, ride_date} = this.state;

    return (
      <div className="column">
        <h1>Total: ${this.state.total}</h1>


        <form onSubmit={this.handleSubmit}>

          <div className="field">
            <label className="label">participant_count</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="participant_count"
                onChange={this.handleParticipantChange}
                value={participant_count}
                required
              />
            </div>
          </div>

          <div className="field">
            <label className="label">duration</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="duration"
                onChange={this.handleDurationChange}
                value={duration}
                required
              />
            </div>
          </div>

          <div className="field">
            <label className="label">ride_date</label>
            <div className="control">
              <input
                className="input"
                type="datetime-local"
                name="ride_date"
                onChange={this.handleChange}
                value={ride_date}
                required
              />
            </div>
          </div>

          <div className="control">
            <button type="submit" className="button is-info">
              Send message
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default RideForm;