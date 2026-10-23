import FWCore.ParameterSet.Config as cms

def SecondaryProducer(*args, **kwargs):
  mod = cms.EDProducer('SecondaryProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
