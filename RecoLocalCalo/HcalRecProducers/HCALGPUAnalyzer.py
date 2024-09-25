import FWCore.ParameterSet.Config as cms

def HCALGPUAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HCALGPUAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
