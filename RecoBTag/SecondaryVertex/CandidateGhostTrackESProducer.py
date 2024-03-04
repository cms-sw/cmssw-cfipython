import FWCore.ParameterSet.Config as cms

def CandidateGhostTrackESProducer(**kwargs):
  mod = cms.ESProducer('CandidateGhostTrackESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
