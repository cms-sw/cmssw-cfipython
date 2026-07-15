import FWCore.ParameterSet.Config as cms

def TrackFeatureExtractor_alpaka(*args, **kwargs):
  mod = cms.EDProducer('TrackFeatureExtractor@alpaka',
    src = cms.InputTag('hltInitialStepTracks'),
    beamSpot = cms.InputTag('hltOnlineBeamSpot'),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
