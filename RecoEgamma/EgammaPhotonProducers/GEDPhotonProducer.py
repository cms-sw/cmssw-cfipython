import FWCore.ParameterSet.Config as cms

def GEDPhotonProducer(*args, **kwargs):
  mod = cms.EDProducer('GEDPhotonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
