import FWCore.ParameterSet.Config as cms

def DisplacedVertexProducer(*args, **kwargs):
  mod = cms.EDProducer('DisplacedVertexProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
