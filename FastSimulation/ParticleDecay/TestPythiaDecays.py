import FWCore.ParameterSet.Config as cms

def TestPythiaDecays(*args, **kwargs):
  mod = cms.EDAnalyzer('TestPythiaDecays',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
