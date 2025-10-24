import FWCore.ParameterSet.Config as cms

def TestWriteHostVertexSoA(*args, **kwargs):
  mod = cms.EDProducer('TestWriteHostVertexSoA',
    vertexSize = cms.uint32(1000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
