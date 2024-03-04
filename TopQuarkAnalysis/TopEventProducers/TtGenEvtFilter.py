import FWCore.ParameterSet.Config as cms

def TtGenEvtFilter(**kwargs):
  mod = cms.EDFilter('TtGenEvtFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
