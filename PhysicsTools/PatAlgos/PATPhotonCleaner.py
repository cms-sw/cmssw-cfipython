import FWCore.ParameterSet.Config as cms

def PATPhotonCleaner(**kwargs):
  mod = cms.EDProducer('PATPhotonCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
