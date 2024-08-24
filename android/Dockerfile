FROM budtmo/docker-android:emulator_11.0

USER root

RUN echo 'root:x:0:0:root:/root:/bin/bash' >> /etc/passwd

COPY run.sh /run.sh

# Add this line to set execute permissions
RUN chmod +x /run.sh

USER androidusr

ENTRYPOINT ["/bin/bash", "-c"]
CMD ["/run.sh"]
