import FWCore.ParameterSet.Config as cms

def CSCDBGasGainCorrectionPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCDBGasGainCorrectionPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
