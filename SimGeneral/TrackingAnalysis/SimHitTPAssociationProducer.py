import FWCore.ParameterSet.Config as cms

def SimHitTPAssociationProducer(*args, **kwargs):
  mod = cms.EDProducer('SimHitTPAssociationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
