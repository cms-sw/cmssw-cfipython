import FWCore.ParameterSet.Config as cms

def testMagneticField(**kwargs):
  mod = cms.EDAnalyzer('testMagneticField',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
