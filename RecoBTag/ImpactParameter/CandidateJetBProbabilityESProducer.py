import FWCore.ParameterSet.Config as cms

def CandidateJetBProbabilityESProducer(**kwargs):
  mod = cms.ESProducer('CandidateJetBProbabilityESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
