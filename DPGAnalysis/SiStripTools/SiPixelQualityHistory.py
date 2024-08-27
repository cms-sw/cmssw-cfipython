import FWCore.ParameterSet.Config as cms

def SiPixelQualityHistory(**kwargs):
  mod = cms.EDAnalyzer('SiPixelQualityHistory',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
