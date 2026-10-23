import FWCore.ParameterSet.Config as cms

def SiPixelFedCablingMapWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelFedCablingMapWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
