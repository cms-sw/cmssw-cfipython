import FWCore.ParameterSet.Config as cms

def CSCGeometryDump(**kwargs):
  mod = cms.EDAnalyzer('CSCGeometryDump',
    verbose = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
