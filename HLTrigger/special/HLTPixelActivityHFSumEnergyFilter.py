import FWCore.ParameterSet.Config as cms

def HLTPixelActivityHFSumEnergyFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTPixelActivityHFSumEnergyFilter',
    inputTag = cms.InputTag('hltSiPixelClusters'),
    HFHitCollection = cms.InputTag('hltHfreco'),
    eCut_HF = cms.double(0),
    eMin_HF = cms.double(10000),
    offset = cms.double(-1000),
    slope = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
