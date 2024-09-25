import FWCore.ParameterSet.Config as cms

def CandidateJetBProbabilityESProducer(*args, **kwargs):
  mod = cms.ESProducer('CandidateJetBProbabilityESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
