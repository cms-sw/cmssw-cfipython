import FWCore.ParameterSet.Config as cms

hltPixelActivityFilter = cms.EDFilter('HLTPixelActivityFilter',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltSiPixelClusters'),
  minClusters = cms.uint32(3),
  maxClusters = cms.uint32(0),
  minLayersBPix = cms.uint32(0),
  maxLayersBPix = cms.uint32(0),
  minLayersFPix = cms.uint32(0),
  maxLayersFPix = cms.uint32(0)
)
