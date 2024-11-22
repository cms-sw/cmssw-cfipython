import FWCore.ParameterSet.Config as cms

def CandidateNegativeTrackCountingESProducer(*args, **kwargs):
  mod = cms.ESProducer('CandidateNegativeTrackCountingESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
