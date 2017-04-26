import React from "react";
import {
  Table,
  Header,
  Image,
} from "semantic-ui-react";

const EncuentroRow = ({encuentro={}}) => {
  const {
    robot_1 = "",
    robot_2 = ""
  } = encuentro;

  return (
    <Table.Row>
      <Table.Cell>{robot_1}</Table.Cell>
      <Table.Cell>0</Table.Cell>
      <Table.Cell>0</Table.Cell>
      <Table.Cell>{robot_2}</Table.Cell>
    </Table.Row>
  );
}

export default EncuentroRow;
