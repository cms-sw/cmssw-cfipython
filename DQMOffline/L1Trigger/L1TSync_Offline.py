import FWCore.ParameterSet.Config as cms

def L1TSync_Offline(*args, **kwargs):
  mod = cms.EDProducer('L1TSync_Offline',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
