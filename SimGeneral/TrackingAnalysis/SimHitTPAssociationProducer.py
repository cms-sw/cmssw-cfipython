import FWCore.ParameterSet.Config as cms

def SimHitTPAssociationProducer(**kwargs):
  mod = cms.EDProducer('SimHitTPAssociationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
