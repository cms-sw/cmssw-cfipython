import FWCore.ParameterSet.Config as cms

def MaskedMeasurementTrackerEventProducer(**kwargs):
  mod = cms.EDProducer('MaskedMeasurementTrackerEventProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
