import FWCore.ParameterSet.Config as cms

def UTC_S2(*args, **kwargs):
  mod = cms.EDAnalyzer('UTC_S2',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
