import FWCore.ParameterSet.Config as cms

def PGeometricDetBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('PGeometricDetBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
