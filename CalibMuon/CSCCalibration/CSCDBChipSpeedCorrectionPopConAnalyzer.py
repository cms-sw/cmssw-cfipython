import FWCore.ParameterSet.Config as cms

def CSCDBChipSpeedCorrectionPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCDBChipSpeedCorrectionPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
