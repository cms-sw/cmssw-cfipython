import FWCore.ParameterSet.Config as cms

def StreamThingAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('StreamThingAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
