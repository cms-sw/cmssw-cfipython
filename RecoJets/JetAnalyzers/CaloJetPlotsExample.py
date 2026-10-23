import FWCore.ParameterSet.Config as cms

def CaloJetPlotsExample(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloJetPlotsExample',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
