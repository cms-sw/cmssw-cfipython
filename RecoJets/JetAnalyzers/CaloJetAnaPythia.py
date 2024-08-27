import FWCore.ParameterSet.Config as cms

def CaloJetAnaPythia(**kwargs):
  mod = cms.EDAnalyzer('CaloJetAnaPythia',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
