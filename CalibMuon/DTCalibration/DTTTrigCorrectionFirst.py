import FWCore.ParameterSet.Config as cms

def DTTTrigCorrectionFirst(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTTrigCorrectionFirst',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
