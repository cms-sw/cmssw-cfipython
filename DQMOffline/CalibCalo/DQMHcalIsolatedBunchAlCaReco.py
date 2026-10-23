import FWCore.ParameterSet.Config as cms

def DQMHcalIsolatedBunchAlCaReco(*args, **kwargs):
  mod = cms.EDProducer('DQMHcalIsolatedBunchAlCaReco',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
