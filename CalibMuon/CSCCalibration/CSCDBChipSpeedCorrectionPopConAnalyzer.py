import FWCore.ParameterSet.Config as cms

def CSCDBChipSpeedCorrectionPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCDBChipSpeedCorrectionPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
