import FWCore.ParameterSet.Config as cms

def PFJetPlotsExample(*args, **kwargs):
  mod = cms.EDAnalyzer('PFJetPlotsExample',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
