import FWCore.ParameterSet.Config as cms

def L1RCTRelValAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1RCTRelValAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
