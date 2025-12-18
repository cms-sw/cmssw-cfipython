import FWCore.ParameterSet.Config as cms

def SeedingOTEDProducer(*args, **kwargs):
  mod = cms.EDProducer('SeedingOTEDProducer',
    src = cms.InputTag('siPhase2VectorHits', 'accepted'),
    trackerEvent = cms.InputTag('MeasurementTrackerEvent'),
    beamSpotLabel = cms.InputTag('offlineBeamSpot'),
    updator = cms.string('KFUpdator'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
