import FWCore.ParameterSet.Config as cms

def EcalAlignmentPopConBTransitionAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalAlignmentPopConBTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
