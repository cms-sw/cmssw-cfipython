import FWCore.ParameterSet.Config as cms

def CSCGeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
