import FWCore.ParameterSet.Config as cms

def VertexCompositePtrCandidateAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('VertexCompositePtrCandidateAssociatorEDProducer',
    recoVertices = cms.required.InputTag,
    simVertices = cms.required.InputTag,
    associator = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
