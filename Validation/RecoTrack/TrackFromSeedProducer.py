import FWCore.ParameterSet.Config as cms

def TrackFromSeedProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackFromSeedProducer',
    TTRHBuilder = cms.string(''),
    src = cms.InputTag(''),
    beamSpot = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
