import FWCore.ParameterSet.Config as cms

def CSCGeometryAsChambers(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCGeometryAsChambers',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
