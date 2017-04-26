import React from "react";
import { Table } from "semantic-ui-react";

const EncuentroHeader = () => (
  <Table.Header>
    <Table.Row>
      <Table.HeaderCell width={5}>Local</Table.HeaderCell>
      <Table.HeaderCell width={2}></Table.HeaderCell>
      <Table.HeaderCell width={2}></Table.HeaderCell>
      <Table.HeaderCell width={5}>Visitante</Table.HeaderCell>
    </Table.Row>
  </Table.Header>
);

export default EncuentroHeader;