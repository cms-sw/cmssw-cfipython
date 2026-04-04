import FWCore.ParameterSet.Config as cms

def SiPixelFedCablingMapTestWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelFedCablingMapTestWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
