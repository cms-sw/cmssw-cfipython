import FWCore.ParameterSet.Config as cms

def PropagatorWithMaterialESProducer(*args, **kwargs):
  mod = cms.ESProducer('PropagatorWithMaterialESProducer',
    PropagationDirection = cms.string('alongMomentum'),
    SimpleMagneticField = cms.string(''),
    ComponentName = cms.string(''),
    Mass = cms.double(0),
    MaxDPhi = cms.double(0),
    useRungeKutta = cms.bool(False),
    useOldAnalPropLogic = cms.bool(True),
    ptMin = cms.double(-1),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
