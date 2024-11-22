import FWCore.ParameterSet.Config as cms

def ProbeMulteplicityProducer(*args, **kwargs):
  mod = cms.EDProducer('ProbeMulteplicityProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
