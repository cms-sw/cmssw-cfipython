import FWCore.ParameterSet.Config as cms

def OOTPileupCorrectionDBV1Writer(**kwargs):
  mod = cms.EDAnalyzer('OOTPileupCorrectionDBV1Writer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
