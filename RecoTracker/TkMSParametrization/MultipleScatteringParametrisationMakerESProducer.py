import FWCore.ParameterSet.Config as cms

def MultipleScatteringParametrisationMakerESProducer(**kwargs):
  mod = cms.ESProducer('MultipleScatteringParametrisationMakerESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
