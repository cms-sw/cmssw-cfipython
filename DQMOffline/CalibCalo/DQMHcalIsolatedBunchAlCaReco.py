import FWCore.ParameterSet.Config as cms

def DQMHcalIsolatedBunchAlCaReco(**kwargs):
  mod = cms.EDProducer('DQMHcalIsolatedBunchAlCaReco',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
