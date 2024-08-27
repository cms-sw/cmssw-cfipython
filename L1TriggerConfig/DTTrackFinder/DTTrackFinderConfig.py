import FWCore.ParameterSet.Config as cms

def DTTrackFinderConfig(**kwargs):
  mod = cms.ESProducer('DTTrackFinderConfig',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
