import FWCore.ParameterSet.Config as cms

def GEDPhotonCoreProducer(*args, **kwargs):
  mod = cms.EDProducer('GEDPhotonCoreProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
