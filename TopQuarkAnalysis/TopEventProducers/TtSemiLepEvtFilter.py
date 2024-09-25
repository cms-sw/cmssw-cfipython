import FWCore.ParameterSet.Config as cms

def TtSemiLepEvtFilter(*args, **kwargs):
  mod = cms.EDFilter('TtSemiLepEvtFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
