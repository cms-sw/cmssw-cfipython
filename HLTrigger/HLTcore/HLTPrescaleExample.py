import FWCore.ParameterSet.Config as cms

def HLTPrescaleExample(*args, **kwargs):
  mod = cms.EDAnalyzer('HLTPrescaleExample',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
