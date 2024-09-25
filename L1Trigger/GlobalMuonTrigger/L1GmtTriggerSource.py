import FWCore.ParameterSet.Config as cms

def L1GmtTriggerSource(*args, **kwargs):
  mod = cms.EDAnalyzer('L1GmtTriggerSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
