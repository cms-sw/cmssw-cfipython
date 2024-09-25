import FWCore.ParameterSet.Config as cms

def GEMGeometryDump(*args, **kwargs):
  mod = cms.EDAnalyzer('GEMGeometryDump',
    verbose = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
