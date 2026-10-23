import FWCore.ParameterSet.Config as cms

def WhatsItWatcherAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('WhatsItWatcherAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
