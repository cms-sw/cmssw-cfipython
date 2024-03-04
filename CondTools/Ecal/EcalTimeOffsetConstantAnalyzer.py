import FWCore.ParameterSet.Config as cms

def EcalTimeOffsetConstantAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalTimeOffsetConstantAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
