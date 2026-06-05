import FWCore.ParameterSet.Config as cms

def TauValPhotonViewCleaner(*args, **kwargs):
  mod = cms.EDProducer('TauValPhotonViewCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
