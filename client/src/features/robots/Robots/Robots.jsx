import React, {Component} from "react";

import {
    Grid,
    Segment,
    Header,
} from "semantic-ui-react";

import RobotsList from "../RobotsList";
import RobotDetails from "../RobotDetails";


export default class Pilots extends Component {
    render() {
        return (
            <Segment>
                <Grid>
                    <Grid.Column width={10}>
                        <Header as="h3">Robots List</Header>
                        <RobotsList />
                    </Grid.Column>
                    <Grid.Column width={6}>
                        <Header as="h3">Robot Details</Header>
                        <Segment >
                            <RobotDetails />
                        </Segment>
                    </Grid.Column>
                </Grid>
            </Segment>
        );
    }
}