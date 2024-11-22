import FWCore.ParameterSet.Config as cms

def DAFTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('DAFTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
