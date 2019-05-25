import FWCore.ParameterSet.Config as cms

VertexCompositeCandidateCollectionSelector = cms.EDProducer('VertexCompositeCandidateCollectionSelector',
  lxyCUT = cms.double(16),
  lxyWRTbsCUT = cms.double(0),
  debug = cms.untracked.bool(False)
)
