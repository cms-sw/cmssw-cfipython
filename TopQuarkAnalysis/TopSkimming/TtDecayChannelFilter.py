import FWCore.ParameterSet.Config as cms

def TtDecayChannelFilter(**kwargs):
  mod = cms.EDFilter('TtDecayChannelFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
