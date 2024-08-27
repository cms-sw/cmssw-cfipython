import FWCore.ParameterSet.Config as cms

def EcalADCToGeVConstantPopConBTransitionAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalADCToGeVConstantPopConBTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
