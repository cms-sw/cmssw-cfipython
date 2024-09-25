import FWCore.ParameterSet.Config as cms

def CSCGeometryDump(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCGeometryDump',
    verbose = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
