import FWCore.ParameterSet.Config as cms

def SiStripPopConNoiseUnitTest(**kwargs):
  mod = cms.EDAnalyzer('SiStripPopConNoiseUnitTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
