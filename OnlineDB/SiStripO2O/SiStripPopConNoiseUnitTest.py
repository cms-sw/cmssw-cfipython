import FWCore.ParameterSet.Config as cms

def SiStripPopConNoiseUnitTest(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripPopConNoiseUnitTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
