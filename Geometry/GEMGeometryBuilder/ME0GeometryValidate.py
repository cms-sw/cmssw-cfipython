import FWCore.ParameterSet.Config as cms

def ME0GeometryValidate(**kwargs):
  mod = cms.EDAnalyzer('ME0GeometryValidate',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
