import FWCore.ParameterSet.Config as cms

def CaloMatchingExample(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloMatchingExample',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
