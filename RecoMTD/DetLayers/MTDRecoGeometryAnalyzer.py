import FWCore.ParameterSet.Config as cms

def MTDRecoGeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('MTDRecoGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
