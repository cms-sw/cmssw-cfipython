import FWCore.ParameterSet.Config as cms

def test_NoiseBuilder(**kwargs):
  mod = cms.EDAnalyzer('test_NoiseBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
