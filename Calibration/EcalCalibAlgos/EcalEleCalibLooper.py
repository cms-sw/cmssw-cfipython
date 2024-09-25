import FWCore.ParameterSet.Config as cms

def EcalEleCalibLooper(*args, **kwargs):
  mod = cms.Looper('EcalEleCalibLooper')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
