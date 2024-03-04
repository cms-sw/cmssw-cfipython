import FWCore.ParameterSet.Config as cms

def DD4hepTestDDDWorld(**kwargs):
  mod = cms.EDAnalyzer('DD4hepTestDDDWorld',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
