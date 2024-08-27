import FWCore.ParameterSet.Config as cms

def JetCorrectorDemo(**kwargs):
  mod = cms.EDAnalyzer('JetCorrectorDemo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
