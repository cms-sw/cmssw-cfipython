import FWCore.ParameterSet.Config as cms

def PPSSimTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('PPSSimTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
