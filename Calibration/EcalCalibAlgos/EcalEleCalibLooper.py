import FWCore.ParameterSet.Config as cms

def EcalEleCalibLooper(**kwargs):
  mod = cms.EDLooper('EcalEleCalibLooper')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
