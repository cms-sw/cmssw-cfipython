import FWCore.ParameterSet.Config as cms

def LSTPixelSeedInputProducer(*args, **kwargs):
  mod = cms.EDProducer('LSTPixelSeedInputProducer',
    beamSpot = cms.InputTag('offlineBeamSpot'),
    seedTracks = cms.VInputTag(
      'lstInitialStepSeedTracks',
      'lstHighPtTripletStepSeedTracks'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
