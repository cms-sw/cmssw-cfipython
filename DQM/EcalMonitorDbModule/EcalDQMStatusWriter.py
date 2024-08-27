import FWCore.ParameterSet.Config as cms

def EcalDQMStatusWriter(**kwargs):
  mod = cms.EDAnalyzer('EcalDQMStatusWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
