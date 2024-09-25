import FWCore.ParameterSet.Config as cms

def HGCHEbackSignalScalerAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCHEbackSignalScalerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
