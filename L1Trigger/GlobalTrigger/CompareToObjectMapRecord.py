import FWCore.ParameterSet.Config as cms

def CompareToObjectMapRecord(*args, **kwargs):
  mod = cms.EDAnalyzer('CompareToObjectMapRecord',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
