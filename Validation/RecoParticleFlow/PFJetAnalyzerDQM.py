import FWCore.ParameterSet.Config as cms

def PFJetAnalyzerDQM(**kwargs):
  mod = cms.EDProducer('PFJetAnalyzerDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
