import FWCore.ParameterSet.Config as cms

def TBHodoActiveVolumeRawInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('TBHodoActiveVolumeRawInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
