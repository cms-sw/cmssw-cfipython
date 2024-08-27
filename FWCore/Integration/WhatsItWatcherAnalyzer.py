import FWCore.ParameterSet.Config as cms

def WhatsItWatcherAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('WhatsItWatcherAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
