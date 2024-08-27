import FWCore.ParameterSet.Config as cms

def HGCHEbackSignalScalerAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HGCHEbackSignalScalerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
