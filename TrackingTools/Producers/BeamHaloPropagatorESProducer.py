import FWCore.ParameterSet.Config as cms

def BeamHaloPropagatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('BeamHaloPropagatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
