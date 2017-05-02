import React from "react";

import {Image,Icon,Card,Grid} from "semantic-ui-react";

const Encuentro = ({encuentro={}}) => {
  const {
    numero = '',
  } = encuentro;

  return (
    <Grid key={numero} columns='equal'>
      <Grid.Row>
        <Grid.Column>
          <Card>
            <Image src='/escudos/escudo1.png' />
            <Card.Content>
            <Card.Header>
                Matthew
            </Card.Header>
            <Card.Meta>
                <span className='date'>
                Joined in 2015
                </span>
            </Card.Meta>
            <Card.Description>
                Matthew is a musician living in Nashville.
            </Card.Description>
            </Card.Content>
            <Card.Content extra>
            <a>
                <Icon name='user' />
                22 Friends
            </a>
            </Card.Content>
          </Card>
        </Grid.Column>
        <Grid.Column>
          <Card>
            <Image src='/escudos/escudo2.png' />
            <Card.Content>
            <Card.Header>
                Matthew
            </Card.Header>
            <Card.Meta>
                <span className='date'>
                Joined in 2015
                </span>
            </Card.Meta>
            <Card.Description>
                Matthew is a musician living in Nashville.
            </Card.Description>
            </Card.Content>
            <Card.Content extra>
            <a>
                <Icon name='user' />
                22 Friends
            </a>
            </Card.Content>
          </Card>
        </Grid.Column>
      </Grid.Row>
    </Grid>
  );
}

export default Encuentro;