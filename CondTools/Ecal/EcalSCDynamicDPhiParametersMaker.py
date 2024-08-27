import FWCore.ParameterSet.Config as cms

def EcalSCDynamicDPhiParametersMaker(**kwargs):
  mod = cms.EDAnalyzer('EcalSCDynamicDPhiParametersMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
