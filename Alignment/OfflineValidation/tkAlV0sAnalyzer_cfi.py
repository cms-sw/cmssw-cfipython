import FWCore.ParameterSet.Config as cms

tkAlV0sAnalyzer = cms.EDAnalyzer('TkAlV0sAnalyzer',
  vertexCompositeCandidates = cms.InputTag('generalV0Candidates', 'Kshort'),
  tracks = cms.untracked.InputTag('ALCARECOTkAlKShortTracks'),
  mightGet = cms.optional.untracked.vstring
)
