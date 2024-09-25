import FWCore.ParameterSet.Config as cms

def trgMatchedPhotonProducer(*args, **kwargs):
  mod = cms.EDProducer('trgMatchedPhotonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
