import FWCore.ParameterSet.Config as cms

def JetCorrectorDemo(*args, **kwargs):
  mod = cms.EDAnalyzer('JetCorrectorDemo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
