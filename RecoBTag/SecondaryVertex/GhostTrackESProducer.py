import FWCore.ParameterSet.Config as cms

def GhostTrackESProducer(*args, **kwargs):
  mod = cms.ESProducer('GhostTrackESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
