import FWCore.ParameterSet.Config as cms

def EventShapeDQM(**kwargs):
  mod = cms.EDProducer('EventShapeDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
