import FWCore.ParameterSet.Config as cms

def PATVertexAssociationProducer(**kwargs):
  mod = cms.EDProducer('PATVertexAssociationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
