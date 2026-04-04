import FWCore.ParameterSet.Config as cms

def SmartPropagatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('SmartPropagatorESProducer',
    ComponentName = cms.string('SmartPropagator'),
    PropagationDirection = cms.string('alongMomentum'),
    Epsilon = cms.double(5),
    TrackerPropagator = cms.string('PropagatorWithMaterial'),
    MuonPropagator = cms.string('SteppingHelixPropagatorAlong'),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
