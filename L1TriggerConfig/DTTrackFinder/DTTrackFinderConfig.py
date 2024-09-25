import FWCore.ParameterSet.Config as cms

def DTTrackFinderConfig(*args, **kwargs):
  mod = cms.ESProducer('DTTrackFinderConfig',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
