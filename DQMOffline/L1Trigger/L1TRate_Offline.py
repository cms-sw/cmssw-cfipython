import FWCore.ParameterSet.Config as cms

def L1TRate_Offline(*args, **kwargs):
  mod = cms.EDProducer('L1TRate_Offline',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
