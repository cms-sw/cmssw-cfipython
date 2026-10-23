import FWCore.ParameterSet.Config as cms

def CaloSamplesAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloSamplesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
