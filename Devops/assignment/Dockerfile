# ---------------Stage 1: Build ----------------

FROM maven:3.9.6-eclipse-temurin-17 AS build
LABEL stage="builder"
WORKDIR /app

COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

# ---------------- Stage 2: Run ----------

FROM eclipse-temurin:17-jre
LABEL authors="USER 10"

WORKDIR /app
COPY --from=build /app/target/*.jar app.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
