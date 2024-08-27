import FWCore.ParameterSet.Config as cms

def TtFullLepEvtFilter(**kwargs):
  mod = cms.EDFilter('TtFullLepEvtFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
