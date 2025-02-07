import FWCore.ParameterSet.Config as cms

def testCaloGeometryTools(*args, **kwargs):
  mod = cms.EDAnalyzer('testCaloGeometryTools',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
