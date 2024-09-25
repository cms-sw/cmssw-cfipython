import FWCore.ParameterSet.Config as cms

def CSCGeometryValidate(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCGeometryValidate',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
