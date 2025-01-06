import React, { useEffect, useState } from 'react'
import 'react-toastify/dist/ReactToastify.css';
import axios from 'axios'
import Create from './Create';



function Create_Image() {
    const [data, setdata] = useState([])
    const [Update, setUpdate] = useState({})
    useEffect(() => {
        axios.get('http://127.0.0.1:8000/create/')
            .then((response) => {
                setdata(response.data)
            })
            .catch((err) => {
                console.log('Eorr is come');
            })
    }, [data]);


    const updateDetails = (id) => {
        console.log(id);
        fetch(`http://127.0.0.1:8000/detail/${id}/`)
            .then((response) => response.json())
            .then((res) => {
                setUpdate(res);
                console.log("Hello", res);
            })
            .catch((error) => console.error('Error:', error));
    }

    const handleInputEvent = (event, fieldName) => {
        const value = event.target.value;
        setUpdate((pre) => ({
            ...pre, [fieldName]: value,
        }))
    }


    const handleSubmit = async (e, id) => {
        e.preventDefault();
        const requestdata = {
            id: Update.id,
            Name: Update.Name,
            Prep_time: Update.Prep_time,
            Description: Update.Description,

        };
        console.log('Update data', requestdata);
        const response = await axios.put(`http://127.0.0.1:8000/update/${id}/`, requestdata, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        console.log(response);
    }

    const deleteItem = (id) => {
        fetch(`http://127.0.0.1:8000/delete/${id}/`, { method: 'DELETE' })
            .then(() => {
                console.log('DELETED');
            })
            .catch((error) => {
                console.error('Error deleting the item:', error);
            });
    };

    const [currentpage, setcurrentpage] = useState(1);
    const [searchItem, setsearchItem] = useState('')
    const flterData=data.filter((item)=>
        item.Name.toLowerCase().includes(searchItem.toLowerCase())
    )
    const recordPerPage =3
    const lastIndex=currentpage * recordPerPage
    const firstPage=lastIndex - recordPerPage
    const record=flterData.slice(firstPage,lastIndex)
    const npage=Math.ceil(data.length / recordPerPage)
    const numbers = Array.from({ length: npage }, (_, i) => i + 1);

function prevpage(){
    if(currentpage!==firstPage){
        setcurrentpage(currentpage-1)
    }
}
function nextPage(){
    if(currentpage!==lastIndex){
        setcurrentpage(currentpage+1)
    }
}
function changepage(n){
    
        setcurrentpage(n)
    
}



    return (
        <>
            <div className="container p-5">
                <div className="row">
                    <input type="search" className='form-control' placeholder='Search' value={searchItem} onChange={(e)=>{
                        setsearchItem(e.target.value)
                        setcurrentpage(1)
                    }}/>
                </div>
                <table class="table">
                    <thead>
                        <tr>
                            <th scope="col">ID</th>
                            <th scope="col">Name</th>
                            <th scope="col">Prep_time</th>
                            <th scope="col">Description</th>
                            <th scope="col" colSpan={2}>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            record.map((item) => {
                                return (
                                    <tr key={item.id}>
                                        <th scope="row">{item.id}</th>
                                        <td><img src={item.Recipe_img} alt="Recipe" style={{ width: "100px", height: "auto" }} />
                                        {item.Name}</td>
                                        <td>{item.Prep_time}</td>
                                        <td>{item.Description}</td>
                                        <td><button className='btn btn-success' data-bs-toggle="modal" onClick={() => updateDetails(item.id)} data-bs-target="#exampleModal">Update</button></td>
                                        <td><button className='btn btn-danger' data-bs-toggle="modal" onClick={() => updateDetails(item.id)} data-bs-target="#exampleModaldelete">Delete</button></td>
                                    </tr>
                                )
                            })
                        }
                    </tbody>
                </table>
                <nav aria-label="Pagination Navigation">
            <ul className="pagination">
                <li className="page-item ">
                    <a className="page-link"  tabIndex="-1" onClick={prevpage}>Previous</a>
                </li>
                {
    numbers.map((n, i) => {
        return (
            <li className={`page-item ${currentpage === n ? 'active' : ''}`} key={i}>
                <a className="page-link" onClick={() => changepage(n)}>
                    {n}
                </a>
            </li>
        );
    })
}

                 <li className="page-item">
                    <a className="page-link"  onClick={nextPage}>Next</a>
                </li>
            
            </ul>
        </nav>
            </div>

            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel">Update </h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            {Update.id}-{Update.Name}
                            <div className="container mt-4">
                                <form action="" onSubmit={(e) => handleSubmit(e, Update.id)}>
                                    <div className='form-group mb-4'>
                                        <label htmlFor="">Name</label>
                                        <input type="text" name='Name' placeholder='Name' className='form-control' value={Update.Name} onChange={(event) => handleInputEvent(event, 'Name')} />
                                    </div>
                                    <div className='form-group mb-4'>
                                        <label htmlFor="">Prep_time</label>
                                        <input type="time" name='Prep_time' placeholder='Prep_time' className='form-control' value={Update.Prep_time} onChange={(event) => handleInputEvent(event, 'Prep_time')} />
                                    </div>
                                    <div className='form-group mb-4'>
                                        <label htmlFor="">Description</label>
                                        <input type="text" name='Description' placeholder='Description' className='form-control' value={Update.Description} onChange={(event) => handleInputEvent(event, 'Description')} />
                                    </div>
                                    <div className='form-group mb-4'>
                                        <button type="submit" class="btn btn-primary" >Save changes</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>

                        </div>
                    </div>
                </div>
            </div>


            <div class="modal fade" id="exampleModaldelete" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel"> Delete Modal</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <h4>Do want to delete {Update.Name}</h4>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-danger" data-bs-dismiss="modal" onClick={() => deleteItem(Update.id)}>Confirm</button>

                        </div>
                    </div>
                </div>
            </div>
            <Create />

        </>
    )
}

export default Create_Image
