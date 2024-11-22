import FWCore.ParameterSet.Config as cms

def VertexMerger(*args, **kwargs):
  mod = cms.EDProducer('VertexMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
