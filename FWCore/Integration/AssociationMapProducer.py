import FWCore.ParameterSet.Config as cms

def AssociationMapProducer(*args, **kwargs):
  mod = cms.EDProducer('AssociationMapProducer',
    inputTag1 = cms.required.InputTag,
    inputTag2 = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
