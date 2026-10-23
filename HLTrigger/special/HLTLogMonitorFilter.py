import FWCore.ParameterSet.Config as cms

def HLTLogMonitorFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTLogMonitorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
