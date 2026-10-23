import FWCore.ParameterSet.Config as cms

def PCaloGeometryBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('PCaloGeometryBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
