import FWCore.ParameterSet.Config as cms

def ModelpMSSMFilter(*args, **kwargs):
  mod = cms.EDFilter('ModelpMSSMFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
