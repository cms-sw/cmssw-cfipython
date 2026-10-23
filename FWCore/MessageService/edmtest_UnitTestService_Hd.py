import FWCore.ParameterSet.Config as cms

def edmtest_UnitTestService_Hd(*args, **kwargs):
  mod = cms.Service('edmtest::UnitTestService_Hd')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
