import FWCore.ParameterSet.Config as cms

def GenJetAnaPythia(**kwargs):
  mod = cms.EDAnalyzer('GenJetAnaPythia',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
