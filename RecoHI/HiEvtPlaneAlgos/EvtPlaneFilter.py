import FWCore.ParameterSet.Config as cms

def EvtPlaneFilter(**kwargs):
  mod = cms.EDFilter('EvtPlaneFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
