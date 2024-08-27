import FWCore.ParameterSet.Config as cms

def HLTBitAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HLTBitAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
