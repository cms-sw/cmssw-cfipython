import FWCore.ParameterSet.Config as cms

def MuonTransientTrackingRecHitBuilderESProducer(**kwargs):
  mod = cms.ESProducer('MuonTransientTrackingRecHitBuilderESProducer',
    ComponentName = cms.required.string,
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
