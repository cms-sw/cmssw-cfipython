import FWCore.ParameterSet.Config as cms

def DTTTrigCorrectionFirst(**kwargs):
  mod = cms.EDAnalyzer('DTTTrigCorrectionFirst',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
