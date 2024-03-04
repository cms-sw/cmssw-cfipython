import FWCore.ParameterSet.Config as cms

def ME0GeometryDump(**kwargs):
  mod = cms.EDAnalyzer('ME0GeometryDump',
    verbose = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
