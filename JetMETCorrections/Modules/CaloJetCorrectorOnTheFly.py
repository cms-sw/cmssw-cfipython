import FWCore.ParameterSet.Config as cms

def CaloJetCorrectorOnTheFly(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloJetCorrectorOnTheFly',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
