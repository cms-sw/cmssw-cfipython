import FWCore.ParameterSet.Config as cms

def miscalibExample(*args, **kwargs):
  mod = cms.EDAnalyzer('miscalibExample',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
