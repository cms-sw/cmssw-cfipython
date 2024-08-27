import FWCore.ParameterSet.Config as cms

def IOVPayloadAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('IOVPayloadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
