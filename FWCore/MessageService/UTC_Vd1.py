import FWCore.ParameterSet.Config as cms

def UTC_Vd1(*args, **kwargs):
  mod = cms.EDAnalyzer('UTC_Vd1',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
