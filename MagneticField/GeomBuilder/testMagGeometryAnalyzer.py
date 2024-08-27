import FWCore.ParameterSet.Config as cms

def testMagGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('testMagGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
