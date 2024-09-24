import FWCore.ParameterSet.Config as cms

def PATVertexAssociationProducer(*args, **kwargs):
  mod = cms.EDProducer('PATVertexAssociationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod