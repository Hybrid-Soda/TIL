class MovieReview {
    String title;
    String review;
}

public class MovieReviewMain {
    public static void main(String[] args) {
        MovieReview inception = new MovieReview();
        inception.title = "인셉션";
        inception.review = "인생은 무한 루프";

        MovieReview aboutTime = new MovieReview();
        aboutTime.title = "어바웃 타임";
        aboutTime.review = "인생 시간 영화!";

        MovieReview[] reviews = {inception, aboutTime};

        for (int i = 0; i < 2; i++) {
            System.out.println("영화 제목: " + reviews[i].title + ", 리뷰: " + reviews[i].review);
        }

        for (MovieReview review : reviews) {
            System.out.println("영화 제목: " + review.title + ", 리뷰: " + review.review);
        }
    }
}
