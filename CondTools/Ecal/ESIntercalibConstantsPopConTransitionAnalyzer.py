import FWCore.ParameterSet.Config as cms

def ESIntercalibConstantsPopConTransitionAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ESIntercalibConstantsPopConTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
