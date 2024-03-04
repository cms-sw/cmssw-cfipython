import FWCore.ParameterSet.Config as cms

def TauValPhotonViewCleaner(**kwargs):
  mod = cms.EDProducer('TauValPhotonViewCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
