import FWCore.ParameterSet.Config as cms

def SiPixelFedCablingMapAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SiPixelFedCablingMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
