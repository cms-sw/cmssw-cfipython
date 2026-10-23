import FWCore.ParameterSet.Config as cms

def ConvertedPhotonProducer(*args, **kwargs):
  mod = cms.EDProducer('ConvertedPhotonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
