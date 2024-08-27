import FWCore.ParameterSet.Config as cms

def WhatsItAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('WhatsItAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
