import React, { Component } from 'react';
import { Header, Image, Table } from 'semantic-ui-react'

class PosicionesPage extends Component {
  render() {
    return (
    <Table basic='very' celled collapsing>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell>#</Table.HeaderCell>
          <Table.HeaderCell>Equipo</Table.HeaderCell>
          <Table.HeaderCell>Jugados</Table.HeaderCell>
          <Table.HeaderCell>Triunfos</Table.HeaderCell>
          <Table.HeaderCell>Empates</Table.HeaderCell>
          <Table.HeaderCell>Derrotas</Table.HeaderCell>
          <Table.HeaderCell>A favor</Table.HeaderCell>
          <Table.HeaderCell>En contra</Table.HeaderCell>
          <Table.HeaderCell>Diferencia</Table.HeaderCell>
          <Table.HeaderCell>Puntos</Table.HeaderCell>
        </Table.Row>
      </Table.Header>

      <Table.Body>
        <Table.Row>
          <Table.Cell>1</Table.Cell>
          <Table.Cell>
            <Header as='h4' image>
              <Image src='/static/escudos/escudo1.png' shape='rounded' size='mini' />
              <Header.Content>
                Sony
                <Header.Subheader>R&H Mecanicos</Header.Subheader>
              </Header.Content>
            </Header>
          </Table.Cell>
          <Table.Cell>1</Table.Cell>
          <Table.Cell>1</Table.Cell>
          <Table.Cell>0</Table.Cell>
          <Table.Cell>0</Table.Cell>
          <Table.Cell>2</Table.Cell>
          <Table.Cell>1</Table.Cell>
          <Table.Cell>1</Table.Cell>
          <Table.Cell><strong>3</strong></Table.Cell>
        </Table.Row>
        <Table.Row>
          <Table.Cell>2</Table.Cell>
          <Table.Cell>
            <Header as='h4' image>
              <Image src='/static/escudos/escudo2.png' shape='rounded' size='mini' />
              <Header.Content>
                Ultron
                <Header.Subheader>Los Avengers</Header.Subheader>
              </Header.Content>
            </Header>
          </Table.Cell>
          <Table.Cell>1</Table.Cell>
          <Table.Cell>0</Table.Cell>
          <Table.Cell>0</Table.Cell>
          <Table.Cell>1</Table.Cell>
          <Table.Cell>1</Table.Cell>
          <Table.Cell>2</Table.Cell>
          <Table.Cell>-1</Table.Cell>
          <Table.Cell><strong>0</strong></Table.Cell>
        </Table.Row>
        <Table.Row>
          <Table.Cell>3</Table.Cell>
          <Table.Cell>
            <Header as='h4' image>
              <Image src='/static/escudos/escudo3.png' shape='rounded' size='mini' />
              <Header.Content>
                Robocop
                <Header.Subheader>O.C.P.</Header.Subheader>
              </Header.Content>
            </Header>
          </Table.Cell>
          <Table.Cell>1</Table.Cell>
          <Table.Cell>0</Table.Cell>
          <Table.Cell>0</Table.Cell>
          <Table.Cell>1</Table.Cell>
          <Table.Cell>1</Table.Cell>
          <Table.Cell>2</Table.Cell>
          <Table.Cell>-1</Table.Cell>
          <Table.Cell><strong>0</strong></Table.Cell>
        </Table.Row>
      </Table.Body>
    </Table>
  );
  }
}

export default PosicionesPage;