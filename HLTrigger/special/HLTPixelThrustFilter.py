import FWCore.ParameterSet.Config as cms

def HLTPixelThrustFilter(**kwargs):
  mod = cms.EDFilter('HLTPixelThrustFilter',
    inputTag = cms.InputTag('hltSiPixelClusters'),
    minThrust = cms.double(0),
    maxThrust = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
