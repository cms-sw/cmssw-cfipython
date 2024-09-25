import FWCore.ParameterSet.Config as cms

def CandidateTrackCountingESProducer(*args, **kwargs):
  mod = cms.ESProducer('CandidateTrackCountingESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
