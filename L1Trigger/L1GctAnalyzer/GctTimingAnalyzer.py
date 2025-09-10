import FWCore.ParameterSet.Config as cms

def GctTimingAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('GctTimingAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
