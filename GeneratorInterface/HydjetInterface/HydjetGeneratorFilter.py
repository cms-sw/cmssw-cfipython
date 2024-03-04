import FWCore.ParameterSet.Config as cms

def HydjetGeneratorFilter(**kwargs):
  mod = cms.EDFilter('HydjetGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
