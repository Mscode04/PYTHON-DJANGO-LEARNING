import axios from 'axios';
import React, { useState } from 'react';

function Create() {
    const [formdata, setformdata] = useState({
        Name: '',
        Prep_time: '',
        Description: '',
        Recipe_img: null,
    });

    const handleInputEvent = (event) => {
        const { name, value } = event.target;
        setformdata({ ...formdata, [name]: value });
    };

    const handleInputEventImage = (e) => {
        const file = e.target.files[0];
        setformdata({ ...formdata, Recipe_img: file });
    };

    const handleSubmit = async (event) => {
        event.preventDefault(); // Prevent the form from refreshing the page

        const formDataToSubmit = new FormData();
        formDataToSubmit.append('Name', formdata.Name);
        formDataToSubmit.append('Prep_time', formdata.Prep_time);
        formDataToSubmit.append('Description', formdata.Description);
        formDataToSubmit.append('Recipe_img', formdata.Recipe_img);

        try {
            const response = await axios.post('http://127.0.0.1:8000/create/', formDataToSubmit, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            console.log('Item created successfully:', response.data);
        } catch (error) {
            console.error('Create item error:', error);
        }
    };

    return (
        <div className="container mt-4">
            <h3>Create New Item</h3>
            <form onSubmit={handleSubmit}>
                <div className="form-group mb-4">
                    <label htmlFor="">Name</label>
                    <input
                        type="text"
                        name="Name"
                        placeholder="Name"
                        className="form-control"
                        onChange={handleInputEvent}
                    />
                </div>
                <div className="form-group mb-4">
                    <label htmlFor="">Prep_time</label>
                    <input
                        type="time"
                        name="Prep_time"
                        placeholder="Prep_time"
                        className="form-control"
                        onChange={handleInputEvent}
                    />
                </div>
                <div className="form-group mb-4">
                    <label htmlFor="">Description</label>
                    <input
                        type="text"
                        name="Description"
                        placeholder="Description"
                        className="form-control"
                        onChange={handleInputEvent}
                    />
                </div>
                <div className="form-group mb-4">
                    <label htmlFor="">Image</label>
                    <input
                        type="file"
                        name="Recipe_img"
                        accept="image/*"
                        className="form-control"
                        onChange={handleInputEventImage}
                    />
                </div>
                <div className="form-group mb-4">
                    <button type="submit" className="btn btn-primary">
                        Add New
                    </button>
                </div>
            </form>
        </div>
    );
}

export default Create;
