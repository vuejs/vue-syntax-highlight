<page-query>
  query Article($id: String!) {
    contentfulCaseStudy(id: $id) {
      id
      title
      slug
      content(html: true)
    }
  }
</page-query>
