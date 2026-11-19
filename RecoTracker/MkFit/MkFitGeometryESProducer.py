import FWCore.ParameterSet.Config as cms

def MkFitGeometryESProducer(*args, **kwargs):
  mod = cms.ESProducer('MkFitGeometryESProducer',
    bFieldParams = cms.vdouble(
      3.81036,
      -2.03767e-06,
      7.34495e-06,
      3.01291e-07
    ),
    refitBFieldAtMid = cms.bool(True),
    refitRadialFieldCorr = cms.bool(True),
    refitElossSignFromPass = cms.bool(True),
    refitBkwMsFixedMomentum = cms.bool(True),
    refitBkwSubSteps = cms.int32(2),
    refitMaterialPerModule = cms.bool(True),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
