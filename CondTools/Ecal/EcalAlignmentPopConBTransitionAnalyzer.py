import FWCore.ParameterSet.Config as cms

def EcalAlignmentPopConBTransitionAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalAlignmentPopConBTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
