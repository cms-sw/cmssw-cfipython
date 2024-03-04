import FWCore.ParameterSet.Config as cms

def EcalADCToGeVConstantAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalADCToGeVConstantAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
