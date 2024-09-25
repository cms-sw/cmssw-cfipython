import FWCore.ParameterSet.Config as cms

def HydjetGeneratorFilter(*args, **kwargs):
  mod = cms.EDFilter('HydjetGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
