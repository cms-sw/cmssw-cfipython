import FWCore.ParameterSet.Config as cms

def DTGeometryValidate(**kwargs):
  mod = cms.EDAnalyzer('DTGeometryValidate',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
