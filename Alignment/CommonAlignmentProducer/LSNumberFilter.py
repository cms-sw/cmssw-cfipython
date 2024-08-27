import FWCore.ParameterSet.Config as cms

def LSNumberFilter(**kwargs):
  mod = cms.EDFilter('LSNumberFilter',
    minLS = cms.untracked.uint32(21),
    veto_HLT_Menu = cms.untracked.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
