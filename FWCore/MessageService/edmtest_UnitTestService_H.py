import FWCore.ParameterSet.Config as cms

def edmtest_UnitTestService_H(*args, **kwargs):
  mod = cms.Service('edmtest::UnitTestService_H')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
