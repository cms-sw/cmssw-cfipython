import FWCore.ParameterSet.Config as cms

def testMagGeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('testMagGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
