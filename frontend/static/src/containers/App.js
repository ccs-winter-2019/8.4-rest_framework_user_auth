import React, { Component } from 'react';
import RideForm from '../components/RideForm';


class App extends Component {

  createRide = (ride) => {
    const conf = {
      method: "post",
      body: JSON.stringify(ride),
      headers: new Headers({"Content-Type": "application/json"})
    };

    fetch(`/api/rides/`, conf).then((response) => {
      if (response.status !== 201) {
        // There was an error so roll back the state
        // var jobs = this.state.jobs;
        // jobs.pop();
        // return this.setState({placeholder: "Something went wrong", jobs: jobs});

        // return this.setState({placeholder: "Something went wrong"});
      }

      return response.json();
    }).then((ride) => {
      // redirect

      window.location = 'http://localhost:8000/rides/';
    });
  }

  render() {
    return (
      <div>
        <RideForm createRide={this.createRide} />
      </div>
    );
  }
}

export default App;
