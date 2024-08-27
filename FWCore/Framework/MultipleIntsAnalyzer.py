import FWCore.ParameterSet.Config as cms

def MultipleIntsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('MultipleIntsAnalyzer',
    getFromModules = cms.required.untracked.VInputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
