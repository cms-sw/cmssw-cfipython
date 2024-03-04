import FWCore.ParameterSet.Config as cms

def CompareToObjectMapRecord(**kwargs):
  mod = cms.EDAnalyzer('CompareToObjectMapRecord',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
