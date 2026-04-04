import FWCore.ParameterSet.Config as cms

def CSCGeometryOfStrips(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCGeometryOfStrips',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
