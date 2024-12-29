import React from "react";
import SearchIcon from "@mui/icons-material/Search";
import { TextField } from "@mui/material";
import IconButton from "@mui/material/IconButton";

export default function SearchBar({ setSearchQuery, placeholder }) {
  return (
    <form>
      <TextField
        id="search-bar"
        className="text"
        //   onInput={(e) => {
        //     setSearchQuery(e.target.value);
        //   }}
        label={placeholder}
        variant="outlined"
        placeholder="Search..."
        size="small"
      />
      <IconButton type="submit" aria-label="search">
        <SearchIcon />
      </IconButton>
    </form>
  );
}
