import FWCore.ParameterSet.Config as cms

def BeamHaloPropagatorESProducer(**kwargs):
  mod = cms.ESProducer('BeamHaloPropagatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
