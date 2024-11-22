import FWCore.ParameterSet.Config as cms

def EvtPlaneFilter(*args, **kwargs):
  mod = cms.EDFilter('EvtPlaneFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
