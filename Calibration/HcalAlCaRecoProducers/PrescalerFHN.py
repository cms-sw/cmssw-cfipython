import FWCore.ParameterSet.Config as cms

def PrescalerFHN(*args, **kwargs):
  mod = cms.EDFilter('PrescalerFHN',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
