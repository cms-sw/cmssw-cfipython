import FWCore.ParameterSet.Config as cms

def testWriteMVAComputerCondDB(*args, **kwargs):
  mod = cms.EDAnalyzer('testWriteMVAComputerCondDB',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
