import React from "react";
import { Table } from "semantic-ui-react";

const RobotsListHeader = () => (
  <Table.Header>
    <Table.Row>
      <Table.HeaderCell width={1}>#</Table.HeaderCell>
      <Table.HeaderCell width={5}>Equipo</Table.HeaderCell>
      <Table.HeaderCell width={2}>Jugados</Table.HeaderCell>
      <Table.HeaderCell width={2}>Triunfos</Table.HeaderCell>
      <Table.HeaderCell width={2}>Empates</Table.HeaderCell>
      <Table.HeaderCell width={2}>Derrotas</Table.HeaderCell>
      <Table.HeaderCell width={2}>Favor</Table.HeaderCell>
      <Table.HeaderCell width={2}>Contra</Table.HeaderCell>
      <Table.HeaderCell width={2}>Diferencia</Table.HeaderCell>
      <Table.HeaderCell width={2}>Puntos</Table.HeaderCell>
    </Table.Row>
  </Table.Header>
);

export default RobotsListHeader;