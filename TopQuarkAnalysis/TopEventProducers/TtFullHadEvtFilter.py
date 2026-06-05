import FWCore.ParameterSet.Config as cms

def TtFullHadEvtFilter(*args, **kwargs):
  mod = cms.EDFilter('TtFullHadEvtFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
