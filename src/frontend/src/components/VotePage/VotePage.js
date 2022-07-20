import * as React from "react";

import {
  Button,
  Card,
  CardActions,
  CardContent,
  CardMedia,
  Grid,
  Typography,
} from "@material-ui/core";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import cat from "../../images/cat.jpeg";
import dog from "../../images/dog.jpeg";
import { faThumbsUp } from "@fortawesome/free-solid-svg-icons";
import { map } from "lodash";

const images = [
  {
    url: cat,
    title: "Cat",
  },
  {
    url: dog,
    title: "Dog",
  },
];

function VotePage() {
  return (
    <Grid container justifyContent="center" direction="row" spacing={2}>
      {map(images, (image) => (
        <Grid item>
          <Card>
            <CardMedia
              component="img"
              height={600}
              image={`${image.url}`}
              alt={image.title}
            />
            <CardContent>
              <Typography variant="h5">{image.title}</Typography>
            </CardContent>
            <CardActions>
              <Button
                size="small"
                variant="outlined"
                startIcon={<FontAwesomeIcon icon={faThumbsUp} />}
              >
                Vote
              </Button>
            </CardActions>
          </Card>
        </Grid>
      ))}
    </Grid>
  );
}

export default VotePage;
