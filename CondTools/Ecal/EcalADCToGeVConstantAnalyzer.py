import FWCore.ParameterSet.Config as cms

def EcalADCToGeVConstantAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalADCToGeVConstantAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
