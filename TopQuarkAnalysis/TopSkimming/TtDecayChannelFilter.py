import FWCore.ParameterSet.Config as cms

def TtDecayChannelFilter(*args, **kwargs):
  mod = cms.EDFilter('TtDecayChannelFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
