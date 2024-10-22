import FWCore.ParameterSet.Config as cms

def SuperclusValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('SuperclusValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
