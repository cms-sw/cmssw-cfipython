import FWCore.ParameterSet.Config as cms

hltSingleVertexPixelTrackFilter = cms.EDFilter('HLTSingleVertexPixelTrackFilter',
  saveTags = cms.bool(True),
  vertexCollection = cms.InputTag('hltPixelVerticesForMinBias'),
  trackCollection = cms.InputTag('hltPixelCands'),
  MinPt = cms.double(0.2),
  MaxPt = cms.double(10000),
  MaxEta = cms.double(1),
  MaxVz = cms.double(10),
  MinTrks = cms.int32(30),
  MinSep = cms.double(0.12)
)
