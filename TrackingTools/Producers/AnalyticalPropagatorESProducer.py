import FWCore.ParameterSet.Config as cms

def AnalyticalPropagatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('AnalyticalPropagatorESProducer',
    ComponentName = cms.string('AnalyticalPropagator'),
    SimpleMagneticField = cms.string(''),
    PropagationDirection = cms.string('alongMomentum'),
    MaxDPhi = cms.double(1.6),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
