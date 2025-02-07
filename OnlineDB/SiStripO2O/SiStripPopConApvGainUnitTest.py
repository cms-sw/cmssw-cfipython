import FWCore.ParameterSet.Config as cms

def SiStripPopConApvGainUnitTest(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripPopConApvGainUnitTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
