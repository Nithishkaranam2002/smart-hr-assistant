# Use Nginx base image
FROM nginx:alpine

# Remove default Nginx page
RUN rm -rf /usr/share/nginx/html/*

# Copy frontend files
COPY ./frontend /usr/share/nginx/html

# Expose port
EXPOSE 80
