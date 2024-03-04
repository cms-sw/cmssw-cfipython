import FWCore.ParameterSet.Config as cms

def DTGeometryTest(**kwargs):
  mod = cms.EDAnalyzer('DTGeometryTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
