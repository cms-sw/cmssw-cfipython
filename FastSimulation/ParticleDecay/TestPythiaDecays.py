import FWCore.ParameterSet.Config as cms

def TestPythiaDecays(**kwargs):
  mod = cms.EDAnalyzer('TestPythiaDecays',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
