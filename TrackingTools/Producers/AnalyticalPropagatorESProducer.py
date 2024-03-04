import FWCore.ParameterSet.Config as cms

def AnalyticalPropagatorESProducer(**kwargs):
  mod = cms.ESProducer('AnalyticalPropagatorESProducer',
    ComponentName = cms.required.string,
    SimpleMagneticField = cms.string(''),
    PropagationDirection = cms.required.string,
    MaxDPhi = cms.required.double,
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
