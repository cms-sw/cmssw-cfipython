import FWCore.ParameterSet.Config as cms

def DeDxDiscriminatorLearner(*args, **kwargs):
  mod = cms.EDAnalyzer('DeDxDiscriminatorLearner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
