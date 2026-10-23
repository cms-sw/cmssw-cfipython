import FWCore.ParameterSet.Config as cms

def WhatsItAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('WhatsItAnalyzer',
    expectedValues = cms.untracked.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
