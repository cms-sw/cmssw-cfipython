import FWCore.ParameterSet.Config as cms

def IOVPayloadAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('IOVPayloadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
