import FWCore.ParameterSet.Config as cms

VertexCompositeCandidateCollectionSelector = cms.EDProducer('VertexCompositeCandidateCollectionSelector',
  v0 = cms.required.InputTag,
  beamSpot = cms.required.InputTag,
  primaryVertex = cms.required.InputTag,
  pvNDOF = cms.required.int32,
  lxyCUT = cms.double(16),
  lxyWRTbsCUT = cms.double(0),
  debug = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
