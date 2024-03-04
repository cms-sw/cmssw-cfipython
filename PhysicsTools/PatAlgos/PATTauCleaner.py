import FWCore.ParameterSet.Config as cms

def PATTauCleaner(**kwargs):
  mod = cms.EDProducer('PATTauCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
