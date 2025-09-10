import FWCore.ParameterSet.Config as cms

def CSCChipSpeedCorrectionDBReadAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCChipSpeedCorrectionDBReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
