import FWCore.ParameterSet.Config as cms

def CaloJetCorrectorOnTheFly(**kwargs):
  mod = cms.EDAnalyzer('CaloJetCorrectorOnTheFly',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
