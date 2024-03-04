import FWCore.ParameterSet.Config as cms

def TestEcalGetWindow(**kwargs):
  mod = cms.EDAnalyzer('TestEcalGetWindow',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
