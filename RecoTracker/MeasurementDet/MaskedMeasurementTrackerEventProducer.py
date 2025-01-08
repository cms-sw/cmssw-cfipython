import FWCore.ParameterSet.Config as cms

def MaskedMeasurementTrackerEventProducer(*args, **kwargs):
  mod = cms.EDProducer('MaskedMeasurementTrackerEventProducer',
    src = cms.InputTag('MeasurementTrackerEvent'),
    clustersToSkip = cms.InputTag(''),
    phase2clustersToSkip = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
