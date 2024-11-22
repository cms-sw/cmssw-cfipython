import FWCore.ParameterSet.Config as cms

def VertexConstraintProducer(*args, **kwargs):
  mod = cms.EDProducer('VertexConstraintProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
