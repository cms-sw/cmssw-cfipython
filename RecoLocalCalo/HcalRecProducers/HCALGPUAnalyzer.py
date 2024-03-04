import FWCore.ParameterSet.Config as cms

def HCALGPUAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HCALGPUAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
