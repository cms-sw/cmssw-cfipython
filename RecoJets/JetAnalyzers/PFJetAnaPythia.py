import FWCore.ParameterSet.Config as cms

def PFJetAnaPythia(**kwargs):
  mod = cms.EDAnalyzer('PFJetAnaPythia',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
