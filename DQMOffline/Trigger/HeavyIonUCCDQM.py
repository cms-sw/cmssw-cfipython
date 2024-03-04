import FWCore.ParameterSet.Config as cms

def HeavyIonUCCDQM(**kwargs):
  mod = cms.EDProducer('HeavyIonUCCDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
