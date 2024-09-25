import FWCore.ParameterSet.Config as cms

def EcalADCToGeVConstantPopConBTransitionAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalADCToGeVConstantPopConBTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
