import FWCore.ParameterSet.Config as cms

def SeedGeneratorFromL1TTracksEDProducer(**kwargs):
  mod = cms.EDProducer('SeedGeneratorFromL1TTracksEDProducer',
    InputCollection = cms.InputTag('l1tTTTracksFromTrackletEmulation', 'Level1TTTracks'),
    estimator = cms.string(''),
    propagator = cms.string(''),
    MeasurementTrackerEvent = cms.InputTag(''),
    minEtaForTEC = cms.double(0.9),
    maxEtaForTOB = cms.double(1.2),
    errorSFHitless = cms.double(1e-09),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
