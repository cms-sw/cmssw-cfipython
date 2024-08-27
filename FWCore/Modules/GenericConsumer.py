import FWCore.ParameterSet.Config as cms

def GenericConsumer(**kwargs):
  mod = cms.EDAnalyzer('GenericConsumer',
    eventProducts = cms.untracked.vstring(),
    lumiProducts = cms.untracked.vstring(),
    runProducts = cms.untracked.vstring(),
    processProducts = cms.untracked.vstring(),
    verbose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
