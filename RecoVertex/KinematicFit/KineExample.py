import FWCore.ParameterSet.Config as cms

def KineExample(*args, **kwargs):
  mod = cms.EDAnalyzer('KineExample',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
