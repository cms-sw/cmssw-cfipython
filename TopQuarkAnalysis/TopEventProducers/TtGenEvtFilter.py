import FWCore.ParameterSet.Config as cms

def TtGenEvtFilter(*args, **kwargs):
  mod = cms.EDFilter('TtGenEvtFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
