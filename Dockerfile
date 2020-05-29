FROM continuumio/miniconda
COPY environment.yml /app/environment.yml
RUN conda env update -f /app/environment.yml
COPY . /app
CMD ["bash", "-c", "source activate SPGFoodSafety  && python /app/main.py"]
