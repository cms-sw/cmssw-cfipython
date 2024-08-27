import FWCore.ParameterSet.Config as cms

def GhostTrackESProducer(**kwargs):
  mod = cms.ESProducer('GhostTrackESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
