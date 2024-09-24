import FWCore.ParameterSet.Config as cms

def HLTInspect(*args, **kwargs):
  mod = cms.EDAnalyzer('HLTInspect',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod