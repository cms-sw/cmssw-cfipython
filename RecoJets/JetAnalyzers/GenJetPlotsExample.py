import FWCore.ParameterSet.Config as cms

def GenJetPlotsExample(*args, **kwargs):
  mod = cms.EDAnalyzer('GenJetPlotsExample',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
