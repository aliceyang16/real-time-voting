import { commitMutation } from "react-relay";
import graphql from "babel-plugin-relay/macro";

const mutation = graphql`
  mutation BallotMutation($dogVote: Boolean, $catVote: Boolean) {
    insertBallots(dogVote: $dogVote, catVote: $catVote) {
      ok
    }
  }
`;

function commit(environment, dashboardId, newDashboardName, callback, t) {
  const variables = { dashboardId, newDashboardName };
  return commitMutation(environment, {
    mutation,
    variables,
    onCompleted: (response) => {
      callback && callback(response?.duplicateDashboard);
    },
    onError: (error) => {
      console.log(error);
    },
  });
}

export default { commit };
