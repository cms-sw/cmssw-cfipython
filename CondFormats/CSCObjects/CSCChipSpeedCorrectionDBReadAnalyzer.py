import FWCore.ParameterSet.Config as cms

def CSCChipSpeedCorrectionDBReadAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCChipSpeedCorrectionDBReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
