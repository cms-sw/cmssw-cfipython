import FWCore.ParameterSet.Config as cms

def IntConsumingAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('IntConsumingAnalyzer',
    getFromModule = cms.required.untracked.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
