import FWCore.ParameterSet.Config as cms

def CSCGeometryAsChambers(**kwargs):
  mod = cms.EDAnalyzer('CSCGeometryAsChambers',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
