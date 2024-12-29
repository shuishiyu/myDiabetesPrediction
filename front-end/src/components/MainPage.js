import React, { useState, useEffect } from "react";
import Stack from "@mui/material/Stack";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import SearchBar from "./SearchBar";

export default function MainPage() {
  const [data, setData] = useState([{}]);
  useEffect(() => {
    fetch("/patients")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  });
  return (
    <main>
      {/* Hero unit */}
      <Box
        sx={{
          bgcolor: "background.paper",
          pt: 3,
          pb: 3,
        }}
      >
        <Container maxWidth="sm">
          <Typography
            component="h5"
            variant="h5"
            align="center"
            color="text.primary"
            gutterBottom
          >
            Search and Predict!
          </Typography>
          <Typography
            variant="subtitle1"
            align="center"
            color="text.secondary"
            paragraph
          >
            Search patients from the FHIR Database, then select the patient whom
            you would like to predict the risk of having diabetes for.
          </Typography>

          <Stack direction="row" spacing={2} justifyContent="center">
            <SearchBar placeholder={"Search by patient ID"} />
          </Stack>
        </Container>
      </Box>
      <Container sx={{ py: 8 }} maxWidth="md"></Container>
    </main>
  );
}
