import FWCore.ParameterSet.Config as cms

def DeDxDiscriminatorLearner(**kwargs):
  mod = cms.EDAnalyzer('DeDxDiscriminatorLearner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
