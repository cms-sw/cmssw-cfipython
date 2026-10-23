import FWCore.ParameterSet.Config as cms

def IntConsumingAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('IntConsumingAnalyzer',
    getFromModule = cms.required.untracked.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
