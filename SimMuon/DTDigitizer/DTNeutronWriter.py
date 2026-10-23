import FWCore.ParameterSet.Config as cms

def DTNeutronWriter(*args, **kwargs):
  mod = cms.EDProducer('DTNeutronWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
