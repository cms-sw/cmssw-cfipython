import FWCore.ParameterSet.Config as cms

def SeedingOTEDProducer(**kwargs):
  mod = cms.EDProducer('SeedingOTEDProducer',
    src = cms.InputTag('siPhase2VectorHits', 'accepted'),
    trackerEvent = cms.InputTag('MeasurementTrackerEvent'),
    beamSpotLabel = cms.InputTag('offlineBeamSpot'),
    updator = cms.string('KFUpdator'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
