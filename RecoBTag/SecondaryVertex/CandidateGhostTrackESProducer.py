import FWCore.ParameterSet.Config as cms

def CandidateGhostTrackESProducer(*args, **kwargs):
  mod = cms.ESProducer('CandidateGhostTrackESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
