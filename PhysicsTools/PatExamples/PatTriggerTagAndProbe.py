import FWCore.ParameterSet.Config as cms

def PatTriggerTagAndProbe(**kwargs):
  mod = cms.EDAnalyzer('PatTriggerTagAndProbe',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
