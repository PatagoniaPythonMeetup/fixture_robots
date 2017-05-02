import React from "react";
import Relay from 'react-relay';

class Robot extends React.Component {
  render() {
    var {key, nombre} = this.props.robot;
    return (
      <li key={key}>
        <strong>{key}</strong> {nombre}
      </li>
    );
  }
}

Robot = Relay.createContainer(Robot, {
  fragments: {
    robot: () => Relay.QL`
      fragment on Robot {
        key,
        nombre,
        escuela,
        encargado,
        score
      }
    `,
  },
});

export default Robot;