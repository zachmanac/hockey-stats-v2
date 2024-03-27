import { useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import TextField from '@mui/material/TextField';

const columns = [
  { field: 'name', headerName: 'Full Name', width: 160 },
  { field: 'position', headerName: 'Position', width: 130 },
  { field: 'games_played', headerName: 'Games Played', type: 'number', width: 150 },
  { field: 'goals', headerName: 'Goals', type: 'number', width: 100 },
  { field: 'assists', headerName: 'Assists', type: 'number', width: 100 },
  { field: 'points', headerName: 'Points', type: 'number', width: 100 },
];

export default function DataTable({ players }) {
  const [nameFilter, setNameFilter] = useState('');

  const displayedRows = players.filter((player) => 
  `${player.name}`.toLowerCase().includes(nameFilter.toLowerCase())
  ).map((player) => ({
    ...player,
    id: player.player_id,
  }));

  return (
    <div style={{ height: 630, width: '100%' }}>
      <TextField
        id="outlined-basic"
        label="Player Name"
        variant="outlined"
        value={nameFilter}
        onChange={(e) => {setNameFilter(e.target.value)}}
      />
        <DataGrid
          rows={displayedRows}
          columns={columns}
          initialState={{
            pagination: {
              paginationModel: { page: 0, pageSize: 10 },
            },
          }}
          pageSizeOptions={[10, 25]}
          checkboxSelection
        />
    </div>
  );
};