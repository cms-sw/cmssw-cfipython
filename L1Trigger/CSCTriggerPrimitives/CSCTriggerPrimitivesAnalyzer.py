import FWCore.ParameterSet.Config as cms

def CSCTriggerPrimitivesAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCTriggerPrimitivesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
