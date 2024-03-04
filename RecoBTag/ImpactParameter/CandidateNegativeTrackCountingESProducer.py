import FWCore.ParameterSet.Config as cms

def CandidateNegativeTrackCountingESProducer(**kwargs):
  mod = cms.ESProducer('CandidateNegativeTrackCountingESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
