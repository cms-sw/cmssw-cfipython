import FWCore.ParameterSet.Config as cms

def SiPixelFedCablingMapTestWriter(**kwargs):
  mod = cms.EDAnalyzer('SiPixelFedCablingMapTestWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
