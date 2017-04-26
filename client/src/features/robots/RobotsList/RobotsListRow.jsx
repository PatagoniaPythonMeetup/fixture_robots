import React from "react";
import {
  Table,
  Header,
  Image,
} from "semantic-ui-react";

const RobotsListRow = ({robot={}}) => {
  const {
    index = 0,
    nombre = "",
    escuela = "",
    score = [0, 0, 0, 0, 0, 0, 0, 0]
  } = robot;

  return (
    <Table.Row>
      <Table.Cell>{index}</Table.Cell>
      <Table.Cell>
        <Header as='h4' image>
          <Image src='/escudos/escudo2.png' shape='rounded' size='mini' />
          <Header.Content>
            {nombre}
            <Header.Subheader>{escuela}</Header.Subheader>
          </Header.Content>
        </Header>
      </Table.Cell>
      <Table.Cell>{score[0]}</Table.Cell>
      <Table.Cell>{score[1]}</Table.Cell>
      <Table.Cell>{score[2]}</Table.Cell>
      <Table.Cell>{score[3]}</Table.Cell>
      <Table.Cell>{score[4]}</Table.Cell>
      <Table.Cell>{score[5]}</Table.Cell>
      <Table.Cell>{score[6]}</Table.Cell>
      <Table.Cell><strong>{score[7]}</strong></Table.Cell>
    </Table.Row>
  );
}

export default RobotsListRow;
