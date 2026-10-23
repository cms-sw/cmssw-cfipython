import FWCore.ParameterSet.Config as cms

def VersionedPhotonIdProducer(*args, **kwargs):
  mod = cms.EDProducer('VersionedPhotonIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
