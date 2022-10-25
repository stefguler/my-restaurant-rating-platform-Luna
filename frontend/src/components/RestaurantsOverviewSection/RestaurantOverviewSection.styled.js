import styled from "styled-components"

export const RestaurantOverviewContainer = styled.div`
width: 100%;
`;

export const SearchBarContainer = styled.div`

  select {
    cursor: pointer;
    width: 15%;
    color: #D8D8D8;
    border: 1px solid #EBEBEB;
    font-size: 20px;
    /* padding: 1rem; */

      option {
        cursor: pointer;
    }

  }
`;

export const SearchInput = styled.input`
  width: 85%;
  color: #D8D8D8;
  border: 1px solid #EBEBEB;
  font-size: 20px;
  font-weight: 700;
  padding: 1rem;

  :focus {
    outline: none;
  }

`;

export const RestaurantListFilterContainer = styled.div`
  display: flex;
  width: 100%;
  margin-top: 1rem;
  justify-content: center;

 

`

export const ListContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 15%;
  padding-bottom: 1rem;
  border-bottom: #D8D8D8 solid 2px;  

  cursor: pointer;

  :hover {
    border-color: #E47D31;
  }

  .active {
    border-radius: red;
  }  
`

export const RestaurantListFilter = styled.span`
  text-transform: uppercase;
  font-size: 20px;
  font-weight: 700;
`

