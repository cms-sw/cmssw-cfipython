import FWCore.ParameterSet.Config as cms

def HLTLogMonitorFilter(**kwargs):
  mod = cms.EDFilter('HLTLogMonitorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
