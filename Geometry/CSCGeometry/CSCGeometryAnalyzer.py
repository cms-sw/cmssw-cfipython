import FWCore.ParameterSet.Config as cms

def CSCGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
