import FWCore.ParameterSet.Config as cms

v0VertexTrackProducer = cms.EDProducer('V0VertexTrackProducer',
  vertexCompositeCandidates = cms.InputTag('generalV0Candidates', 'Kshort'),
  mightGet = cms.optional.untracked.vstring
)
