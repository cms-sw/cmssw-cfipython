import FWCore.ParameterSet.Config as cms

def WhatsItAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('WhatsItAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
