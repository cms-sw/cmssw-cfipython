import FWCore.ParameterSet.Config as cms

def testMagneticField(*args, **kwargs):
  mod = cms.EDAnalyzer('testMagneticField',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
