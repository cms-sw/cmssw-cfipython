import FWCore.ParameterSet.Config as cms

def HLTPixelThrustFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTPixelThrustFilter',
    inputTag = cms.InputTag('hltSiPixelClusters'),
    minThrust = cms.double(0),
    maxThrust = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
