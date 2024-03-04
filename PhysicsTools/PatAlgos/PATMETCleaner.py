import FWCore.ParameterSet.Config as cms

def PATMETCleaner(**kwargs):
  mod = cms.EDProducer('PATMETCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
