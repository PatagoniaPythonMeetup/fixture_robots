import React, {Component} from "react";

import {
  Image,
  Icon,
  Card,
  Grid
} from "semantic-ui-react";

const Encuentro = ({encuentro={}}) => {
  const {
    
  } = encuentro;

  return (
    <Grid columns='equal'>
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