import FWCore.ParameterSet.Config as cms

def VertexAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('VertexAssociatorEDProducer',
    recoVertices = cms.required.InputTag,
    simVertices = cms.required.InputTag,
    associator = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
