import React, {Component} from "react";
import {Table} from "semantic-ui-react";

import RobotsListHeader from "./RobotsListHeader";
import RobotsListRow from "./RobotsListRow";

export class RobotsList extends Component {
  render() {
    const {robots = []} = this.props;

    const robotRows = robots.map(robot => (
      <RobotsListRow robot={robot}/>
    ));

    return (
      <Table basic='very' celled collapsing>
        <RobotsListHeader />
        <Table.Body>
          {robotRows}
        </Table.Body>
      </Table>
    )
  }
}

export default RobotsList;
