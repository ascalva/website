FROM 054942746160.dkr.ecr.us-west-2.amazonaws.com/personal-website-base:latest

COPY ./requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt
RUN pip3 install gunicorn

## Environment Setup ##
EXPOSE 5000

# Make new user owner of project directory.
RUN mkdir /app
WORKDIR   /app
COPY .    /app

RUN chown -R lit_user:lit_user /app

# Switch to non-root user after setup and installations.
USER lit_user

CMD ["gunicorn", "-c", "gunicorn.py", "flask_app:app"]
