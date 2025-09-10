import FWCore.ParameterSet.Config as cms

def testReadMVAComputerCondDB(*args, **kwargs):
  mod = cms.EDAnalyzer('testReadMVAComputerCondDB',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
