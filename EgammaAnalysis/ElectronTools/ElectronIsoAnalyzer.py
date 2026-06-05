import FWCore.ParameterSet.Config as cms

def ElectronIsoAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ElectronIsoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
