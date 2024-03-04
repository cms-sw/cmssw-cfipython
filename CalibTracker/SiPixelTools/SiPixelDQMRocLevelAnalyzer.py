import FWCore.ParameterSet.Config as cms

def SiPixelDQMRocLevelAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SiPixelDQMRocLevelAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
