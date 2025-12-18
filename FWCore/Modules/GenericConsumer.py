import FWCore.ParameterSet.Config as cms

def GenericConsumer(*args, **kwargs):
  mod = cms.EDAnalyzer('GenericConsumer',
    eventProducts = cms.untracked.vstring(),
    lumiProducts = cms.untracked.vstring(),
    runProducts = cms.untracked.vstring(),
    processProducts = cms.untracked.vstring(),
    verbose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
