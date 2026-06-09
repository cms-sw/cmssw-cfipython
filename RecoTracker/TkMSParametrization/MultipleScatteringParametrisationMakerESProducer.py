import FWCore.ParameterSet.Config as cms

def MultipleScatteringParametrisationMakerESProducer(*args, **kwargs):
  mod = cms.ESProducer('MultipleScatteringParametrisationMakerESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
