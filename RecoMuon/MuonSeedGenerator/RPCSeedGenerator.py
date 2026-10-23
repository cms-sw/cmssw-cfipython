import FWCore.ParameterSet.Config as cms

def RPCSeedGenerator(*args, **kwargs):
  mod = cms.EDProducer('RPCSeedGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
