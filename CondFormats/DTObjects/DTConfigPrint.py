import FWCore.ParameterSet.Config as cms

def DTConfigPrint(**kwargs):
  mod = cms.EDAnalyzer('DTConfigPrint',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod