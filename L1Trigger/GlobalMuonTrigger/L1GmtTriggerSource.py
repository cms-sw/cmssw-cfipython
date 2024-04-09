import FWCore.ParameterSet.Config as cms

def L1GmtTriggerSource(**kwargs):
  mod = cms.EDAnalyzer('L1GmtTriggerSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod