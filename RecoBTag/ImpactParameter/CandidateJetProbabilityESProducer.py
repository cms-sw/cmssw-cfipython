import FWCore.ParameterSet.Config as cms

def CandidateJetProbabilityESProducer(**kwargs):
  mod = cms.ESProducer('CandidateJetProbabilityESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
