import FWCore.ParameterSet.Config as cms

def PixelSimHitsTest(**kwargs):
  mod = cms.EDAnalyzer('PixelSimHitsTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
