import FWCore.ParameterSet.Config as cms

def HLTScoutingPrimaryVertexProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTScoutingPrimaryVertexProducer',
    vertexCollection = cms.InputTag('hltPixelVertices'),
    mantissaPrecision = cms.int32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
