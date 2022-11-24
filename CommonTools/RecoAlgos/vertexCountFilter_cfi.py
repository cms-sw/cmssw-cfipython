import FWCore.ParameterSet.Config as cms

vertexCountFilter = cms.EDFilter('VertexCountFilter',
  src = cms.InputTag(''),
  minNumber = cms.uint32(0),
  maxNumber = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
