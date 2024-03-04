import FWCore.ParameterSet.Config as cms

def testWriteMVAComputerCondDB(**kwargs):
  mod = cms.EDAnalyzer('testWriteMVAComputerCondDB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
