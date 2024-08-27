import FWCore.ParameterSet.Config as cms

def L1MuCSCTFParametersTester(**kwargs):
  mod = cms.EDAnalyzer('L1MuCSCTFParametersTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
