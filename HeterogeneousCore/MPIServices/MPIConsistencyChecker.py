import FWCore.ParameterSet.Config as cms

def MPIConsistencyChecker(*args, **kwargs):
  mod = cms.Service('MPIConsistencyChecker')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
