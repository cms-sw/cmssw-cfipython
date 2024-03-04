import FWCore.ParameterSet.Config as cms

def PropagatorWithMaterialESProducer(**kwargs):
  mod = cms.ESProducer('PropagatorWithMaterialESProducer',
    PropagationDirection = cms.required.string,
    SimpleMagneticField = cms.string(''),
    ComponentName = cms.required.string,
    Mass = cms.required.double,
    MaxDPhi = cms.required.double,
    useRungeKutta = cms.required.bool,
    useOldAnalPropLogic = cms.bool(True),
    ptMin = cms.double(-1),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
