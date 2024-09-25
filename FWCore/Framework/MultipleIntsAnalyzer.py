import FWCore.ParameterSet.Config as cms

def MultipleIntsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('MultipleIntsAnalyzer',
    getFromModules = cms.required.untracked.VInputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
