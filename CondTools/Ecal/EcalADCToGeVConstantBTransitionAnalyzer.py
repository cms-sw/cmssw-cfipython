import FWCore.ParameterSet.Config as cms

def EcalADCToGeVConstantBTransitionAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalADCToGeVConstantBTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
