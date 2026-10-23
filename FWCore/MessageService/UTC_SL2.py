import FWCore.ParameterSet.Config as cms

def UTC_SL2(*args, **kwargs):
  mod = cms.EDAnalyzer('UTC_SL2',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
