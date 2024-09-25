import FWCore.ParameterSet.Config as cms

def AssociationMapProducer(*args, **kwargs):
  mod = cms.EDProducer('AssociationMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
