import FWCore.ParameterSet.Config as cms

def AnalyticalPropagatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('AnalyticalPropagatorESProducer',
    ComponentName = cms.required.string,
    SimpleMagneticField = cms.string(''),
    PropagationDirection = cms.required.string,
    MaxDPhi = cms.required.double,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
