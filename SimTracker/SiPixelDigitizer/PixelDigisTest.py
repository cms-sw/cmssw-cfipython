import FWCore.ParameterSet.Config as cms

def PixelDigisTest(**kwargs):
  mod = cms.EDAnalyzer('PixelDigisTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
