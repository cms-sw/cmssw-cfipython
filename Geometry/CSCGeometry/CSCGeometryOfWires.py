import FWCore.ParameterSet.Config as cms

def CSCGeometryOfWires(**kwargs):
  mod = cms.EDAnalyzer('CSCGeometryOfWires',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
