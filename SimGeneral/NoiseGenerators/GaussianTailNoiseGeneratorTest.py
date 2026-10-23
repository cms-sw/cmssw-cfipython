import FWCore.ParameterSet.Config as cms

def GaussianTailNoiseGeneratorTest(*args, **kwargs):
  mod = cms.EDAnalyzer('GaussianTailNoiseGeneratorTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
