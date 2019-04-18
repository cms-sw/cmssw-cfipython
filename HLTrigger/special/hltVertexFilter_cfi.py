import FWCore.ParameterSet.Config as cms

hltVertexFilter = cms.EDFilter('HLTVertexFilter',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltPixelVertices'),
  minNDoF = cms.double(0),
  maxChi2 = cms.double(99999),
  maxD0 = cms.double(1),
  maxZ = cms.double(15),
  minVertices = cms.uint32(1)
)
