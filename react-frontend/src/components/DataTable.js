import { useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import TextField from '@mui/material/TextField';
// import data from './mockData';

const columns = [
  { field: 'firstName', headerName: 'First name', width: 130 },
  { field: 'lastName', headerName: 'Last name', width: 130 },
  {
    field: 'age',
    headerName: 'Age',
    type: 'number',
    width: 90,
  },
  {
    field: 'fullName',
    headerName: 'Full name',
    description: 'This column has a value getter and is not sortable.',
    sortable: false,
    width: 160,
    valueGetter: (value, row) => `${row.firstName || ''} ${row.lastName || ''}`,
  },
  {
    field: 'gamesPlayed',
    headerName: 'Games Played',
    type: 'number',
    sortable: false,
    width: 150
  },
  {
    field: 'goals',
    headerName: 'Goals',
    type: 'number',
    width: 80
  },
  {
    field: 'assists',
    headerName: 'Assists',
    type: 'number',
    width: 80
  },
  {
    field: 'points',
    headerName: 'Points',
    type: 'number',
    valueGetter: (value, row) => ((row.goals || 0 )+ (row.assists || 0)),
    width: 80
  },
];

const rows = [
  { id: 1, lastName: 'Snow', firstName: 'Jon', age: 35, gamesPlayed: 82, goals: 45, assists: 20, points: 65 },
  { id: 2, lastName: 'Lannister', firstName: 'Cersei', age: 42, gamesPlayed: 82, goals: 12, assists: 46, points: 63 },
  { id: 3, lastName: 'Lannister', firstName: 'Jaime', age: 45, gamesPlayed: 59, goals: 32, assists: 21, points: 89 },
  { id: 4, lastName: 'Stark', firstName: 'Arya', age: 16, gamesPlayed: 78, goals: 11, assists: 25, points: 36 },
  { id: 5, lastName: 'Targaryen', firstName: 'Daenerys', age: null, gamesPlayed: 81, goals: 24, assists: 27, points: 52 },
  { id: 6, lastName: 'Melisandre', firstName: null, age: 150, gamesPlayed: 76, goals: 35, assists: 47, points: 72 },
  { id: 7, lastName: 'Clifford', firstName: 'Ferrara', age: 44, gamesPlayed: 82, goals: 38, assists: 27, points: 69 },
  { id: 8, lastName: 'Frances', firstName: 'Rossini', age: 36, gamesPlayed: 76, goals: 45, assists: 20, points: 65 },
  { id: 9, lastName: 'Roxie', firstName: 'Harvey', age: 65, gamesPlayed: 80, goals: 52, assists: 21, points: 76 },
];

export default function DataTable() {
  const [nameFilter, setNameFilter] = useState('');

  const displayedRows = function (rows) {
    return rows.filter((row) => {
      if(`${row.firstName || ''} ${row.lastName || ''}`.toLowerCase().includes(nameFilter)) {
        return true;
      } else {
        return false;
      }
    }
    )
  }

  return (
    <div style={{ height: 400, width: '100%' }}>
      <TextField id="outlined-basic" label="Player Name" variant="outlined" value={nameFilter}
      onChange={(e) => {setNameFilter(e.target.value)}}
      />
      <DataGrid
        rows={displayedRows(rows)}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: { page: 0, pageSize: 5 },
          },
        }}
        pageSizeOptions={[5, 10]}
        checkboxSelection
      />
    </div>
  );
}