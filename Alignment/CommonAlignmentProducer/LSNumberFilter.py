import FWCore.ParameterSet.Config as cms

def LSNumberFilter(*args, **kwargs):
  mod = cms.EDFilter('LSNumberFilter',
    minLS = cms.untracked.uint32(21),
    veto_HLT_Menu = cms.untracked.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
