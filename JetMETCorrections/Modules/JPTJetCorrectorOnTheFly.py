import FWCore.ParameterSet.Config as cms

def JPTJetCorrectorOnTheFly(*args, **kwargs):
  mod = cms.EDAnalyzer('JPTJetCorrectorOnTheFly',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
