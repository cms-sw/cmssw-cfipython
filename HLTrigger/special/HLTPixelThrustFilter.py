import FWCore.ParameterSet.Config as cms

def HLTPixelThrustFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTPixelThrustFilter',
    inputTag = cms.InputTag('hltSiPixelClusters'),
    useOnlySaturatedPixels = cms.bool(False),
    minNPixels = cms.uint32(2),
    maxNPixels = cms.uint32(0),
    minNSaturatedPixels = cms.uint32(0),
    maxNSaturatedPixels = cms.uint32(0),
    minThrust = cms.double(0),
    maxThrust = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
