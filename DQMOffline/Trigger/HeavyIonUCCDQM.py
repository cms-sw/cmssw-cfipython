import FWCore.ParameterSet.Config as cms

def HeavyIonUCCDQM(*args, **kwargs):
  mod = cms.EDProducer('HeavyIonUCCDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
