import FWCore.ParameterSet.Config as cms

def PGeometricDetBuilder(**kwargs):
  mod = cms.EDAnalyzer('PGeometricDetBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
