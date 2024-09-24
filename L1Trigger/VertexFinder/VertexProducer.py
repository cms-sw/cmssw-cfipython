import FWCore.ParameterSet.Config as cms

def VertexProducer(*args, **kwargs):
  mod = cms.EDProducer('VertexProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
