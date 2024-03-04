import FWCore.ParameterSet.Config as cms

def CandidateChargeBTagESProducer(**kwargs):
  mod = cms.ESProducer('CandidateChargeBTagESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
