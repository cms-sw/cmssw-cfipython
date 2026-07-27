import FWCore.ParameterSet.Config as cms

def edmtest_DelayESCallsService(*args, **kwargs):
  mod = cms.Service('edmtest::DelayESCallsService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
