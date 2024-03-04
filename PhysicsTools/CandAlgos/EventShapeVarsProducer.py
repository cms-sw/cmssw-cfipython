import FWCore.ParameterSet.Config as cms

def EventShapeVarsProducer(**kwargs):
  mod = cms.EDProducer('EventShapeVarsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
