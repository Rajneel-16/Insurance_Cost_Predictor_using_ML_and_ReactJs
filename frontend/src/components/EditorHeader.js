import React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import { useTheme, useMediaQuery } from '@mui/material';
import { green } from '@mui/material/colors';

const EditorHeader = () => {
    const theme = useTheme();
    const isMd = useMediaQuery(
        theme.breakpoints.up('md'),
        { defaultMatches: true }
    );
    
    return (
        < >
            <Typography
                variant='h2'
                color={theme.palette.text.primary}
            >
                Personal Details Form
            </Typography>
            <Box paddingTop={2}>
                <Typography
                    variant='h5'
                    color={theme.palette.text.secondary}
                >
                    Fill your
                    {' '}
                    <span style={{ color: green[600] }}>
                    details
                    </span>
                    {' '}
                     to get the Insurance Cost
                </Typography>
            </Box>
        </>
    );
};

export default EditorHeader;