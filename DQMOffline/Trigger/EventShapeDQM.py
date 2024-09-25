import FWCore.ParameterSet.Config as cms

def EventShapeDQM(*args, **kwargs):
  mod = cms.EDProducer('EventShapeDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
