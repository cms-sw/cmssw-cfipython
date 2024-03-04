import FWCore.ParameterSet.Config as cms

def GEMGeometryDump(**kwargs):
  mod = cms.EDAnalyzer('GEMGeometryDump',
    verbose = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
