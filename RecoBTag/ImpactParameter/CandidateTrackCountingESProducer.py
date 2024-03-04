import FWCore.ParameterSet.Config as cms

def CandidateTrackCountingESProducer(**kwargs):
  mod = cms.ESProducer('CandidateTrackCountingESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
