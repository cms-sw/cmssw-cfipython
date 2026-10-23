import FWCore.ParameterSet.Config as cms

def PPSGeometryBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('PPSGeometryBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
