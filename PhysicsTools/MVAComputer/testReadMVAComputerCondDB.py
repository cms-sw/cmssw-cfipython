import FWCore.ParameterSet.Config as cms

def testReadMVAComputerCondDB(**kwargs):
  mod = cms.EDAnalyzer('testReadMVAComputerCondDB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
