import FWCore.ParameterSet.Config as cms

def JPTJetPlotsExample(**kwargs):
  mod = cms.EDAnalyzer('JPTJetPlotsExample',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
