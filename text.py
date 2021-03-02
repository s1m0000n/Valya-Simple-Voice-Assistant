from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    Doc
)


class TextProcessor:
    def __init__(self):
        self.segmenter = Segmenter()
        self.morph_vocab = MorphVocab()
        self.emb = NewsEmbedding()
        self.morph_tagger = NewsMorphTagger(self.emb)
        self.ner_tagger = NewsNERTagger(self.emb)
        self.syntax_parser = NewsSyntaxParser(self.emb)

    def __call__(self, text):
        doc = Doc(text)
        doc.segment(self.segmenter)
        doc.tag_morph(self.morph_tagger)
        for token in doc.tokens:
            token.lemmatize(self.morph_vocab)
        doc.parse_syntax(self.syntax_parser)
        doc.tag_ner(self.ner_tagger)
        for span in doc.spans:
            span.normalize(self.morph_vocab)
        return doc
