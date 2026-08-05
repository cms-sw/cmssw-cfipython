import FWCore.ParameterSet.Config as cms

def TICLGeomAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TICLGeomAnalyzer',
    label = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
