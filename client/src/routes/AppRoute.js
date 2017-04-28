import Relay from 'react-relay';

export default class extends Relay.Route {
  static queries = {
    robots: () => Relay.QL`
      query {
        robots
      }
    `,
  };
  static routeName = 'AppRoute';
}