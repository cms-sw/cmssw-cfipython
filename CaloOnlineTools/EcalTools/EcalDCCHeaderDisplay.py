import FWCore.ParameterSet.Config as cms

def EcalDCCHeaderDisplay(**kwargs):
  mod = cms.EDAnalyzer('EcalDCCHeaderDisplay',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
