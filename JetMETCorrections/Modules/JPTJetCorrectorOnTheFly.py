import FWCore.ParameterSet.Config as cms

def JPTJetCorrectorOnTheFly(**kwargs):
  mod = cms.EDAnalyzer('JPTJetCorrectorOnTheFly',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
