import Relay from 'react-relay';

export default class extends Relay.Route {
  static queries = {
    fixture: (Component) => Relay.QL`query FixtureQuery { fixture { ${Component.getFragment('fixture')} } }`,
  };
  static routeName = 'AppRoute';
}