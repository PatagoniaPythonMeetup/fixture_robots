import React, {Component} from "react";
import {Table} from "semantic-ui-react";

import EncuentroHeader from "./EncuentroHeader";
import EncuentroRow from "./EncuentroRow";

export class Ronda extends Component {
  render() {
    const {ronda = []} = this.props;

    const encuentroRows = ronda.ecuentros.map(encuentro => (
      <EncuentroRow encuentro={encuentro}/>
    ));

    return (
      <Table basic='very' celled collapsing>
        <EncuentroHeader />
        <Table.Body>
          {encuentroRows}
        </Table.Body>
      </Table>
    )
  }
}

export default Ronda;
