import FWCore.ParameterSet.Config as cms

def HLTScoutingPrimaryVertexProducer(**kwargs):
  mod = cms.EDProducer('HLTScoutingPrimaryVertexProducer',
    vertexCollection = cms.InputTag('hltPixelVertices'),
    mantissaPrecision = cms.int32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
