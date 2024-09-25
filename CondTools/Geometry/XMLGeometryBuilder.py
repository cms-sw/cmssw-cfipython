import FWCore.ParameterSet.Config as cms

def XMLGeometryBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('XMLGeometryBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
