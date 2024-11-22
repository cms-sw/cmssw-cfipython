import FWCore.ParameterSet.Config as cms

def CSCGeometryOfWires(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCGeometryOfWires',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
