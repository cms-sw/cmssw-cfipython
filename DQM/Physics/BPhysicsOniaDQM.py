import FWCore.ParameterSet.Config as cms

def BPhysicsOniaDQM(*args, **kwargs):
  mod = cms.EDProducer('BPhysicsOniaDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
