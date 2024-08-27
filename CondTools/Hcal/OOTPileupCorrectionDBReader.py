import FWCore.ParameterSet.Config as cms

def OOTPileupCorrectionDBReader(**kwargs):
  mod = cms.EDAnalyzer('OOTPileupCorrectionDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
