import FWCore.ParameterSet.Config as cms

def HLTPixelActivityFilter(**kwargs):
  mod = cms.EDFilter('HLTPixelActivityFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltSiPixelClusters'),
    minClusters = cms.uint32(3),
    maxClusters = cms.uint32(0),
    minClustersBPix = cms.uint32(0),
    maxClustersBPix = cms.uint32(0),
    minClustersFPix = cms.uint32(0),
    maxClustersFPix = cms.uint32(0),
    minLayersBPix = cms.uint32(0),
    maxLayersBPix = cms.uint32(0),
    minLayersFPix = cms.uint32(0),
    maxLayersFPix = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
