import FWCore.ParameterSet.Config as cms

def HLTPixelAsymmetryFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTPixelAsymmetryFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltSiPixelClusters'),
    MinAsym = cms.double(0),
    MaxAsym = cms.double(1),
    MinCharge = cms.double(4000),
    MinBarrel = cms.double(10000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
